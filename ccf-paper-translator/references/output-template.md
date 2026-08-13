# Full Translation Output Template

Use only sections that exist in the source, but preserve their source order and hierarchy.

```markdown
# <Translated paper title>

> Original title: <source title>
> Source: <DOI/arXiv/OpenReview/local source identifier>
> Target language: <language>
> Translation scope: Complete paper, including captions, tables, references, and appendices

<translated author/affiliation block when requested or semantically useful>

## Abstract

<faithful paragraph-by-paragraph translation>

## 1. <Translated section heading>

<translated paragraphs in source order>

Inline mathematics uses `$p(y \mid x)$`.

Display mathematics uses a blank-line-separated block:

$$
\begin{aligned}
<source-equivalent LaTeX>
\end{aligned}
\tag{1}
$$

![Original Figure 1](<paper-slug>.zh-CN.assets/figure-01.png)

**Figure 1. <Translated caption>**

<continue all sections, tables, footnotes, acknowledgments, declarations, references, and appendices>

---

## Translation coverage note

- Source pages:
- Sections translated:
- Figures embedded / source total:
- Tables translated or embedded / source total:
- Equations rendered / source total:
- Math-rendering limitations:
- Footnotes/endnotes:
- References:
- Appendices:
- Unresolved source or extraction issues:
```

For a bilingual request, place each source paragraph immediately before its translated paragraph. Do not switch to a summary table for long sections.
