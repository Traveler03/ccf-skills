#!/usr/bin/env python3
"""Lint Markdown mathematics for a conservative cross-renderer profile."""

from __future__ import annotations

import argparse
import re
import string
import sys
from pathlib import Path


FORBIDDEN_MACROS = {
    "DeclareMathOperator": "write the name with \\mathrm{...}",
    "def": "custom macro definitions are not portable",
    "href": "HTML and link-producing math macros are not portable",
    "htmlClass": "HTML-producing math macros are not portable",
    "htmlId": "HTML-producing math macros are not portable",
    "htmlStyle": "HTML-producing math macros are not portable",
    "includegraphics": "embed figures with Markdown, not a math macro",
    "newcommand": "custom macro definitions are not portable",
    "operatorname": "write the name with \\mathrm{...}",
    "renewcommand": "custom macro definitions are not portable",
    "require": "renderer-extension macros are not portable",
    "url": "HTML and link-producing math macros are not portable",
}

MACRO_RE = re.compile(r"\\([A-Za-z]+)")
ENVIRONMENT_RE = re.compile(r"\\(begin|end)\{([^{}]+)\}")
INLINE_CODE_RE = re.compile(r"(`+)(.*?)\1")
TEXTUAL_GROUP_WITH_SUBSCRIPT_RE = re.compile(
    r"\\(?:mathrm|mathtt|text|textit)\{[^{}]*_[^{}]*\}"
)


def is_escaped(text: str, index: int) -> bool:
    backslashes = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        backslashes += 1
        index -= 1
    return backslashes % 2 == 1


def unescaped_positions(text: str, character: str) -> list[int]:
    return [
        index
        for index, value in enumerate(text)
        if value == character and not is_escaped(text, index)
    ]


def brace_error(formula: str) -> str | None:
    depth = 0
    for index, value in enumerate(formula):
        if is_escaped(formula, index):
            continue
        if value == "{":
            depth += 1
        elif value == "}":
            depth -= 1
            if depth < 0:
                return "closing brace has no matching opening brace"
    if depth:
        return f"formula has {depth} unclosed brace(s)"
    return None


def check_formula(
    formula: str,
    line_number: int,
    errors: list[str],
    max_inline_length: int,
    inline: bool,
    extra_forbidden: set[str],
) -> None:
    label = "inline" if inline else "display"
    if not formula.strip():
        errors.append(f"line {line_number}: empty {label} formula")
        return

    if inline and len(formula) > max_inline_length:
        errors.append(
            f"line {line_number}: inline formula has {len(formula)} source characters "
            f"(limit {max_inline_length}); move it to a display block"
        )

    if inline and "\\mathbb" in formula and "\\times" in formula:
        errors.append(
            f"line {line_number}: matrix/tensor shape declarations are not portable "
            "inline; move this formula to a display block"
        )

    punctuation_escapes = sorted(
        {
            match.group(1)
            for match in re.finditer(r"\\(.)", formula)
            if match.group(1) in string.punctuation
        }
    )
    if punctuation_escapes:
        commands = ", ".join(f"\\{value}" for value in punctuation_escapes)
        errors.append(
            f"line {line_number}: Markdown-escapable punctuation command(s) "
            f"{commands} inside math are not portable; Markdown may consume the "
            "backslash before math parsing"
        )

    formula_without_escaped_underscores = formula.replace(r"\_", "")
    if TEXTUAL_GROUP_WITH_SUBSCRIPT_RE.search(formula_without_escaped_underscores):
        errors.append(
            f"line {line_number}: underscore inside a text-style math group can create "
            "double subscripts; put the identifier in Markdown code or a table"
        )

    problem = brace_error(formula)
    if problem:
        errors.append(f"line {line_number}: {problem}")

    left_count = len(re.findall(r"\\left\b", formula))
    right_count = len(re.findall(r"\\right\b", formula))
    if left_count != right_count:
        errors.append(
            f"line {line_number}: mismatched \\left/\\right "
            f"({left_count} versus {right_count})"
        )

    environment_stack: list[str] = []
    for action, environment in ENVIRONMENT_RE.findall(formula):
        if action == "begin":
            environment_stack.append(environment)
        elif not environment_stack or environment_stack.pop() != environment:
            errors.append(
                f"line {line_number}: unmatched \\end{{{environment}}} environment"
            )
            break
    else:
        if environment_stack:
            errors.append(
                f"line {line_number}: unclosed math environment(s): "
                + ", ".join(environment_stack)
            )

    forbidden = set(FORBIDDEN_MACROS) | extra_forbidden
    for macro in sorted(set(MACRO_RE.findall(formula)) & forbidden):
        reason = FORBIDDEN_MACROS.get(macro, "forbidden by command-line profile")
        errors.append(f"line {line_number}: forbidden macro \\{macro}: {reason}")


def lint_file(path: Path, max_inline_length: int, extra_forbidden: set[str]) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    in_fence = False
    fence_marker = ""
    in_display = False
    display_start = 0
    display_lines: list[str] = []

    for index, original_line in enumerate(lines, start=1):
        stripped = original_line.strip()

        fence_match = re.match(r"^\s*(```+|~~~+)", original_line)
        if fence_match and not in_display:
            marker = fence_match.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if in_fence:
            continue

        if "$$" in original_line and stripped != "$$":
            errors.append(
                f"line {index}: display delimiter $$ must be alone on its line"
            )
            continue

        if stripped == "$$":
            if not in_display:
                if index > 1 and lines[index - 2].strip():
                    errors.append(
                        f"line {index}: add a blank line before the opening $$"
                    )
                in_display = True
                display_start = index
                display_lines = []
            else:
                formula = "\n".join(display_lines)
                check_formula(
                    formula,
                    display_start,
                    errors,
                    max_inline_length,
                    inline=False,
                    extra_forbidden=extra_forbidden,
                )
                if index < len(lines) and lines[index].strip():
                    errors.append(
                        f"line {index}: add a blank line after the closing $$"
                    )
                in_display = False
                display_start = 0
                display_lines = []
            continue

        if in_display:
            display_lines.append(original_line)
            continue

        line = INLINE_CODE_RE.sub("", original_line)
        dollars = unescaped_positions(line, "$")
        if len(dollars) % 2:
            errors.append(f"line {index}: unmatched inline $ delimiter")
            continue

        table_line = line.lstrip().startswith("|")
        for start, end in zip(dollars[0::2], dollars[1::2]):
            formula = line[start + 1 : end]
            if table_line and unescaped_positions(formula, "|"):
                errors.append(
                    f"line {index}: raw | inside table math can split a Markdown column; "
                    "use \\lvert, \\rvert, or \\mid"
                )
            check_formula(
                formula,
                index,
                errors,
                max_inline_length,
                inline=True,
                extra_forbidden=extra_forbidden,
            )

    if in_fence:
        errors.append("end of file: unclosed fenced code block")
    if in_display:
        errors.append(f"line {display_start}: unclosed display math block")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check Markdown math against a conservative portable profile."
    )
    parser.add_argument("files", nargs="+", type=Path, help="Markdown files to check")
    parser.add_argument(
        "--max-inline-length",
        type=int,
        default=40,
        help="maximum LaTeX source characters inside inline math (default: 40)",
    )
    parser.add_argument(
        "--forbid-macro",
        action="append",
        default=[],
        metavar="NAME",
        help="add a macro name to the denylist; omit the leading backslash",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_inline_length < 1:
        print("error: --max-inline-length must be positive", file=sys.stderr)
        return 2

    total_errors = 0
    for path in args.files:
        if not path.is_file():
            print(f"{path}: file not found", file=sys.stderr)
            total_errors += 1
            continue
        errors = lint_file(path, args.max_inline_length, set(args.forbid_macro))
        if errors:
            print(f"{path}: {len(errors)} error(s)")
            for error in errors:
                print(f"  - {error}")
            total_errors += len(errors)
        else:
            print(f"{path}: math check passed")

    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
