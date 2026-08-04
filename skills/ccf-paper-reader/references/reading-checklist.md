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
5. 如果方法有结构化中间产物，最小 JSON-style data flow 长什么样？字段名是否在 JSON 内用括号自带中文解释？JSON 后是否说明每组字段由谁产生、输入给谁、输出什么、下游怎么用？
6. 它和最接近工作相比，真正变化在哪里？用通俗中文解释差别。
7. 它的主实验验证了什么 claim？主实验和消融实验要分开解释，并解释关键指标和数字。
8. 它有没有 ablation（消融）、generalization（泛化）、robustness（鲁棒性）、cost（成本）、regression（回归）或 budget control（预算控制）？
9. 它没有验证什么？
10. 对用户当前项目的 gap 或 idea 有什么启发？

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
指标怎么理解：怎么算，越高/越低代表什么，分母/分子是什么：
Main result（核心结果）：
数字怎么理解：和 baseline/random 比如何，直观含义是什么：
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
- 关键数值有没有解释清楚：指标含义、比较对象、直观意义、结论边界？
- 还没解决的问题有没有聚焦：是否围绕用户方向收束成 2-4 个核心 gap，并用论文证据数字或实验现象支撑？
- JSON-style 示例有没有配套“字段流向/简化流程图”：字段组之间的先后关系、模块输入输出、下游使用方式是否讲清楚？
