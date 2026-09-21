# 工作流 W2：受证据约束的逐节写作

> 生成模式核心。把 PAPER_PLAN + 证据写成可编译的 LaTeX，绝不过度声称、绝不编造。

## 写作纪律（CONFIDENT PROSE, HONEST LIMITS）

1. **声明与证据对齐**：每个 claim 的措辞必须与证据的实际范围/模态匹配。声称「improves 15%」必须有 `results/` 里 12.8%~17% 范围的数据支撑（允许标准舍入）
2. **不升级声明**：证据只支持「suggest/indicate」就不要写「prove/demonstrate」
3. **真实数字**：数字必须来自证据文件，不是从记忆或推断生成
4. **诚实限制**：泛化性不足就写明 scope；真实局限写进 Limitations，不写空泛免责
5. **缺数据用占位**：对 GAP_REPORT 里的 missing 槽位，写 `<!-- DATA_NEEDED: GAP_S4_ABLATION — 需补充消融实验 -->`，绝不虚构数字
6. **按写法卡措辞**：按 W1 核心 claim 写法卡写——张力真实、贡献增量去掉方法名仍可说清、比较口径明确、适用条件不省略（模块12 七项做法写入时生效）
7. **core 机制逐槽展开（v3.2）**：按 W1 机制注册表六槽展开卡写——动机 / 定义 / 触发与落点 /
   输入产物与作用域 / 关键参数与判据 + 替代方案 / 验证与消融角色；禁止"采用 X 算法求解"式
   一句带过。supporting 可一段，baseline 可表内一句（简写合法）。
8. **账本取词（v3.2）**：正文、图注与图内文字用词直接取自术语账本（**复制不重打**）；
   提及实现状态的句子与设计-实现台账一致——`unknown` 只能写"设计为…"，不得写成"we implement/我们实现了"。
9. **自由参数（v3.2）**：涉及自由参数/阈值/权重/选取规则的比较 claim，按 W1 写法卡给
   敏感性或翻转点；给不出就在正文限缩措辞（不得延伸到正式口径之外）。

## 分节写作顺序

建议按依赖顺序，避免写废：

1. **方法 (Method)** — 最确定，先写（也最容易被复现审查）；写作前先过机制注册表：
   core 机制按六槽展开，supporting 一段，baseline 表内一句
2. **实验 (Experiments)** — 用证据文件填充
3. **相关工作 (Related Work)** — 真实引用（用 fetch_bib.py）
4. **引言 (Introduction)** — 从宽到窄漏斗，front-load contribution
5. **摘要 (Abstract)** — 最后写，浓缩核心
6. **讨论/结论 (Discussion/Conclusion)** — 诚实 scope（局限集中在 Discussion/Limitations，结论只强化记忆点）

## 写作质量 5-Pass（每节写完后跑）

- **Pass 1 Clutter**：删 `due to the fact that` → `because`、`it is worth noting that` → 删除
- **Pass 2 Active**：被动转主动（`It was observed` → `We observed`）；方法/既定事实处被动可保留
- **Pass 3 Architecture**：>40 词长句拆分；主题句先行；句子开头多样化
- **Pass 4 Banana Rule**：同一概念全文用同一术语，不玩同义替换（obese group 不许变 heavier group）；缩写首次定义；判据来源 = W1 术语账本（replace 词不得出现、define_once 词首现定义，图注/图内文字同表）
- **Pass 5 Numeric/Citation Integrity**：摘要的 N 与 Table 1 一致；百分数与原始数据一致；图与表一致

## 引用纪律

- 只用 `scripts/fetch_bib.py` 从 DBLP/CrossRef 拉取真实 BibTeX
- 拉不到 → `% [VERIFY]` 标记，绝不手动编
- 只用正文实际引用到的条目写进 `references.bib`（杜绝 bloat）
- 优先已发表 venue 版本，而非 arXiv 预印本（若已出版）

## 反 AI 痕迹（同步）

写作时即规避 AI 高频词（delve、pivotal、landscape、crucial、notably、Moreover/Furthermore 堆叠等），减少后续去 AI 工作量。

## 反防御性写作（同步，→ 模块13 写入时生效）

- 摘要/引言按发布会开场四件事：重要问题 → 现有缺口 → 独特思路 → 最强结果与意义（对照 W1 叙事策略卡的故事线写）
- 每个实验一个论证职责（对照 W1 实验职责表）；不写「先做 A、又试 B、C 失败」的流水账
- 写作时即规避自我削弱表达（遗憾的是 / 仅 / 效果有限 / 仍明显落后）；不占优的结果不说输
- **每节写完跑「写入时 4 问」**（模块13 交稿 8 问的写入版）：
  ① 这句话是否扩大了本文需承担的责任？
  ② 是否把局部现象写成了普遍缺陷？
  ③ 是否按"我们做了什么过程"在展开？
  ④ 段尾/结论是否突然自我否定？
- 与「诚实限制」的分工：真实局限集中在 Limitations 如实写；abstract / intro / conclusion 不主动展开自我否定（模块13 规则 7）

## 输出

```
paper/
├── main.tex
├── sections/
│   ├── 00-abstract.tex
│   ├── 01-introduction.tex
│   ├── 02-related.tex
│   ├── 03-method.tex
│   ├── 04-experiments.tex
│   ├── 05-conclusion.tex
│   └── (理论论文) 06-proofs.tex
└── references.bib
```

## 硬规则

- **不生成作者姓名/邮箱/单位** — 用 `Anonymous Submission` 匿名块
- 写完整节而非大纲；每节一个文件；可编译
- 保存前备份现有 `paper/` 目录，不覆盖破坏

→ 下一阶段: [W4 编译校验](workflow-W4-compile.md)（W3 图表为可选项，见 module-3）
