# Paper Reading Checklist

Use this checklist to read one paper. The goal is to produce a research-useful Chinese note, not a generic summary.

## Evidence Labels

Use these labels when needed:

- `论文声称`: stated by the paper.
- `实验支持`: supported by the paper's experiments.
- `我的推断`: inferred by the reader.
- `未找到`: not found in the inspected sections.
- `需要进一步查证`: needs another source or full-paper check.

## Must Answer

1. 这篇论文想解决什么问题？
2. 它说 existing methods 有什么不足？
3. 它的核心 insight 是什么？
4. 它提出的方法输入是什么、输出是什么、关键机制是什么？
5. 它和最接近工作相比，真正变化在哪里？用通俗中文解释差别。
6. 它的主实验验证了什么 claim？主实验和消融实验要分开解释。
7. 它有没有 ablation（消融）、generalization（泛化）、robustness（鲁棒性）、cost（成本）、regression（回归）或 budget control（预算控制）？
8. 它没有验证什么？
9. 对用户当前项目的 gap 或 idea 有什么启发？

## Section Priorities

When time is short, read in this order:

1. Abstract and Introduction last paragraphs.
2. Contributions paragraph.
3. Method overview and methodology figure.
4. Experiment setup.
5. Main result table.
6. Ablation and analysis.
7. Limitation, discussion, and conclusion.

## Experiment Extraction

For each important experiment, extract and explain in Chinese:

```text
实验类型：主实验 / 消融实验 / 泛化迁移 / 成本分析 / 回归分析 / 其它
实验想回答的问题：
Benchmark / dataset（基准或数据集）：
Baseline（对比方法）：
Metric（指标）：
Main result（核心结果）：
中文解释：
这个实验实际证明了什么：
这个实验还不能证明什么：
```

## Gap-Oriented Questions

Use these questions to produce useful gap notes:

- 论文只证明 final performance 变好，还是解释了为什么变好？
- 有没有把 improvement 分解到 component、diagnosis、patch、validation 或 data choice？
- 有没有控制 search budget、feedback reuse、benchmark overfitting？
- 有没有 held-out split 或 cross-task transfer？
- 有没有检查 regression？
- 有没有依赖 human/oracle signal，真实自动化时是否仍成立？
