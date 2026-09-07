#!/usr/bin/env python3
"""Regression tests for the portable Markdown-math checker."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("check_markdown_math.py")
SPEC = importlib.util.spec_from_file_location("check_markdown_math", SCRIPT_PATH)
assert SPEC and SPEC.loader
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


def check(formula: str, *, inline: bool) -> list[str]:
    errors: list[str] = []
    CHECKER.check_formula(formula, 1, errors, 40, inline, set())
    return errors


def lint(markdown: str) -> list[str]:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "sample.md"
        path.write_text(markdown, encoding="utf-8")
        return CHECKER.lint_file(path, 40, set())


class PortableMathTests(unittest.TestCase):
    def test_rejects_escaped_underscore_identifier(self) -> None:
        errors = check(r"\mathrm{num\_kv\_heads}=1", inline=False)
        self.assertTrue(any("Markdown-escapable punctuation" in error for error in errors))

    def test_rejects_escaped_percent(self) -> None:
        errors = check(r"9.1\%", inline=True)
        self.assertTrue(any("Markdown-escapable punctuation" in error for error in errors))

    def test_rejects_cosmetic_spacing_command(self) -> None:
        errors = check(r"f\!(x)", inline=True)
        self.assertTrue(any("Markdown-escapable punctuation" in error for error in errors))

    def test_rejects_thin_space_command(self) -> None:
        errors = check(r"p(x),\,q(x)", inline=True)
        self.assertTrue(any("Markdown-escapable punctuation" in error for error in errors))

    def test_rejects_raw_underscore_in_text_style_group(self) -> None:
        errors = check(r"\mathrm{num_kv_heads}=1", inline=False)
        self.assertTrue(any("double subscripts" in error for error in errors))

    def test_rejects_inline_shape_declaration(self) -> None:
        errors = check(r"W_1\in\mathbb{R}^{w\times d}", inline=True)
        self.assertTrue(any("shape declarations" in error for error in errors))

    def test_accepts_display_shape_declaration(self) -> None:
        errors = check(r"W_1\in\mathbb{R}^{w\times d}", inline=False)
        self.assertEqual(errors, [])

    def test_rejects_operatorname(self) -> None:
        errors = check(r"\operatorname{swish}(x)", inline=True)
        self.assertTrue(any("forbidden macro" in error for error in errors))

    def test_accepts_nested_environments(self) -> None:
        formula = r"\begin{aligned}\begin{matrix}a\end{matrix}\end{aligned}"
        self.assertEqual(check(formula, inline=False), [])

    def test_rejects_inline_opener_attached_to_cjk_punctuation(self) -> None:
        errors = lint(r"观测，$\mathbf{o}_t$ 是状态。")
        self.assertTrue(any("opening inline $" in error for error in errors))

    def test_accepts_inline_opener_after_whitespace(self) -> None:
        self.assertEqual(lint(r"观测， $\mathbf{o}_t$ 是状态。"), [])

    def test_rejects_ascii_prime(self) -> None:
        errors = check(r"\mathbf{a}_{t'}", inline=True)
        self.assertTrue(any("ASCII apostrophe" in error for error in errors))

    def test_accepts_explicit_prime(self) -> None:
        self.assertEqual(check(r"\mathbf{a}_{t^{\prime}}", inline=True), [])


if __name__ == "__main__":
    unittest.main()
