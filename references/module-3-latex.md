# 模块 3：LaTeX 精修（LaTeX Polish）

> 增强来源：awesome-latex-skills（172⭐，LaTeX prompt 集合）+ nature-figure（975 downloads，出版级图表规范）

**触发关键词**：LaTeX、编译、格式、图表、排版、latex、compile、figure、table、公式、参考文献、模板、template

## 工作流

1. 读取 `.tex` / `.sty` / `.cls` 文件
2. 分节提取文本内容（使用 parser 逻辑）
3. 按粗→细顺序检查：
   - **编译级**：缺失的 `\end{}`、未定义的引用、错误环境嵌套、包冲突
   - **格式级**：图表标签位置、浮动体参数、公式编号、页边距
   - **样式级**：引用格式、断词、跨页孤行、图表分辨率
4. 输出带位置标注的修改建议

## 🆕 静态体检脚本（v3）

直接用脚本做第一遍体检，覆盖未闭合环境/未定义引用/重复 label/定理一致性/写作残留/匿名泄漏：

```bash
python scripts/check_tex.py paper/
# 或指定文件
python scripts/check_tex.py --files main.tex sections/intro.tex --bib references.bib
```

> 脚本在 paper-master 目录的 `scripts/` 下。有 ERROR 先修完再人工精修。

## 🆕 页数校验（v3）

- **ML 会议**（ICLR=9/NeurIPS=9/ICML=8/AAAI=7）：正文到 Conclusion 结束，参考文献+附录不计
- **IEEE**：参考文献计入总页数（journal 12-14 / conference 5-8）
- **Nature/CNS**：3-5 页正文

```bash
pdftotext main.pdf - | python -c "
import sys
text = sys.stdin.read()
pages = text.split('\f')
for i, page in enumerate(pages):
    if any(w in page for w in ['References', 'Bibliography']):
        print(f'References start on page {i+1}')"
```

超页处理：优先移附录（证明/额外结果）、压缩表格、收紧写作。

## 🆕 定理重述一致性检查（理论论文，v3）

正文声明的定理/命题/引理/推论 ↔ 附录/正文证明块必须一致：
- 量化词、假设、分支（case splits）逐条比对
- 术语漂移检测：`stationary` vs `terminal`、改名后的假设等视为不一致
- 发现差异：加显式 notation bridge 或修正，不静默重命名
- 用 `check_tex.py` 的定理一致性检查项粗查 + 人工细读

> 理论论文若附录只有 sketch 而无完整证明，会在理论型会议被拒。务必核对。

## 安全规则（永不碰的内容）

- `\cite{}`、`\ref{}`、`\label{}` 内部
- 数学环境 `$...$`、`$$...$$`、`\begin{equation}...\end{equation}` 内部
- 已注释的行（以 `%` 开头）
- `\newcommand` / `\renewcommand` 定义本身
- 图表文件的 `\includegraphics` 路径

---

## 一、编译级错误诊断（增强版）

### 1.1 常见编译错误速查表

| 错误信息 | 原因 | 修复 |
|---------|------|------|
| `Undefined control sequence` | 命令拼写错误或包未加载 | 检查命令名 / 添加 `\usepackage` |
| `Missing \endcsname inserted` | `\label` 或 `\ref` 中有特殊字符 | 检查 label 名只含字母数字 |
| `Extra }, or forgotten \endgroup` | 花括号/环境不匹配 | 检查 `\begin{...}` 和 `\end{...}` 配对 |
| `File 'xxx.sty' not found` | 缺失包 | `tlmgr install xxx` 或安装该包 |
| `Overfull \hbox` | 行内容溢出 | 调整断词或用 `\sloppy` |
| `Underfull \hbox` | 行内容过少 | 检查是否有不必要的 `\\` |
| `Citation 'xxx' undefined` | .bib 缺失或未运行 bibtex | 运行 pdflatex → bibtex → pdflatex × 2 |
| `Reference 'xxx' undefined` | .aux 过期 | 重新编译 2 次 |

### 1.2 编译环境检查
- [ ] 是否运行了完整的编译链？（pdflatex/xelatex → bibtex/biber → pdflatex → pdflatex）
- [ ] `.aux` / `.bbl` / `.toc` 等辅助文件是否过期？
- [ ] 包的加载顺序是否合理？（`hyperref` 应最后加载）
- [ ] 是否存在包冲突？（`amsmath` vs `mathtools` 等）

---

## 二、LaTeX 结构规范

### 2.1 文档类检查

```latex
% ✅ 正确
\documentclass[letterpaper,11pt,twocolumn]{article}  % AAAI 风格

% ⚠️ 关注点
% 1. 纸张大小：letterpaper / a4paper 与期刊要求一致
% 2. 字体大小：10pt / 11pt / 12pt
% 3. 双栏/单栏：twocolumn / onecolumn
```

### 2.2 章节/环境嵌套检查
- [ ] `\section{}` → `\subsection{}` → `\subsubsection{}` 层级正确？
- [ ] `\begin{figure}` ... `\end{figure}` 配对完整？
- [ ] `\begin{table}` ... `\end{table}` 配对完整？
- [ ] `\begin{equation}` ... `\end{equation}` 配对完整？
- [ ] 列表环境 `itemize`/`enumerate` 正确闭合？

### 2.3 交叉引用检查
- [ ] 所有 `\label{}` 是否是唯一的？
- [ ] 所有 `\ref{}` / `\cite{}` / `\eqref{}` 是否对应存在的 label/key？
- [ ] 图表引用格式是否统一？（`Figure~\ref{}` vs `Fig.~\ref{}`）

---

## 三、出版级图表规范（吸收 nature-figure + awesome-latex-skills）

### 3.1 图表设计原则
1. **自明性**：图无需读正文也能理解
2. **一致性**：同类型数据用相同颜色/形状编码
3. **可及性**：色盲友好配色
4. **出版质量**：分辨率 ≥300 dpi，矢量图优先

### 3.2 图表文件规范

| 图类型 | 推荐格式 | 导出要求 |
|--------|---------|---------|
| 数据图（折线/柱状/散点） | PDF / SVG | 矢量，字体可编辑 |
| 热图 | PDF | 300 dpi 嵌入 |
| 示意图/流程图 | PDF / TikZ | 矢量，文字可搜索 |
| 照片/显微图像 | PNG / TIFF | 300-600 dpi |
| 统计图 | PDF | seaborn/ggplot2 导出 |

### 3.3 LaTeX 浮动体最佳实践

```latex
% ✅ 推荐：灵活的位置参数
\begin{figure}[tbp]
    \centering
    \includegraphics[width=\columnwidth]{figure.pdf}
    \caption{\textbf{Figure 1:} Caption in sentence case.}
    \label{fig:example}
\end{figure}

% 位置参数含义
% [h] 当前位置  [t] 页面顶部  [b] 页面底部  [p] 独立页面
% [htbp] 推荐组合，LaTeX 按顺序尝试
```

### 3.4 图表设计专项检查（吸收 nature-figure）

- [ ] **配色**：是否使用了色盲友好配色？（禁止红绿纯组合、jet 彩虹配色）
- [ ] **字体**：图表内文字是否 ≥7pt？（出版印刷最小字号）
- [ ] **分辨率**：光栅图 ≥300 dpi，矢量图优先
- [ ] **子图标注**：(a)(b)(c) 用小写字母，通常放在左下角
- [ ] **坐标轴标签**：含单位，如 `Time (s)`、`Accuracy (%)`
- [ ] **误差线**：标注类型（SEM / SD / CI）
- [ ] **统计显著性**：`*P < 0.05, **P < 0.01, ***P < 0.001`
- [ ] **标题**：图表标题用 Sentence case（仅首字母大写）

### 3.5 matplotlib 出版级参数

详见 [journal-styles/nature-cns.md](journal-styles/nature-cns.md) 中的完整参数配置。

---

## 四、表格排版优化

### 4.1 LaTeX 表格最佳实践

```latex
% ✅ 推荐：booktabs 风格（无竖线）
\begin{table}[t]
    \centering
    \caption{\textbf{Table 1:} Performance comparison.}
    \label{tab:results}
    \begin{tabular}{lccc}
        \toprule
        Method & Accuracy & Precision & Recall \\
        \midrule
        Ours    & 92.3\%   & 91.8\%    & 93.1\% \\
        Baseline & 88.5\%  & 87.2\%    & 89.0\% \\
        \bottomrule
    \end{tabular}
\end{table}
```

### 4.2 表格检查清单
- [ ] 使用 `booktabs` 包？（`\toprule` `\midrule` `\bottomrule`）
- [ ] 避免竖线？（学术期刊偏好无竖线表格）
- [ ] 表头与数据对齐？（数字右对齐，文字左对齐）
- [ ] 数据精度一致？（统一小数位数）
- [ ] 粗体标注最优结果？

---

## 五、公式排版规范

### 5.1 行内 vs 独立公式
```latex
% 行内公式（短公式）
The loss function is defined as $\mathcal{L}(x) = \frac{1}{N}\sum_i \ell(x_i)$.

% 独立公式（重要公式，需编号）
\begin{equation}
    \mathcal{L}(x) = \frac{1}{N}\sum_{i=1}^{N} \ell(x_i, y_i)
    \label{eq:loss}
\end{equation}
```

### 5.2 公式检查清单
- [ ] 所有符号是否在正文中定义？
- [ ] 多行公式是否用 `align` 环境？（避免手动对齐）
- [ ] 矩阵/向量符号是否一致？（粗体 vs 箭头）
- [ ] 函数名是否用罗马体？（`\sin` 非 `sin`，`\max` 非 `max`）
- [ ] 公式后标点是否正确？（公式是句子的组成部分）

---

## 六、参考文献排版

### 6.1 BibTeX 编译链检查
```
pdflatex → bibtex → pdflatex × 2    （传统 BibTeX）
pdflatex → biber → pdflatex × 2      （biblatex + biber）
```

### 6.2 常见引用格式文件
| 期刊/会议 | .bst 文件 | 引用样式 |
|----------|----------|---------|
| AAAI | `aaai22.bst` | 作者-年份 |
| IEEE | `IEEEtran.bst` | 编号 [1] |
| ACM | `ACM-Reference-Format.bst` | 编号 [1] |
| NeurIPS | `neurips_2024.bst` | 作者-年份 |
| ICML | `icml2024.bst` | 作者-年份 |
| CVPR | `ieee_fullfirstname.bst` | 编号 [1] |

- [ ] .bst 文件是否与目标会议/期刊匹配？
- [ ] 所有引用是否在 .bib 文件中有对应条目？（调用模块9）
- [ ] 引用 key 格式是否统一？

---

## 七、最终输出格式

```
## LaTeX 检查报告

### 编译诊断
- 错误数：X
- 警告数：Y
- 详情：[逐项列出位置和修复建议]

### 图表检查
- 图表数：X
- 问题：[列出分辨率/配色/标注问题]

### 格式一致性
- 引用格式：[一致/不一致]
- 章节编号：[正确/有问题]
- 页数：[是否符合期刊要求]

### 🆕 出版质量评估
- 图表规范度：1-10
- LaTeX 代码质量：1-10
- 建议：[优先级排序的修改列表]
```

## 与相关模块协作

- → 模块4（期刊适配）：根据目标期刊检查格式
- → 模块9（引用验证）：交叉验证参考文献
- → [journal-styles/nature-cns.md](journal-styles/nature-cns.md)：Nature/CNS 图表规范参考