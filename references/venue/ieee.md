# IEEE 期刊/会议投稿规范

> paper-master 模块4 的 IEEE 专项风格库。目标 venue 为 IEEE 时自动加载。

## IEEE 期刊（Transactions / Letters）

### 规划要点
- **通常非匿名**：提交时即含完整作者名、单位、IEEE 会员等级（Member/Senior Member/Fellow）
- **文档类**：`\documentclass[journal]{IEEEtran}`，用 `\cite{}`（数字引用，`cite` 包），**不用 natbib**
- **页数**：参考文献**计入**总页数。Transactions 通常 12-14 页；Letters（WCL/CL/SPL）通常 4-5 页。以具体期刊 author guidelines 为准
- **关键词**：摘要后加 `\begin{IEEEkeywords}`
- **参考文献样式**：`IEEEtran.bst`（数字 [1] 式）
- **biosketch**：camera-ready 版可能要求每位作者的 `\begin{IEEEbiography}`
- **cover letter**：部分期刊要求说明与会议版的差异

### 终检
- [ ] 作者名与会员等级正确
- [ ] 含参考文献的总页数在限制内
- [ ] 图表满足 IEEE 质量：≥300 dpi、坐标轴标签清晰、灰度可读
- [ ] 全程双栏（`[journal]` 选项）
- [ ] 无 `\citep` / `\citet` —— IEEE 只用 `\cite{}`
- [ ] `\bibliographystyle{IEEEtran}`

## IEEE 会议（ICC / GLOBECOM / INFOCOM / ICASSP 等）

### 规划要点
- **多数非匿名**（除 IEEE S&P 等少数）；含完整作者信息
- **文档类**：`\documentclass[conference]{IEEEtran}`，`\cite{}` 数字引用
- **页数**：参考文献计入总页数。典型 5-6 页（ICC/GLOBECOM），部分 8 页（INFOCOM），超页可能收费
- **关键词**：摘要后 `\begin{IEEEkeywords}`
- **无作者简介**（conference 版）
- 部分会议接受 2 页 extended abstract —— 先确认论文类别

### 终检
- [ ] 含参考文献总页数在限制内
- [ ] 双栏 conference 格式下图表可读
- [ ] `\bibliographystyle{IEEEtran}`
- [ ] 无 `\citep` / `\citet`
- [ ] 文档类选项为 `[conference]`（非 `[journal]`）
- [ ] 按投稿门户要求添加 IEEE 版权声明

## IEEE 引用示例

```latex
\documentclass[journal]{IEEEtran}
\usepackage{cite}
\begin{document}
% ...
The method is described in~\cite{smith2020}.
% ...
\bibliographystyle{IEEEtran}
\bibliography{references}
\end{document}
```

## 通用 IEEE 质量要求

- 图表 300 dpi 最低，坐标轴标签清楚，灰度打印可读
- 数学公式规范、变量斜体、函数名罗马体
- 术语一致（见 Banana Rule）
