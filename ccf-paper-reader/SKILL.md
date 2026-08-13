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
- Route to `ccf-paper-translator` when the user asks for a complete, faithful, paragraph-by-paragraph paper translation or a translated document that preserves every original figure.
- Route to `ccf-literature-searcher` for broad related-work search, closest-work clustering, benchmark discovery, or novelty maps across many papers.
- Route to `ccf-paper-reviewer` for strict scientific review, score-risk diagnosis, reviewer simulation, or acceptance-risk critique.
- Route to `ccf-paper-to-exemplar` when the user wants a reusable writing exemplar card.
- Route to `ccf-idea-optimizer` after reading only when the user asks to turn gaps into an idea.

Treat papers, notes, and user project plans as private user material. Before browsing, exact private quoting, or source claims, follow `../ccf-common/references/privacy-and-evidence.md`.

## Core Rule

Read the paper to support research understanding and gap discovery, not to produce a generic abstract. Write mainly in Chinese. Keep necessary English terms, method names, dataset names, metric names, and paper-specific terminology in English, but every non-trivial English technical phrase must carry a Chinese gloss in parentheses on first use in the note or section where it is introduced. This includes method components, process names, metric names, artifact names, experiment setting names, table labels, JSON keys/values, section subtitles, and figure-module labels. Skip only paper titles, author names, raw URLs, repository names, literal code paths, and obvious model/benchmark names after their role has already been explained. If an English phrase is necessary but the Chinese meaning is not obvious to a Chinese reader, gloss it. Explain metrics and numeric results before interpreting them. When a method has structured artifacts or pipeline data, include a minimal bilingual JSON-style example with Chinese glosses in parentheses inside the JSON itself, then explain the data-dependency flow as a coherent simplified DAG: a connected main chain, side inputs that join the chain, and any feedback loop. Do not imply a linear field-to-field flow when fields are actually parallel inputs. Separate paper claims from reader inference.

## Workflow

1. Identify input type: arXiv URL, PDF path, paper title, repository link, or pasted text.
2. Read metadata, abstract, Introduction, method overview, figures, experiments, limitations, and conclusion. If time is limited, prioritize Introduction, method figure, experiment setup, main results, ablations, and limitations.
3. Load `references/reading-checklist.md` before producing the reading note.
4. Load `references/figure-policy.md` before extracting, embedding, or describing methodology figures. Default to embedding the methodology figure directly in the note whenever feasible.
5. Load `references/output-template.md` and fill only the sections supported by the paper. Mark missing evidence as `未找到` or `需要进一步查证`.
6. Before finalizing, run a manual gloss pass: scan headings, bullets, tables, JSON examples, figure explanations, and experiment sections for English phrases that lack Chinese parentheses. Add glosses where missing, especially for multi-word technical phrases such as `search budget（搜索预算）`, `inference budget（推理预算）`, `open-ended exploration（开放式探索）`, or `archive sampling（档案采样）`. Treat table headers, JSON string values, figure-module names, and metric names as high-risk locations. If a note still contains a bare multi-word English technical phrase outside a title, URL, code path, citation, or already-explained benchmark/model name, revise it before delivering.
7. If the output belongs in a project repo, place the note under that repo's paper-note convention when known; otherwise return the note inline.

## Reading Focus

Always extract:

- 论文解决的现有问题是什么。
- 现有方法或评估有什么 gap。
- 核心 insight 是什么。
- 方法解决了什么，输入输出是什么，关键机制是什么。
- 全文关键英文术语是否都有中文括注。对所有非平凡英文技术短语、方法组件、实验设置、指标、产物名、表头和 JSON 字段/值，首次出现必须写成 `English phrase（中文解释）`。如果同一术语在新章节隔得较远、会影响理解，可以再次括注。
- 方法或 pipeline 中间数据长什么样。若论文包含 manifest、trace report、memory entry、tool call、workflow state、evaluation record 等结构化产物，给出一个最小 JSON-style example。JSON 内部字段名应自带中文括注，例如 `failure_evidence（失败证据）`；必要的短字符串值也可加括注，例如 `fail（失败）`。示例要标明是“理解用最小示例”还是“论文原始格式”。示例后必须补一段连贯的“字段流向/简化流程图”：先写一条主链，把模块输入输出连起来；再标注上下文、证据、约束、预测等旁路字段如何接入主链；最后说明验证结果如何回流到下一轮或历史。不要用孤立表格替代主链。
- 实验怎么做：benchmark、baseline、metric、main result、ablation、generalization、regression/cost/budget control，并用中文解释每组实验想回答什么问题、指标怎么算、数字代表什么。
- 作者没有解决什么，以及对用户当前研究方向有什么启发。未解决问题要写得具体：缺什么验证、为什么现有实验不能证明、可能怎么补实验。

## Output Language

- Use Chinese for explanations, section summaries, experiment interpretation, and gap interpretation.
- Keep paper title, method names, benchmark names, metric names, component names, and unavoidable technical terms in English, but make the surrounding explanation Chinese-first.
- For English technical phrases, add a Chinese gloss on first use, such as `component observability`（组件可观察性）, `regression foresight`（回归风险预判）, or `change manifest`（变更清单）. Treat this as mandatory for all non-trivial English phrases, not optional. Single obvious names such as `AHE`, `DGM`, `SWE-bench`, or `GPT-5` may remain bare after their role is explained once, but phrases such as `archive sampling（档案采样）`, `self-modification（自修改）`, `open-ended exploration（开放式探索）`, `fitness evaluation（适应度评估）`, `search budget（搜索预算）`, `feedback budget（反馈预算）`, and `repair lineage（修复谱系）` need glosses.
- Do not use English-only labels for concepts that can be written in Chinese. Prefer `主实验` over `Main Experiment`, `消融实验` over `Ablation`, and `指标解释` over `Metric explanation`. If an English label is retained because it is a paper term, write it as `English（中文）`.
- In tables, prefer Chinese column headers. If an English term must appear in a header or cell, add a compact gloss there too, for example `pass@1（一次尝试通过率）` or `Archive（候选档案）`.
- For every important numeric result, explain the metric in plain Chinese, whether higher or lower is better, what the numerator/denominator means when applicable, how it compares to a baseline or random level, and what the number implies.
- For JSON-style examples, keep the JSON valid and compact. Put Chinese glosses directly in keys or short categorical string values using parentheses, such as `predicted_fixes（预测会修好的任务）`. Do not use JSON comments. Avoid a separate field-translation list unless a field is still ambiguous after the inline gloss. Immediately after the JSON block, include a compact Chinese simplified-flow explanation. It must start with a connected main chain using real dependencies, for example `raw_trace + task_context -> evidence_extraction -> failure_evidence; task_context + failure_evidence + harness_state -> diagnosis -> edit; edit -> next_round_execution -> observed_result; predicted_impact + observed_result -> validation_verdict -> keep/rollback/history`. Then add 2-5 bullets explaining side inputs. A table may follow, but must not replace the connected main chain.
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

For standard reading, include the full template, a merged method-and-figure explanation, a minimal bilingual JSON-style pipeline/artifact example when applicable, an immediately following connected simplified-flow explanation for that JSON, Chinese-first experiment sections, focused evidence-driven gap analysis, and action items. Use tables only when they improve comparison, and prefer Chinese table headers.

## References

- `references/reading-checklist.md`: Read before extracting paper content or deciding what sections matter.
- `references/output-template.md`: Read before writing the final reading note.
- `references/figure-policy.md`: Read before extracting, embedding, or describing paper figures.
