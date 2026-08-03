# Figure Policy

Use this file before extracting, embedding, or describing figures from a paper.

## Default

For methodology figures, directly embed the figure image in the reading note whenever feasible. Always capture:

- Figure number.
- Page number.
- Caption.
- Source paper link.
- Local image path or Markdown image tag.
- Chinese explanation of each important module.
- Why this figure matters for the paper's method.

## Embedding Rule

Default behavior:

- Render the relevant PDF page or crop the methodology figure when feasible.
- Save the image near the note using a clear name, such as `fig-method-overview.png`.
- Include the image with Markdown syntax.
- Add a source note with paper title, figure number, page, caption, and link.
- Do not crop unrelated figures or long copyrighted sections.

If the note will be committed to a public repository, still embed the figure by default because this skill is configured for figure-inclusive research notes. Keep the source note immediately adjacent to the image.

If extraction fails:

- State the reason, such as missing PDF, scanned page, crop failure, unavailable figure, or unsupported format.
- Still provide figure number, page, caption, source link, and the Chinese method explanation.

## Figure Explanation Checklist

After each embedded methodology figure, explain in plain Chinese and avoid repeating a separate method section:

- What enters the pipeline.
- What each module does.
- What is optimized, searched, trained, retrieved, or verified.
- What exits the pipeline.
- Which part corresponds to the paper's core insight.
- Which part is only engineering support.
- What problem/gap this figure helps solve.
- Which experimental claim this figure is meant to support, if any.
