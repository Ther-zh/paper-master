# Nature/CNS 期刊风格规则库

> 来源吸收：nature-style-writer（855 downloads，Nature风格改写）+ nature-figure（975 downloads，出版级图表）+ nature-paper-reviewer（Nature审稿视角）

## Nature 系列期刊要求

| 期刊 | 缩写 | 文章类型 | 字数限制 | 图表限制 |
|------|------|---------|---------|---------|
| Nature | - | Article / Letter | ~3,000（正文） | 3-4 figures |
| Nature Methods | NMETH | Article | ~3,000 | 4-6 figures |
| Nature Machine Intelligence | NMI | Article | ~4,000 | 4-6 figures |
| Nature Communications | NatComm | Article | ~5,000 | 6-10 figures |
| Nature Biomedical Engineering | NBME | Article | ~3,500 | 4-6 figures |
| Science | - | Research Article | ~4,500 | 4-5 figures |
| Cell | - | Article | ~ 可变 | 6-7 figures |
| PNAS | - | Research Article | ~5,000 | 5-6 figures |

## Nature 写作风格指南

### 核心原则

1. **简洁至上**：每句话都应有信息量，无赘词
2. **可及性**：Nature 读者横跨多学科，避免过度领域化术语
3. **叙事性**：将研究方法嵌入一个引人入胜的故事框架
4. **精确性**：数据和主张必须有精确表述，杜绝夸大

### Nature 风格 7-Pass 编辑法（吸收自 nature-style-writer）

```
Pass 1: Diagnose — 整体评估：结构、论证链、读者友好度
Pass 2: Grammar — 语法修正：主谓一致、时态、冠词
Pass 3: Passive→Active — 被动态转主动态："We observed" 比 "It was observed" 强
Pass 4: Nominalization — 名词化还原："We analyzed" 更好于 "We performed an analysis"
Pass 5: Shorten — 精简：删除冗余短语，每句不超过 25-30 词
Pass 6: Sharpen — 锐化：Claim 短语更精确、限定词更恰当（多用 "suggest/indicate" 替代 "prove/demonstrate"）
Pass 7: Transitions — 段落间过渡：确保逻辑流顺畅，每段首句与上段尾句衔接
```

### 常见 Nature 编辑偏好

#### 主动语态 > 被动语态
```
❌ "The experiment was performed by the team."
✓  "We performed the experiment."
```

#### 减少弱化动词
```
❌ "We carried out an investigation of..."
✓  "We investigated..."
❌ "We made a comparison between..."
✓  "We compared..."
```

#### 精确限定词
```
❌ "Our results prove that..."       → "Our results demonstrate that..."
❌ "This is the first..."            → "To our knowledge, this is the first..."（谨慎使用）
❌ "X causes Y"                      → "X is associated with Y"（除非有因果证据）
```

### 句式长度控制

- **理想**：20-25 词/句
- **上限**：35 词/句
- **混合**：短句（10-15词）+ 长句（25-30词）交替，保持节奏

### Nature 版块写作模板

#### 摘要（Abstract）
```
[1-2句] 背景：为什么这个问题重要
[1-2句] 方法：我们做了什么（概括性）
[2-3句] 发现：我们发现了什么
[1句]  意义：为什么这个发现重要
```
- Nature 摘要 ~150 词
- 不包含引用和缩写（除非先定义）

#### 引言（Introduction）
```
[段落1] 大背景 + 核心问题
[段落2] 已有工作 + 局限性
[段落3] 本文方法简述 + 主要发现预告
```
- 目标：让非领域读者理解为什么这个研究重要
- 避免深奥的技术细节

## Nature 出版级图表规范（吸收自 nature-figure）

### 图表设计原则

1. **自明性**：图无需读正文也能理解
2. **一致性**：同类型数据用相同的颜色/形状编码
3. **可及性**：考虑色盲友好配色
4. **出版质量**：分辨率 ≥300 dpi，矢量图优先

### 图表类型与参数

| 图类型 | 推荐工具 | 输出格式 | DPI |
|--------|---------|---------|-----|
| 折线/柱状/散点 | matplotlib / ggplot2 | PDF/SVG | 矢量 |
| 热图 | matplotlib seaborn | PDF | 矢量 |
| 示意图/流程图 | draw.io / TikZ | PDF | 矢量 |
| 照片/显微图像 | ImageJ / Photoshop | TIFF/PNG | 300-600 |
| 统计图表 | seaborn / ggplot2 | PDF | 矢量 |

### matplotlib 出版级参数

```python
import matplotlib.pyplot as plt

# Nature 标准配置
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica'],
    'font.size': 7,
    'axes.labelsize': 8,
    'axes.titlesize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'lines.linewidth': 1.0,
    'axes.linewidth': 0.5,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
})
```

### 配色方案（色盲友好）

**Nature 推荐配色**：
- 定性数据：`['#E64B35', '#4DBBD5', '#00A087', '#3C5488', '#F39B7F', '#8491B4']`
- 连续数据：`viridis` / `cividis`（perceptually uniform）
- 发散数据：`RdBu_r` / `coolwarm`

**禁止使用**：
- 纯红-纯绿组合（红绿色盲最常见）
- 彩虹配色（jet/rainbow）
- 低对比度的浅色组合

### 图表标题与注释

- 标题格式：`**Figure X |** Title in sentence case.`
- 子图标注：(a) (b) (c) 小写字母，左下角
- 坐标轴标签：带单位，如 `Time (s)` / `Accuracy (%)`
- 误差线：明确标注是 SEM / SD / CI
- 统计显著性：`*P < 0.05, **P < 0.01, ***P < 0.001, n.s. = not significant`

## Nature 审稿视角（吸收自 nature-paper-reviewer）

### Nature 审稿人最关心的 5 个问题

1. **新颖性**：这项工作是否为领域带来实质新见解？
2. **广泛影响**：这项工作是否会引起 Nature 广泛读者群的兴趣？
3. **方法严谨性**：实验设计和统计方法是否无懈可击？
4. **数据可及性**：数据和代码是否可用？
5. **写作质量**：非领域专家能否理解核心信息？

### 投稿前自审清单

- [ ] 摘要能在 2 分钟内让 Nature 编辑理解你的贡献？
- [ ] 第一段是否解释了"为什么现在"这个研究重要？
- [ ] 图表是否自明（不看方法也能理解）？
- [ ] 方法部分是否足够详细让他人复现？
- [ ] 所有 claim 是否有数据支撑？无 overclaim？
- [ ] 参考文献是否覆盖了关键竞争者的最新工作？
- [ ] 补充材料是否组织良好？