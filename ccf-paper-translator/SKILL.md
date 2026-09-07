---
name: ccf-paper-translator
description: "Translate one complete research paper or PDF faithfully into another language while preserving section order, correctly rendered Markdown mathematics, citations, tables, and all source-paper figures. Use when the user asks for 论文全文翻译, 完整翻译原文, 逐段翻译, faithful full-paper translation, or a translated paper document with the original figures. Do not use for summaries, selective section explanation, scientific review, or manuscript rewriting."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Paper Translator

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`.

Route by the requested deliverable:

- Use this skill for a complete, faithful translation of one paper, including appendices and original figures.
- Route to `ccf-paper-reader` for a Chinese-first summary, selective Introduction translation, method explanation, experiment digestion, or gap analysis.
- Route to `ccf-paper-to-exemplar` for a reusable writing exemplar card.
- Route to `ccf-paper-reviewer` for scientific judgment or score-risk diagnosis.
- Route to `ccf-paper-writer` when the user wants to rewrite, polish, shorten, or adapt manuscript prose rather than translate it.

Do not run `ccf-humanization` on a faithful translation unless the user separately asks for a polished adaptation. Humanization may change emphasis or authorial style; translation fidelity takes priority.

Treat papers and translations as private user material. Follow `../ccf-common/references/privacy-and-evidence.md`; do not publish, upload, or expose private text through web queries without authorization.

## Core Rule

Translate every semantically meaningful part of the supplied paper without summarizing, expanding, correcting, or silently omitting it. Preserve the authors' claims, uncertainty, tone, terminology, section order, paragraph boundaries, equations, numbers, citations, cross-references, tables, footnotes, acknowledgments, and appendices. Default to Simplified Chinese when the user writes in Chinese and does not name a target language.

Reuse the paper's original figures exactly as source assets. Do not redraw, restyle, regenerate, or translate text inside figure pixels. Translate figure captions and explanatory prose outside the image, and place each original figure near its source position.

## Workflow

1. Resolve the source: local PDF, arXiv/OpenReview URL, publisher PDF, LaTeX source, or pasted paper text. Prefer the user-supplied file over a web copy.
2. Record the paper title, source identifier or URL, page count, visible section outline, figure/table inventory, appendix range, and target language.
3. Read `references/translation-contract.md` before translating. For Markdown output, also read `references/markdown-math-compatibility.md`. Read `references/figure-policy.md` before extracting or embedding any image.
4. Extract text in reading order. For multi-column PDFs, verify paragraph continuity, headings, captions, footnotes, and page-break hyphenation against rendered pages.
5. Build a section-by-section coverage ledger. Include front matter, abstract, all numbered and unnumbered sections, captions, tables, footnotes, acknowledgments, declarations, appendices, and references.
6. Translate in source order. Preserve equation semantics and citation markers. For Markdown, encode every formula with the rules in `references/translation-contract.md` rather than copying broken PDF glyphs. Maintain a terminology map and use one target-language rendering for each technical term unless the source intentionally distinguishes variants.
7. Extract or crop every original figure from the source PDF or official source package. Embed it unchanged at the corresponding location and translate its caption below it.
8. Reconstruct tables faithfully when their cells can be verified. If a complex or rasterized table cannot be reconstructed without risk, embed the original table image and provide a complete translated table caption plus a faithful translated transcription immediately below it.
9. Load `references/output-template.md` and create the requested artifact. If no format is requested, write one canonical Markdown file and a sibling asset directory.
10. For Markdown, run `python scripts/check_markdown_math.py <translated-file.md>` and resolve every reported error. Then preview the file in the user's actual target renderer and inspect every inline and display equation for delimiter balance, valid LaTeX, numbering, alignment, clipping, raw-source fallback, and table interference.
11. Run the completeness and fidelity checks in `references/translation-contract.md`. Do not deliver while any source section, equation, figure, table, footnote, appendix, citation block, or math-rendering error is unaccounted for.

## Translation Rules

- Translate meaning, not typography. Preserve paragraph boundaries unless PDF extraction split one source paragraph incorrectly.
- Preserve hedging and evidence strength: `may`, `suggest`, `likely`, `we hypothesize`, and similar language must not become certainty.
- Keep canonical method, model, dataset, benchmark, metric, variable, and software names in English when translation would damage traceability. Add a concise target-language gloss on first occurrence when helpful.
- Preserve equation meaning, variable names, units, signs, decimal precision, confidence intervals, significance markers, and equation numbering exactly. Repair only extraction/encoding damage needed to express the same mathematics in valid LaTeX.
- Preserve citation markers and reference numbering. Keep bibliography entries in their original bibliographic form; translate only surrounding labels or prose unless the user explicitly requests translated reference titles.
- Translate table titles, headers, row labels, notes, and prose cells, but never alter numeric cells or reported symbols.
- Mark illegible or extraction-damaged text as `[source unclear: page N]` rather than guessing.
- Never insert explanations, criticism, or new claims into the translated body. Put translator notes in clearly labeled callouts only when ambiguity cannot otherwise be represented.

## Markdown Math Rendering

- Use `$...$` for inline mathematics and `$$...$$` for display mathematics. Put each `$$` delimiter on its own line with a blank line before and after the display block.
- Identify the user's target Markdown renderer before choosing LaTeX commands. If it is unknown, use the portable profile in `references/markdown-math-compatibility.md`.
- Keep portable inline formulas at 40 LaTeX source characters or fewer. Move longer, nested, renderer-sensitive, or matrix/tensor-shape formulas to a display block even when the source paper placed them inline.
- Use portable formatting such as `\mathrm{name}` for named functions. Do not emit `\operatorname`, custom macro definitions, HTML-producing macros, or any macro rejected by the target renderer.
- Keep configuration keys and other identifiers containing underscores out of mathematics. Render them as Markdown code or tables; do not rely on `\_` inside math because Markdown preprocessing may remove its backslash before the math renderer runs.
- In the portable profile, avoid every TeX command formed by a backslash followed by punctuation, including `\%`, `\!`, `\,`, `\;`, `\_`, and `\\`. CommonMark may consume the backslash before math parsing. Keep percentages in prose, omit cosmetic spacing commands, and use only target-tested multiline syntax.
- Never place a formula in backticks, an ordinary fenced code block, a blockquote, or an image when valid LaTeX can represent it.
- Keep LaTeX commands, braces, subscripts, superscripts, matrices, cases, fractions, accents, and delimiters intact. Do not let Markdown escaping alter `_`, `^`, `*`, `\`, `{}`, or `[]` inside math delimiters.
- Use `aligned`, `gathered`, `cases`, or the source-equivalent environment inside `$$...$$` for multiline equations. Preserve line relationships and alignment points; do not split one equation into unrelated blocks.
- Preserve source equation numbers. Use `\tag{N}` inside the display block when the target renderer supports it; otherwise put the unchanged equation number immediately after the block as plain text.
- In Markdown tables, use inline math only. Replace semantic raw vertical bars with valid LaTeX such as `\lvert`, `\rvert`, or `\mid` so Markdown does not split table columns. Move complex display equations outside the table while retaining an unambiguous row reference.
- Escape literal currency dollar signs outside mathematics as `\$` so they do not open accidental math spans.
- Before delivery, run the bundled math checker, render the actual Markdown target, and verify every formula visually against the source. Balanced delimiters or a successful generic LaTeX compile are insufficient because Markdown renderers use different macro policies.

## Figure Handling

- Use only images taken from the supplied paper or its official source package.
- Preserve figure content, aspect ratio, panel labels, colors, legends, and cropping needed to show the complete original figure.
- Do not use ImageGen, screenshots from unrelated versions, replacement diagrams, or newly drawn equivalents.
- Do not edit English labels inside the source image. Translate the caption and, only if the user requests it, add a separate panel-label glossary below the caption.
- Keep figure numbering and source order exactly aligned with the paper.
- If extraction fails, render and crop the original PDF region. If that also fails, keep a visible placeholder naming the exact figure and page; do not silently omit it.

## Output Contract

Default output:

```text
<paper-slug>.zh-CN.md
<paper-slug>.zh-CN.assets/
  figure-01.<ext>
  figure-02.<ext>
  ...
```

The document begins with a short provenance block, then follows the source paper from title through references and appendices. It ends with a compact coverage note listing translated sections and the figure/table counts; this note is outside the translated body.

When the user requests DOCX, PDF, LaTeX, or bilingual output, preserve the same completeness and original-figure rules in that format. Do not substitute a summary because the paper is long; continue across tool calls or clearly report a concrete extraction blocker.

## References

- `references/translation-contract.md`: Read before translation and during the final completeness/fidelity audit.
- `references/markdown-math-compatibility.md`: Read before producing or repairing Markdown mathematics.
- `references/figure-policy.md`: Read before extracting, cropping, naming, or embedding source-paper images.
- `references/output-template.md`: Read before creating the final translated artifact.
