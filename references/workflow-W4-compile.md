# 工作流 W4：编译校验（静态体检 + 编译 + 页数）

> 生成模式的质量门。目标：产出一份可编译、无未定义引用、页数合规的 PDF。

## Step 1：静态健康检查（无需编译，先跑）

```bash
python scripts/check_tex.py paper/
```

检查项：未闭合环境、未定义 `\ref`/`\cite`、重复 label、定理一致性、写作残留（TODO/VERIFY/DATA_NEEDED）、匿名泄漏、陈旧 section 文件。

> 有 ERROR 先修完再编译；DATA_NEEDED 占位在此时应已处理（补数据或移除对应 claim）。

## Step 2：编译

```bash
cd paper/
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tee compile.log
# 或分步: pdflatex → bibtex → pdflatex ×2
```

**常见错误速查**（详见 module-3）：

| 错误 | 修复 |
|------|------|
| `File 'xxx.sty' not found` | `tlmgr install xxx` 或删除无用 `\usepackage` |
| `Citation 'x' undefined` | bib 缺条目 / 未跑 bibtex / 跑两次 |
| `Reference 'x' undefined` | .aux 过期，重新编译两次 |
| `Overfull \hbox` | 正文严重(>20pt)需修；附录/参考文献适度放宽 |
| 包冲突 | hyperref 最后加载 |

## Step 3：页数校验

- **ML 会议**（ICLR=9/NeurIPS=9/ICML=8/AAAI=7）：正文到 Conclusion 结束，参考文献+附录不计
- **IEEE**：参考文献计入总页数（journal 12-14 页 / conference 5-8 页）
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

若超页：优先把证明/额外结果移附录、压缩表格、收紧写作。

## Step 4：输出检查

- [ ] PDF 存在且 > 100KB
- [ ] 无 `??`（未定义引用）、无 `[?]`（未定义引用）
- [ ] 页数合规
- [ ] 图表渲染正常

→ 下一阶段: [W5 审计](workflow-W5-audit.md)
