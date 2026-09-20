# 工作流 W2：受证据约束的逐节写作

> 生成模式核心。把 PAPER_PLAN + 证据写成可编译的 LaTeX，绝不过度声称、绝不编造。

## 写作纪律（CONFIDENT PROSE, HONEST LIMITS）

1. **声明与证据对齐**：每个 claim 的措辞必须与证据的实际范围/模态匹配。声称「improves 15%」必须有 `results/` 里 12.8%~17% 范围的数据支撑（允许标准舍入）
2. **不升级声明**：证据只支持「suggest/indicate」就不要写「prove/demonstrate」
3. **真实数字**：数字必须来自证据文件，不是从记忆或推断生成
4. **诚实限制**：泛化性不足就写明 scope；真实局限写进 Limitations，不写空泛免责
5. **缺数据用占位**：对 GAP_REPORT 里的 missing 槽位，写 `<!-- DATA_NEEDED: GAP_S4_ABLATION — 需补充消融实验 -->`，绝不虚构数字
6. **按写法卡措辞**：按 W1 核心 claim 写法卡写——张力真实、贡献增量去掉方法名仍可说清、比较口径明确、适用条件不省略（模块12 七项做法写入时生效）

## 分节写作顺序

建议按依赖顺序，避免写废：

1. **方法 (Method)** — 最确定，先写（也最容易被复现审查）
2. **实验 (Experiments)** — 用证据文件填充
3. **相关工作 (Related Work)** — 真实引用（用 fetch_bib.py）
4. **引言 (Introduction)** — 从宽到窄漏斗，front-load contribution
5. **摘要 (Abstract)** — 最后写，浓缩核心
6. **讨论/结论 (Discussion/Conclusion)** — 诚实 scope（局限集中在 Discussion/Limitations，结论只强化记忆点）

## 写作质量 5-Pass（每节写完后跑）

- **Pass 1 Clutter**：删 `due to the fact that` → `because`、`it is worth noting that` → 删除
- **Pass 2 Active**：被动转主动（`It was observed` → `We observed`）；方法/既定事实处被动可保留
- **Pass 3 Architecture**：>40 词长句拆分；主题句先行；句子开头多样化
- **Pass 4 Banana Rule**：同一概念全文用同一术语，不玩同义替换（obese group 不许变 heavier group）；缩写首次定义
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
