# 模块 5：审稿预检（Pre-Review Audit）

> 增强来源：nature-paper-reviewer（Nature 审稿视角）+ scicomp-research-skills（对抗性审稿 + 声明-证据对齐）

**触发关键词**：审稿、挑毛病、投稿前、audit、review、reviewer、检查、预审、revise、revision

## 0. 审稿证据阶段（v3.3，先取证再评审）

> 来源：ScholarPeer（arXiv:2601.22638）的多智能体审稿框架。论文在 ~1,786 篇 ICLR
> 2020–2025 投稿上报告：去掉 Q&A 引擎胜率 -26%，去掉 baseline scout -9%，去掉 summary -10%。
> 这里只迁移机制，不迁移其 headline 数字。

**默认深度审稿先跑本阶段；快速语言/格式检查可跳过，但报告必须标 `review_mode: quick`。**

| 产物 | 作用 | 最低要求 |
|---|---|---|
| `EVIDENCE_FACTS.md` | 论文事实表 | claims / method / evidence / datasets / metrics 五项齐全 |
| `DOMAIN_NARRATIVE.md` | 领域演进叙事 | 300–400 词：演进弧 + open problems + significance criteria |
| `BASELINE_GAP.md` | 漏引 baseline/dataset | 每条含 name / reference / reason / compared 状态 |
| `CLAIM_INTERROGATION.md` | 逐 claim 审问日志 | 每个 major claim ≥1 个 novelty Q + 1 个 soundness Q，附证据 |

**四条硬规则**：
1. 所有 novelty 检索限定 `cutoff_date`（论文首次公开/投稿日期）；不得用发表后的工作判断当时新颖性。
2. 来源白名单：顶会/顶刊 + arXiv；每条外部证据必须有 URL/DOI/arXiv ID，搜不到写 `not_found`。
3. 每条 Critical/Major 必须能指回四份产物的具体行/引文；指不回 → 降级为“待核实”。
4. 不把“我没搜到”写成“不存在”；区分 `not_found` 与 `no_prior_art`。

完整流程、prompt 模板、JSON schema 与预算（quick/standard/deep）见
**[module-5-evidence.md](module-5-evidence.md)**。

## 工作流

0. **先跑 §0 证据阶段**（深度审稿默认）：确定 `cutoff_date` → 事实表 → 领域叙事 →
   漏引 baseline → 逐 claim Q&A；四份产物落盘后再进入评审。
1. 从五个视角独立审读论文：

   - **方法学审稿人**：研究设计、统计严谨性、可重复性
   - **领域审稿人**：文献覆盖、理论框架、相关工作对比
   - **批判审稿人**：逻辑谬误、过度声称、证据链薄弱处
   - **语言审稿人**：拼写错误、语法问题、术语不一致
   - 🆕 **Nature 审稿人**（吸收 nature-paper-reviewer）：新颖性、广泛影响、数据可及性

2. 🆕 **对抗性自审**（吸收 scicomp-research-skills）：
   - 假装你是论文的竞争对手，找出你可以攻击的 3 个最薄弱点
   - 针对每个薄弱点，提出如果由你来审稿会写什么 reject 理由

3. 🆕 **声明-证据映射**（吸收 scicomp）：
   - 列出论文中所有 major claim
   - 为每个 claim 标注支撑证据（数据/引用/推理）
   - 标记无证据支持的 bare claim → Critical

4. 合成审稿意见 → 生成 Red Flag 清单 + 修改优先级

## 🆕 Nature 审稿人 5 大关注点

| 维度 | 评估问题 | 风险等级 |
|------|---------|---------|
| **新颖性** | 这项工作是否为领域带来实质新见解？还是 incremental？ | Critical |
| **广泛影响** | 是否会引起该期刊广泛读者群的兴趣？还是太窄？ | Critical |
| **方法严谨性** | 实验设计和统计方法是否无懈可击？ | Major |
| **数据可及性** | 数据和代码是否可用？有无 reproducibility 承诺？ | Major |
| **写作质量** | 非领域专家能否理解核心信息？ | Minor-Major |

## 🆕 声明-证据对齐检查

对论文中的每个 major claim 执行：

```
Claim: "Our method outperforms all existing approaches"
  ├── Evidence: Table 1 中 Ours vs 3 baselines ✓
  ├── Evidence: 缺失 SOTA baseline X 的比较 ✗ → [Critical]
  └── 建议：添加 baseline X 对比，或弱化 claim 为 "competitive with state-of-the-art"

Claim: "This is the first work to..."
  ├── Evidence: 文献调研表明确实首创？ ✓/✗
  └── 警告：first claim 极易被审稿人质疑，建议改为 "To our knowledge, this is the first..."
```

## 🆕 对抗性自审方法

### Step 1: 识别致命弱点
作为"论文杀手"审稿人，快速找出：
1. Experimental setup 有什么漏洞？
2. 哪个 claim 最 overclaiming？
3. 哪个结论没有数据支撑？
4. 哪个 comparison 不公平？
5. Related work 遗漏了哪些关键工作？

### Step 2: 写 reject 理由
为每个弱点写出如果被 reject 的 1-2 句理由。这能帮你预见审稿人的核心攻击点。

### Step 3: 修复优先级
- Critical：可能导致 reject 的问题 → 必须在投稿前修复
- Major：会引发 major revision → 尽量修复或准备 rebuttal
- Minor：minor revision 级别 → 可以先行 mark
- Suggestion：优化建议 → 酌情处理

## 审稿预检清单

### 结构层面
- [ ] 摘要是否独立完整地传达了核心贡献？
- [ ] 引言是否清晰说明了 motivation 和 gap？
- [ ] 每段的主题句是否能串联成连贯叙述？
- [ ] 论文末尾是否有简洁有力的 conclusion？

### 方法层面
- [ ] 方法描述是否足够详细让他人复现？
- [ ] core 机制是否按注册表逐槽展开？"小体量高复杂度"机制是否被压成一句？（[ledgers.md](ledgers.md) §1）
- [ ] 基线选择是否合理且覆盖 SOTA？（对照 `BASELINE_GAP.md`，不是凭记忆）
- [ ] novelty 判断是否限定在 `cutoff_date` 之前？（对照 `CLAIM_INTERROGATION.md`）
- [ ] 超参数设置是否说明清楚？
- [ ] 实验是否有足够的 ablation study？

### 表达层面
- [ ] 是否有 overclaiming？（批量搜索 `first` `novel` `state-of-the-art`）
- [ ] 图表是否自明（不看正文也能理解）？
- [ ] 图内文字与正文/证据/术语账本一致？（矢量源抽字 diff；位图人工读图）
- [ ] 术语是否全文一致？
- [ ] 引用格式是否统一？

### 🆕 数据/代码（Nature 标准）
- [ ] 是否声明了数据和代码的可用性？
- [ ] 是否有 reproducibility checklist？
- [ ] 补充材料是否组织良好？

## 输出格式

```
## 审稿证据阶段（深度审稿必填）
- cutoff_date: YYYY-MM-DD
- EVIDENCE_FACTS.md: 存在 / 缺失
- DOMAIN_NARRATIVE.md: 存在 / 缺失
- BASELINE_GAP.md: 存在 / 缺失（漏引 N 条）
- CLAIM_INTERROGATION.md: 存在 / 缺失（覆盖 M/N 个 major claim）

## 审稿预检报告

### 🚨 Red Flag 清单
| # | 问题 | 位置 | 严重程度 | 修改建议 |
|---|------|------|---------|---------|
| 1 | Bare claim 无证据 | §3.2 | 🔴 Critical | 补充实验数据 |
| 2 | Baseline 遗漏 | §4.1 | 🟡 Major | 添加 SOTA 对比 |

### 📊 声明-证据映射
| Claim | 证据 | 状态 |
|-------|------|------|
| Claim 1 | Table 1 | ✅ 充分 |
| Claim 2 | 无 | ❌ 缺失 |

### 🎯 对抗性自审
**最弱 3 点**：
1. [弱点描述] → 可能被 reject 的理由
2. ...
3. ...

### 📝 分审稿人意见
#### 方法学审稿人
- [ ] ...
#### Nature 审稿人
- [ ] 新颖性评估：[新颖/增量]
- [ ] 广泛影响评估：[高/中/低]
```

## 🆕 数值 Claim 审计（v3.2，论文↔证据核对）

目的：每个数字、比较、范围声明都能追溯回原始结果文件。**九类典型数据错误**：

| # | 失败模式 | 例子 | 检测 |
|---|---------|------|------|
| 1 | **数值夸大** | 论文 85.3%，原始 84.7% | 只允许标准舍入到显示精度 |
| 2 | **择优 seed** | 报 5 seed 最优 90.2%，均值 87.1% | 检查是否注明 average/best |
| 3 | **配置不一致** | A vs B 比较但超参/数据不同 | 核对 config |
| 4 | **聚合错误** | 声称 5 seed 平均实际 3 次运行 | 数原始运行数 |
| 5 | **差值错误** | 声称提升 15% 实际 (85.3-73.1)/73.1=16.7% | 重算相对提升 |
| 6 | **图表不符** | caption 与图/表内容不一致 | 逐 caption 核对 |
| 7 | **范围夸大** | consistently outperforms 只测 2 数据集 | 措辞 vs 评估范围 |
| 8 | **图内文字失配**（v3.2） | 图上标「≤1 次」但证据为「≤12 轮」；图内用词未随术语账本更新 | 图内文字 ↔ 正文/caption/证据/账本 逐条核对 |
| 9 | **自由参数敏感性缺失**（v3.2） | 指标含 λ 但只报单点、无翻转点 | 要求敏感性/翻转点，否则限缩到正式口径 |

流程：列全部定量声明（**含图内文字**）→ 逐条追溯结果文件 → 判定 exact_match/rounding_ok/mismatch → 产出 `CLAIM_AUDIT.md`。
**一致性审计（v3.2）**：机制覆盖 / 图文码 / 术语漂移 / 设计-实现差异 / 自由参数敏感性，见 [workflow-W5-audit.md](workflow-W5-audit.md) §C 与 [ledgers.md](ledgers.md)。
**独立性**：若可用外部跨模型审查者，用无上下文新线程只读「论文+原始结果」核对，避免执行者自我确认偏误；否则以「假装刚接手只看证据」的心态自审。

## 🆕 编辑白名单（v3，修改边界约束）

审稿修订/换投/生成修订时，用 YAML 限制可改路径与操作（禁新增 `\cite`、定理、数字，禁删已有引用/定理），拒绝项记录日志。**完整协议见 [edit-whitelist.md](edit-whitelist.md)。**

## 🆕 跨模型独立性原则（v3）

- **自审 ≠ 终审**：执行者自审存在自证盲区
- 数值、引用、证明类的**质量判决**建议路由给另一个模型家族做独立核对
- 独立审查者只读「论文 + 原始证据」，不接受执行者的摘要/解读
- 审查结论以 JSON/结构化工件留痕，可追溯

## 与相关模块协作

- → 模块5.0（证据阶段）：深度审稿先跑 [module-5-evidence.md](module-5-evidence.md)
- → 模块9（引用验证）：引用问题作为审稿预检的一部分
- → 模块2（段落润色）：发现写作问题后调用润色
- → 模块13（防御性写作阻止）：本模块找问题，模块13 防自伤（交稿前 8 问自查，与对抗性自审互补）
- → [journal-styles/nature-cns.md](journal-styles/nature-cns.md)：Nature 审稿视角参考