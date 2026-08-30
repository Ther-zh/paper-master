# 模块9：引用验证与格式化

> 来源吸收：citation-verifier（42 installs，引用类最高）+ citation-finder（32 installs）+ citation-formatter（32 installs）+ nature-citation（832 downloads）

## 触发关键词
引用检查、引用验证、citation check、DOI 验证、参考文献、bibliography、BibTeX、引用格式、citation format、引用是否真实、引用格式化

## 工作流

### 阶段0：🆕 真实 BibTeX 获取（v3，杜绝幻觉引用）

需要新引用条目时，**不要凭记忆生成 BibTeX**——用脚本从 DBLP/CrossRef 拉取 publisher 验证过的真实条目：

```bash
# 搜索 DBLP（列出候选）
python scripts/fetch_bib.py search "attention is all you need" --author "Vaswani"

# 获取第一条命中的真实 BibTeX（--key 指定 citation key）
python scripts/fetch_bib.py fetch "attention is all you need" --author "Vaswani" --key vaswani2017attention

# 按 DOI 获取（适用于 arXiv 预印本，arXiv DOI = 10.48550/arXiv.{id}）
python scripts/fetch_bib.py doi 10.48550/arXiv.1706.03762
```

回退链：**DBLP（质量最高）→ CrossRef/DOI（兜底）→ `% [VERIFY]` 标记（最后一招）**。
拉不到就标 `[VERIFY]`，**绝不编造**。LLM 记忆生成的 BibTeX 常幻觉 venue/页码/共同作者。

获取后可跑卫生校验：

```bash
# 检查死条目 + year/venue/author 一致性（只读，不改文件）
python scripts/fetch_bib.py clean main.tex references.bib
```

输出 `DEAD ENTRIES`（未引用条目，应删）、`MISMATCH`（元数据与权威源不符）、`VERIFY`（无法验证）。

### 阶段1：引用完整性检查

#### 1.1 引用存在性验证
对论文中每个 `\cite{}` 执行：
- [ ] 引用条目在 .bib 文件中存在？
- [ ] .bib 条目包含所有必填字段？（author, title, year, journal/booktitle, DOI）
- [ ] 无反斜杠转义错误？

#### 1.2 DOI 真实性验证
对每个有 DOI 的引用：
- [ ] DOI 格式正确？（`10.xxxx/xxxx`）
- [ ] DOI 可解析？（通过 doi.org/api 验证）
- [ ] 作者/标题/年份与 .bib 一致？
- [ ] 会议/期刊名称与 .bib 一致？

#### 1.3 引用一致性检查
- [ ] 同一论文在正文中引用格式一致？（如作者-年份 vs 编号）
- [ ] 同一作者的引用前后名字拼写一致？
- [ ] 会议/期刊缩写是否统一？

### 阶段2：引用真实性评估

#### 2.1 高风险信号
- 通过搜索引擎/学术数据库无法找到该论文
- DOI 无法解析或指向不同论文
- 标题看似合理但与知名工作过于相似
- 作者列表不可能（如全部为知名作者但从未合作过）
- 期刊/会议在那一年不存在

#### 2.2 可疑引用处理
```
[⚠️ 可疑引用] Liu et al., 2023
  问题：DOI 10.1000/xxxxx 无法解析
  建议：手动确认该引用是否真实存在
  操作：标记为待验证，不直接删除
```

### 阶段3：引用格式适配

#### 3.1 格式检测
自动检测论文使用的引用格式：
- `[1]` 编号式（IEEE, ACM）
- `(Author, Year)` 作者-年份式（APA, Harvard）
- `[ABC23]` 缩略编号式（部分 CS 会议）
- 上标编号式（部分中文期刊）

#### 3.2 格式修复
- [ ] 所有引用格式统一？
- [ ] BibTeX entry type 与引用用途匹配？（`@article` vs `@inproceedings` vs `@misc`）
- [ ] 标题中不应大写的词是否正确？（LaTeX `{}` 保护）
- [ ] 作者名的 "and" 分隔是否正确？

#### 3.3 跨期刊格式转换
支持常见格式转换：
- IEEE → APA
- ACM → Harvard
- 编号式 → 作者-年份式
- Nature → arXiv

### 阶段4：引用合理性检查

- [ ] **自引比例**：自引是否过多？（>30% 需标注）
- [ ] **时效性**：近3年引用占比？（推荐 >40%）
- [ ] **覆盖性**：是否遗漏了该领域的经典/必引工作？
- [ ] **挂名引用**：是否存在与内容无关的引用？
- [ ] **二手引用**：是否引用了二手来源而非原始论文？

### 阶段5：BibTeX 文件维护

- [ ] 所有 .bib 条目按字母顺序排列？
- [ ] 所有条目使用统一的 citation key 格式？（推荐 `authorYYYYkeyword`）
- [ ] 清理未使用的 .bib 条目？（可用 `python scripts/fetch_bib.py clean` 检测 DEAD ENTRIES）
- [ ] 补全缺失字段的条目？

### 🆕 阶段6：引用上下文适切性审计（v3，第三轴）

最危险的引用问题不是明显造假，而是「**真实论文用错语境**」——引用真实存在，但它并不支撑你当前的 claim。

对每个 `\cite{}`：
1. 提取引用所在句子的完整上下文（前后 ≥1 句）
2. 判断该 claim 是否真是被引论文所建立的：
   - **SUPPORTS**：被引论文确实支撑该 claim
   - **WEAK**：部分相关但支撑不足
   - **WRONG**：语境错误（被引论文实际持相反观点）
3. 判定 `KEEP / FIX / REPLACE / REMOVE`
   - REPLACE：找真正支撑该 claim 的另一篇论文
   - REMOVE：幻觉/无法支撑

**高危信号**：引用 Self-Refine 去支撑「self-feedback 产生相关误差」（实际论文主张相反）、把 arXiv 预印本当正式 venue、年份漂移、phantom DOI。

> 对可疑条目，用 `scripts/fetch_bib.py` 的 DBLP/CrossRef 链辅助核实存在性与元数据，上下文判断需要人工/跨模型核对。

## 输出格式

```
## 引用验证报告

### 统计数据
- 总引用数：X
- 通过验证：X
- 需要修正：X（列出具体问题和建议）
- 可疑引用：X（标注风险等级）

### 详细问题列表
| 引用 | 问题类型 | 严重程度 | 修正建议 |
|------|---------|---------|---------|
| \cite{smith2020} | DOI 不可解析 | ⚠️ 高 | 手动确认 |

### 格式修正建议
- 引用格式不一致：3处
- 建议统一为：[格式]

### 引用合理性评估
- 自引比例：X%
- 近3年引用：X%
- 缺失推荐引用：Y
```

## 与相关模块协作

- → 模块5（审稿预检）：引用问题作为审稿预检的一部分
- → 模块8（文献调研）：验证调研阶段收集的文献