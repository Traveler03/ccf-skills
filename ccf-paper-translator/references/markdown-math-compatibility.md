# Markdown Math Compatibility

Markdown math is not a single standard. GitHub, Codex previews, editors, static-site generators, KaTeX, and MathJax can accept different delimiters and macro sets. A formula that compiles in a generic LaTeX engine can still fall back to raw source or trigger an error in the delivery renderer.

## Target First

1. Record the renderer in the coverage ledger when the user names one.
2. Preview in that renderer, not only in Pandoc, a PDF export, or a different Markdown application.
3. If the renderer is unknown or cannot be automated, use the portable profile below and report that visual verification in the final target remains required.

## Portable Profile

- Use `$...$` for short inline formulas and blank-line-separated `$$...$$` blocks for display formulas.
- Keep inline LaTeX source at 40 characters or fewer. Move longer formulas, nested function calls, long vectors, model configurations, and multi-relation expressions to display blocks.
- Prefer common primitive commands such as `\mathbf`, `\mathrm`, `\mathbb`, `\mathcal`, `\frac`, `\sqrt`, `\sum`, `\prod`, `\left`, `\right`, `\lvert`, `\rvert`, `\mid`, `\cdot`, `\times`, and standard Greek-letter commands.
- Write named functions as `\mathrm{swish}`, `\mathrm{concat}`, or another `\mathrm{...}` expression. Do not use `\operatorname` in the portable profile.
- Do not define macros with `\newcommand`, `\renewcommand`, `\DeclareMathOperator`, or `\def`.
- Do not use renderer-control or HTML-producing commands such as `\require`, `\href`, `\url`, `\includegraphics`, `\htmlClass`, `\htmlId`, or `\htmlStyle` inside math.
- Use `\tag` and multiline environments only after confirming target support. Otherwise place an equation number as plain text immediately after the display block.
- Keep prose and long identifier lists outside math when typography does not require mathematical layout.

An unsupported formula can cause later formulas in the same Markdown block to appear as literal `$...$`. Treat one renderer error as a document-level QA failure rather than an isolated cosmetic defect.

## Deterministic Check

Run from the skill directory:

    python scripts/check_markdown_math.py path/to/translation.md

The default check enforces the portable 40-character inline limit, display-delimiter layout, balanced braces and `\left`/`\right`, matched environments, table safety, and a denylist of non-portable macros. Use `--max-inline-length` only when the named target renderer has been tested with a different limit.

The checker is a gate, not a renderer. After it passes, visually inspect every equation in the actual target and compare it with the source paper.
