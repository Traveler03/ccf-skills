# Original-Figure Policy

The translated paper must reuse the source paper's own figures.

## Source Priority

Use figure assets in this order:

1. Original image files from an official LaTeX/source package supplied by the user or linked by the official paper record.
2. Embedded raster images extracted losslessly from the supplied PDF.
3. A high-resolution crop rendered from the exact supplied PDF page for vector or composite figures.

Do not use search-engine thumbnails, third-party slides, later paper versions, regenerated diagrams, or visually similar replacements.

## Placement And Naming

- Inventory figure number, page, panels, caption, and source position before extraction.
- Use stable names such as `figure-01.png`, `figure-02a.png`, or the original source filename when it is already clear.
- Keep every figure near the translated version of its original location.
- Preserve aspect ratio and enough resolution for labels to remain readable.
- Crop only page margins and unrelated page content; do not crop legends, panel labels, callouts, or caption-referenced content.

## Translation Boundary

- Leave all pixels unchanged, including English text embedded in the figure.
- Translate the figure caption outside the image.
- When the user asks for translated in-figure labels, add a separate panel-label glossary by default. Editing the source image requires a separate explicit request and must retain an untouched original copy.
- Preserve figure numbering, subfigure letters, and source cross-references.

## Failure Handling

If an image cannot be extracted cleanly, render and crop the original PDF region. If that fails, use a visible placeholder:

```text
[Original Figure N could not be extracted from source page P: <reason>]
```

Keep the translated caption and report the missing asset in the coverage note. Never silently omit a figure.
