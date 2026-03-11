# Markdown 转 HTML 规则

当用户需要以下操作时，优先使用 markdown-convert-html 技能：

1. 将 .md 文件转换为 HTML
2. 从 markdown 创建网页
3. 生成 HTML 文档
4. 转换 AI 文档为展示页面
5. 提到"markdown 转 html"、"md2html"、"生成HTML"等关键词

## 快速执行

使用 Python 转换工具：

```bash
# 转换指定文件
python skills/markdown-convert-html/script/convert_md_to_html.py "path/to/file.md"

# 转换所有默认文件 (ai/03.核心概念知识体系/)
python skills/markdown-convert-html/script/convert_md_to_html.py
```

## 参考文档

- **项目总体指南**：[`.claude/CLAUDE.md`](../CLAUDE.md) - 项目概述、完整工具说明、文档标准
- **技能详细规范**：[`skills/markdown-convert-html/SKILL.md`](../../skills/markdown-convert-html/SKILL.md)
- **CSS 模板**：[`ai/AI转型启动会.html`](../../ai/AI转型启动会.html)
