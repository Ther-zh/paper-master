# 模块 4：期刊适配（Journal Adapt）

> 增强来源：nature-style-writer（Nature 风格库）+ journal-styles/nature-cns.md（期刊风格规则库）

**触发关键词**：适配、风格、目标期刊、AAAI、ICML、NeurIPS、CVPR、IEEE、ACM、Nature、Science、Cell、PNAS、换投、reformat、template

## 工作流（两阶段）

### Phase 1 — 风格分析

1. 用户提供 3-5 篇目标期刊/会议已发表论文（或明确期刊名）
2. 提取各论文的 Style Card（10 维度）：
   - 摘要结构、引言架构、贡献表达、文献综述方式
   - 方法论描述、结果呈现、讨论风格
   - 语言特点、缺失模式、特色亮点
3. 聚合生成目标期刊的 Journal Style Card
4. 🆕 若目标为 Nature/CNS 期刊，自动加载 [journal-styles/nature-cns.md](journal-styles/nature-cns.md)

### Phase 2 — 逐节修改

1. 按 Abstract → Introduction → Related Work → Method → Experiments → Conclusion 顺序
2. 每节输入用户手稿 → 对比 Journal Style Card → 输出修订建议
3. 提供「风格差异报告」：列出与目标期刊不一致之处

---

## 🆕 内置期刊风格规则库

| 期刊/会议 | 风格文件 | 特性 |
|----------|---------|------|
| Nature 系列 | [journal-styles/nature-cns.md](journal-styles/nature-cns.md) | 出版级图表规范、Nature 审稿视角、写作偏好（见模块2 7-Pass） |
| AAAI / ICML / NeurIPS / CVPR / ACM | `../paper-venue-master/references/venue-index.md` | 页数、匿名、模板与相机就绪规则统一在该 skill 核验，本模块不再维护副本 |
| IEEE 期刊/会议 | 🆕 [venue/ieee.md](venue/ieee.md) | 非匿名、参考文献计入页数、`\cite{}` 非 natbib、IEEEtran 模板、IEEEkeywords |

> **注意**：7-Pass 编辑法的完整流程定义在 [模块2](module-2-polish.md) 中。本模块仅引用 Nature 特定的风格差异（如 Pass 6 的保守限定词偏好），执行润色时路由回模块2，避免内容重复。

## 🆕 系统类论文（OSDI/SOSP/ASPLOS/NSDI/EuroSys）

若目标为系统方向会议，采用结构化蓝图：
- **12 页页数分配**：Intro ~1.5、Background/Related ~2、Design ~4、Implementation ~1、Evaluation ~3、Discussion ~0.5
- **写作模式**：
  - *Gap Analysis*：现有系统缺什么 → 我们补什么
  - *Observation-Driven*：从实际观察/痛点出发引出设计
  - *Contribution List*：明确列贡献
  - *Thesis Formula*：`X is better for Y in Z`（Irene Zhang 公式）
- 评价重实证：延迟/吞吐/扩展性，和基线公平对比

---

## 🆕 期刊风格快速对比卡

| 维度 | CS 会议（AAAI/ICML） | Nature/Science | IEEE/ACM |
|------|---------------------|---------------|----------|
| 篇幅 | 8-10 页 | 3-5 页（正文） | 8-12 页 |
| 读者 | 领域专家 | 跨学科科学家 | 领域专家 |
| 摘要 | 150-200 词，结构化 | ~150 词，叙事性 | 150-250 词 |
| 图表 | 4-6 个 | 3-4 个（高信息密度） | 4-8 个 |
| 被动语态 | 可接受 | 不推荐（见模块2 Pass 3） | 可接受 |
| Claim 强度 | "demonstrate" | "suggest/indicate"（保守，见模块2 Pass 6） | "demonstrate/show" |
| 补充材料 | 单独文件 | 独立 SI 文档 | 可选 |

### Nature/CNS 场景专属动作

当目标为 Nature/CNS 时，按以下优先顺序执行：
1. 加载 [journal-styles/nature-cns.md](journal-styles/nature-cns.md) 获取完整风格指南
2. 执行 **段落润色**（→ 路由到模块2）：使用 7-Pass 编辑法，特别关注 Pass 6（用 suggest/indicate 替代 prove/demonstrate）
3. 执行 **LaTeX 检查**（→ 路由到模块3）：应用出版级图表规范
4. 执行 **审稿预检**（→ 路由到模块5）：使用 Nature 审稿人 5 维评估

> 其余模块（模块8-11）与 Nature 稿件通用，无特殊差异。

---

## 换投场景（吸收 paper-master-opt）

当用户请求"换投"时（如从 AAAI 换到 ICML），调整路由顺序：

```
标准顺序：结构策略 → 段落润色 → LaTeX精修 → 去AI痕迹 → 审稿预检 → 期刊适配 → Cover Letter
换投顺序：期刊适配（先分析新目标）→ 段落润色（适配新风格）→ LaTeX精修（调整模板）→ 审稿预检
```

---

## 会议规则与模板（交给 paper-venue-master）

本模块只保留**体裁级**风格规则（CS 工程、ML/CV/NLP、Nature/CNS、IEEE）。具体会议的页数、匿名、模板模式、相机就绪要求不在本模块维护，避免规则过期：

- 会议级规则与模板 → `paper-venue-master`（其 `references/venue-index.md` 给出 109 个会议的官方链接与核验状态）。
- 投稿包与复现清单 → `paper-venue-master/references/submission-checklist.md`。
- 换投时先在新会议模板里验证页数与匿名，再回来做 Phase 1/2 的风格改写。

## 内置领域静态规则

位于 [domain-rules/](domain-rules/)：
- [ml-cv-nlp.md](domain-rules/ml-cv-nlp.md)：ML/CV/NLP 领域术语表、公式排版惯例、评测指标写法
- [cs-engineering.md](domain-rules/cs-engineering.md)：CS 工程类论文风格
- 🆕 [journal-styles/nature-cns.md](journal-styles/nature-cns.md)：Nature/CNS 期刊完整风格指南

## 与相关模块协作

- → 模块1（结构策略）：期刊风格影响结构规划
- → 模块2（段落润色）：按期刊风格执行润色
- → 模块3（LaTeX精修）：期刊模板格式检查
- → 模块9（引用验证）：期刊引用格式验证