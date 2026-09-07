# Markdown Math Compatibility

Markdown math is not a single standard. GitHub, Codex previews, editors, static-site generators, KaTeX, and MathJax can accept different delimiters and macro sets. A formula that compiles in a generic LaTeX engine can still fall back to raw source or trigger an error in the delivery renderer.

## Target First

1. Record the renderer in the coverage ledger when the user names one.
2. Preview in that renderer, not only in Pandoc, a PDF export, or a different Markdown application.
3. If the renderer is unknown or cannot be automated, use the portable profile below and report that visual verification in the final target remains required.

## Portable Profile

- Use `$...$` for short inline formulas and blank-line-separated `$$...$$` blocks for display formulas.
- Put a whitespace character before every opening inline `$` unless it begins the line. Never attach an opening delimiter directly to Chinese/English punctuation, parentheses, emphasis markers, or prose: write `， $x$` rather than `，$x$`. Some Markdown pipelines otherwise leave that formula, or every formula in the same text block, as raw source.
- Keep inline LaTeX source at 40 characters or fewer. Move longer formulas, nested function calls, long vectors, matrix/tensor shape declarations, and multi-relation expressions to display blocks.
- Prefer common primitive commands such as `\mathbf`, `\mathrm`, `\mathbb`, `\mathcal`, `\frac`, `\sqrt`, `\sum`, `\prod`, `\left`, `\right`, `\lvert`, `\rvert`, `\mid`, `\cdot`, `\times`, and standard Greek-letter commands.
- Write named functions as `\mathrm{swish}`, `\mathrm{concat}`, or another `\mathrm{...}` expression. Do not use `\operatorname` in the portable profile.
- Put configuration keys and identifiers such as `mlp_dim` or `num_kv_heads` in Markdown code spans or tables, not inside math. Do not encode their underscores as `\_`: some Markdown pipelines consume that escape before invoking the math renderer, turning one textual identifier into multiple TeX subscripts.
- Avoid TeX commands made from a backslash plus punctuation, including `\%`, `\!`, `\,`, `\;`, `\_`, `\{`, `\}`, and `\\`. CommonMark can consume these escapes before invoking the math renderer. Write percentages as prose such as `9.1%`, omit cosmetic math-spacing commands, avoid escaped punctuation inside math, and use multiline syntax only after testing the target.
- Write primes explicitly with `^{\prime}` (or a source-equivalent explicit `\prime` construction). Do not leave a raw ASCII apostrophe such as `t'` inside math; a renderer failure in one formula can make all inline formulas in that Markdown block fall back to source text.
- Do not define macros with `\newcommand`, `\renewcommand`, `\DeclareMathOperator`, or `\def`.
- Do not use renderer-control or HTML-producing commands such as `\require`, `\href`, `\url`, `\includegraphics`, `\htmlClass`, `\htmlId`, or `\htmlStyle` inside math.
- Use `\tag` and multiline environments only after confirming target support. Otherwise place an equation number as plain text immediately after the display block.
- Keep prose and long identifier lists outside math when typography does not require mathematical layout.

An unsupported formula can cause later formulas in the same Markdown block to appear as literal `$...$`. Treat one renderer error as a document-level QA failure rather than an isolated cosmetic defect.

## Deterministic Check

Run from the skill directory:

    python scripts/check_markdown_math.py path/to/translation.md

The default check enforces whitespace before inline opening delimiters, explicit prime notation, the portable 40-character inline limit, display placement for dimension declarations, Markdown-safe punctuation handling, underscore-safe identifiers, display-delimiter layout, balanced braces and `\left`/`\right`, matched environments, table safety, and a denylist of non-portable macros. Use `--max-inline-length` only when the named target renderer has been tested with a different limit.

The checker is a gate, not a renderer. After it passes, visually inspect every equation in the actual target and compare it with the source paper.
