# Paper Reading Note Template

Use Chinese as the main language. Keep necessary English names and terms. For important English phrases, add a short Chinese gloss on first use, such as `change manifest`（变更清单）. Avoid English-heavy section titles and tables unless the English term is the paper's method name, metric, dataset, or benchmark. Do not output paper-internal figure metadata such as `Figure:`, `Page:`, or `Caption:` in the final note.

```markdown
# <Paper Title>

## 0. 元信息

- Title:
- Authors:
- Year / Venue / Status:
- Link:
- Code / Project:
- Reading mode: quick / standard
- Evidence status: public paper / user-provided PDF / partial sections

## 1. 一句话总结

用 1-2 句中文说明这篇论文解决什么问题、用什么核心办法、主要证明了什么。

## 2. Problem：现有问题是什么

- 论文关注的任务/场景：
- 现有方法的不足：
- 为什么这个问题重要：
- 为什么这个问题难：

## 3. Gap：作者认为的空缺

- 作者明确指出的 gap：
- 从论文实验或设定中能看出的隐含 gap：
- 这个 gap 是否和用户当前方向相关：

## 4. Insight：核心洞察

- 核心 insight：
- 为什么这个 insight 能解决 gap：
- 这个 insight 是否新颖：论文声称 / 我的推断 / 需要进一步查证

## 5. Method & Figure：方法和图怎么讲

- 输入：
- 输出：
- 方法图：直接贴图，不列 Figure/Page/Caption 元信息；如需要，只写一句简短图源。
- 先用一句话讲方法：
- 图中模块通俗解释：
- 训练/搜索/推理流程：
- 这张图和论文核心 insight 的关系：
- 哪些只是工程支撑，哪些是真正的方法贡献：
- 和 closest baseline 的主要差别：

## 6. Introduction 翻译与理解

### 6.1 忠实翻译

按段落翻译 Introduction 中最关键的动机、gap、contribution 段落。不要机械翻译全文，除非用户要求。

### 6.2 中文理解

- 作者如何讲 problem：
- 作者如何制造 gap：
- 作者如何引出 method：
- 这套 narrative 对我们写作有什么可借鉴：

## 7. Experiments：实验怎么做

### 7.1 实验设置

- 任务/数据集：
- Baseline（对比方法）：
- Metric（指标）：
- 指标怎么理解：这个指标怎么算，越高/越低代表什么：
- 预算/成本/运行设置：

### 7.2 主实验：它到底有没有变强

- 实验想回答的问题：
- 怎么比：
- 关键结果：
- 指标和数字解释：
- 中文解释：
- 这个实验能证明什么：
- 这个实验还不能证明什么：

### 7.3 消融实验：到底是哪部分有用

- 消融了哪些组件：
- 关键结果：
- 指标和数字解释：
- 中文解释：
- 说明了什么：
- 仍然不清楚什么：

### 7.4 泛化、迁移、成本和回归

- 泛化/迁移实验：
- 成本或 token 分析：
- 回归或负面结果：
- 指标和数字解释：
- 中文解释：
- 对我们研究 gap 的启发：

## 8. Analysis：作者额外分析了什么

- Ablation 检查了什么组件：
- 结果说明什么：
- 有没有 robustness/generalization/cost/regression 分析：
- 缺失的关键实验：

## 9. Limitations：作者承认的限制

- 作者明确写出的 limitation：
- 实验范围限制：
- 方法假设：
- 可能失败场景：

## 10. What Remains Unsolved：还没解决什么

对每个未解决问题，尽量写四点：缺什么验证；为什么论文已有实验还不能证明；这件事为什么重要；可以怎么补实验或形成 idea。

- 未解决问题 1：
  - 缺什么验证：
  - 为什么现有实验不够：
  - 为什么重要：
  - 可能怎么做：
- 未解决问题 2：
  - 缺什么验证：
  - 为什么现有实验不够：
  - 为什么重要：
  - 可能怎么做：
- 可能的 confounder（混淆因素）：
- 和当前项目的关系：

## 11. 对我们方向的启发

- 可以借鉴的 framing：
- 可以借鉴的方法模块：
- 可以攻击或补充的 evaluation gap：
- 可能形成的 idea：

## 12. Action Items

- Update gap map: yes / no
- Update idea bank: yes / no
- Need literature search: yes / no
- Need experiment design: yes / no
- Follow-up papers:
```
