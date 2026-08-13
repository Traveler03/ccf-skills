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
- Figure count, numbering, panel labels, and captions match.
- Table count, numbering, cells, notes, and markers match.
- Footnotes, acknowledgments, declarations, references, and appendices are accounted for.
- No analysis, summary, invented bridge text, or unsupported correction entered the translated body.
- Asset links resolve and no image comes from outside the paper or its official source package.

Report unresolved blockers explicitly. A long paper is not itself a blocker.
