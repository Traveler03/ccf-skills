---
name: ccf-paper-reader
description: "Read and digest one research paper or PDF into a Chinese-first structured note for CCF research workflows. Use when the user asks to read a paper, 整理论文, 精读论文, 总结 introduction, 翻译 introduction, summarize experiments, extract problem/gap/insight/method/evidence, explain methodology figures, or produce a paper-reading document. Do not use as the main skill for broad literature search, strict paper review/scoring, or writing exemplar extraction."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Paper Reader

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`.

Route by primary intent:

- Use this skill for one-paper reading notes, Chinese-first summaries, Introduction translation, method/experiment extraction, and figure-aware paper digestion.
- Route to `ccf-literature-searcher` for broad related-work search, closest-work clustering, benchmark discovery, or novelty maps across many papers.
- Route to `ccf-paper-reviewer` for strict scientific review, score-risk diagnosis, reviewer simulation, or acceptance-risk critique.
- Route to `ccf-paper-to-exemplar` when the user wants a reusable writing exemplar card.
- Route to `ccf-idea-optimizer` after reading only when the user asks to turn gaps into an idea.

Treat papers, notes, and user project plans as private user material. Before browsing, exact private quoting, or source claims, follow `../ccf-common/references/privacy-and-evidence.md`.

## Core Rule

Read the paper to support research understanding and gap discovery, not to produce a generic abstract. Write mainly in Chinese. Keep necessary English terms, method names, dataset names, metric names, and paper-specific terminology in English, but add a short Chinese gloss after important English phrases when first used. Explain metrics and numeric results before interpreting them. Separate paper claims from reader inference.

## Workflow

1. Identify input type: arXiv URL, PDF path, paper title, repository link, or pasted text.
2. Read metadata, abstract, Introduction, method overview, figures, experiments, limitations, and conclusion. If time is limited, prioritize Introduction, method figure, experiment setup, main results, ablations, and limitations.
3. Load `references/reading-checklist.md` before producing the reading note.
4. Load `references/figure-policy.md` before extracting, embedding, or describing methodology figures. Default to embedding the methodology figure directly in the note whenever feasible.
5. Load `references/output-template.md` and fill only the sections supported by the paper. Mark missing evidence as `未找到` or `需要进一步查证`.
6. If the output belongs in a project repo, place the note under that repo's paper-note convention when known; otherwise return the note inline.

## Reading Focus

Always extract:

- 论文解决的现有问题是什么。
- 现有方法或评估有什么 gap。
- 核心 insight 是什么。
- 方法解决了什么，输入输出是什么，关键机制是什么。
- 实验怎么做：benchmark、baseline、metric、main result、ablation、generalization、regression/cost/budget control，并用中文解释每组实验想回答什么问题、指标怎么算、数字代表什么。
- 作者没有解决什么，以及对用户当前研究方向有什么启发。未解决问题要写得具体：缺什么验证、为什么现有实验不能证明、可能怎么补实验。

## Output Language

- Use Chinese for explanations, section summaries, experiment interpretation, and gap interpretation.
- Keep paper title, method names, benchmark names, metric names, component names, and unavoidable technical terms in English.
- For important English phrases, add a Chinese gloss on first use, such as `component observability`（组件可观察性）, `regression foresight`（回归风险预判）, or `change manifest`（变更清单）. Do not add glosses to every repeated occurrence.
- For every important numeric result, explain the metric in plain Chinese, whether higher or lower is better, what the numerator/denominator means when applicable, how it compares to a baseline or random level, and what the number implies.
- Translate Introduction selectively. Prefer paragraph-level faithful translation plus a short Chinese interpretation, not a full verbose rewrite unless the user asks.
- Do not overstate novelty. Use `论文声称`, `作者认为`, `从实验看`, or `我的推断` to separate evidence levels.

## Figure Handling

For methodology figures:

- Identify figure number, page, caption, and what each module means.
- Explain the figure in Chinese using the paper's own terminology.
- Crop or render the relevant methodology figure whenever feasible and include it directly in the document.
- Merge the method overview and methodology figure explanation into one section when possible. Put a plain Chinese method explanation immediately after each embedded figure: module-by-module meaning, data/control flow, key operation, and how the figure supports the paper's insight.
- Do not output paper-internal figure metadata as standalone bullets, such as `Figure:`, `Page:`, or `Caption:`. Keep only the image, a short source note if needed, and the Chinese explanation.
- If figure extraction fails, state the failure reason and still provide figure number, page, caption, source link, and the Chinese method explanation.

## Output Contract

Default to a Markdown reading note using `references/output-template.md`.

For quick reading, include:

```text
一句话总结
Problem / Gap / Insight / Method
方法图通俗解释
Introduction 核心翻译
实验总结（主实验、消融实验、泛化/迁移、回归/成本）
没解决什么
对我们方向的启发
```

For standard reading, include the full template, a merged method-and-figure explanation, Chinese-first experiment sections, limitation/gap analysis, and action items. Use tables only when they improve comparison, and prefer Chinese table headers.

## References

- `references/reading-checklist.md`: Read before extracting paper content or deciding what sections matter.
- `references/output-template.md`: Read before writing the final reading note.
- `references/figure-policy.md`: Read before extracting, embedding, or describing paper figures.
