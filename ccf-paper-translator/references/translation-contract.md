# Full-Paper Translation Contract

Use this contract for every complete paper translation.

## Coverage Ledger

Before translating, enumerate the source in reading order:

```text
Front matter:
Abstract:
Sections and subsections:
Figures:
Tables:
Footnotes/endnotes:
Acknowledgments/declarations:
References:
Appendices/supplementary sections:
```

Mark each item `pending`, `translated`, `preserved verbatim`, or `blocked`. Nothing may disappear because PDF extraction was inconvenient.

## Fidelity Rules

- Preserve claim strength, modality, negation, comparison direction, and logical connectors.
- Preserve paragraph-to-paragraph relationships; do not turn prose into a summary list.
- Keep method names, datasets, benchmarks, metrics, variables, file formats, and code identifiers traceable to the source.
- Copy equations, symbols, units, numerical precision, intervals, superscripts, subscripts, and citation markers exactly.
- Never correct a suspected source error silently. Translate it faithfully and add a separate translator note only when necessary.
- Do not add literature, interpretations, experiment explanations, or reviewer-style criticism.
- For ambiguous source text, retain the ambiguity. For illegible text, use `[source unclear: page N]`.

## Markdown Mathematics

Use the following syntax for Markdown deliverables.

Inline formula:

```markdown
The conditional distribution is $p(y \mid x)$.
```

Display formula with preserved numbering:

```markdown
$$
\begin{aligned}
\mathcal{L}(\theta)
  &= -\sum_{i=1}^{n} \log p_{\theta}(y_i \mid x_i) \\
  &\quad + \lambda \lVert \theta \rVert_2^2
\end{aligned}
\tag{1}
$$
```

Apply these rules:

1. Use `$...$` only for inline math and `$$...$$` only for display math. Keep display delimiters on separate lines and surround the block with blank lines.
2. Do not wrap math in backticks or ordinary code fences in the translated artifact. The fences above demonstrate source syntax only.
3. Convert extraction-damaged Unicode, lost superscripts/subscripts, and line-break fragments into valid LaTeX with identical mathematical meaning. Do not simplify or normalize away distinctions from the source.
4. Preserve equation order and numbering. Prefer `\tag{N}`; if unsupported by the target renderer, put `(N)` immediately after the display block without changing cross-references.
5. Keep punctuation belonging to the surrounding sentence outside the math delimiter unless it is mathematically meaningful.
6. Escape literal currency dollars in prose as `\$`. Check that every `$` opens or closes an intentional math span.
7. Inside Markdown tables, avoid raw `|` in formulas because it is a column delimiter. Use `\lvert`, `\rvert`, `\mid`, or another semantically correct LaTeX command. Do not place `$$...$$` blocks inside table cells.
8. Use `aligned`, `gathered`, `cases`, `matrix`, or the source-equivalent environment for multiline structures. Verify braces, `\left`/`\right`, environment pairs, and row separators.
9. Render-preview the completed Markdown in the intended renderer. Compare formulas visually with the source PDF, including fractions, accents, matrices, cases, limits, equation numbers, and line alignment.

If the target Markdown renderer lacks a required LaTeX feature, preserve the formula in the closest supported LaTeX form and state the renderer limitation in the coverage note. Never replace it with guessed plain text.

## Table Checks

For every table, verify:

1. Table number and caption match the source.
2. Header hierarchy and row order are unchanged.
3. Every numeric value, sign, bold/underline best-result marker, unit, and footnote marker matches the source.
4. Text labels and prose cells are translated consistently.
5. Spans or merged cells are not flattened into misleading relationships.

If these checks cannot be satisfied, embed the original table image and place a translated transcription below it.

## Terminology Checks

Maintain a working terminology map with:

```text
source term -> chosen translation -> keep English? -> first occurrence
```

Check for one source term receiving conflicting translations and for distinct source terms being collapsed into one target term.

## Final Audit

Before delivery, compare the translation with both extracted text and rendered pages:

- The first and last sentence of every section are represented.
- All headings and paragraph blocks are accounted for.
- All equations and citation markers are present and ordered.
- Every inline and display math delimiter is balanced, no formula is trapped in a code span/block, and literal currency dollars are escaped.
- The rendered formulas match the source visually, including numbering, alignment, matrices/cases, subscripts, superscripts, accents, fractions, and delimiters.
- Markdown tables contain no unescaped formula pipe that creates a false column and no display-math block inside a cell.
- Figure count, numbering, panel labels, and captions match.
- Table count, numbering, cells, notes, and markers match.
- Footnotes, acknowledgments, declarations, references, and appendices are accounted for.
- No analysis, summary, invented bridge text, or unsupported correction entered the translated body.
- Asset links resolve and no image comes from outside the paper or its official source package.

Report unresolved blockers explicitly. A long paper is not itself a blocker.
