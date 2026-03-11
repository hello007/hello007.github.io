# Markdown 转 HTML 转换工具

此目录包含将 Markdown 文件转换为专业样式 HTML 的完整工具集。

## 📁 目录结构

```
markdown-convert-html/
├── script/                  # 脚本目录
│   ├── convert_md_to_html.py  # 主转换工具
│   ├── test_regex.py          # 正则表达式测试
│   └── test_process.py        # 段落处理测试
├── SKILL.md                 # 技能说明（中文）
├── SKILL_en.md              # 技能说明（英文）
├── README.md                # 本文件
└── evals/                   # 测试用例
    ├── test-simple.md
    ├── test-complex.md
    └── test-chinese.md
```

## 🚀 使用方法

### 转换单个文件

```bash
python skills/markdown-convert-html/script/convert_md_to_html.py "path/to/file.md"
```

### 转换默认文件集

```bash
python skills/markdown-convert-html/script/convert_md_to_html.py
```

这会自动转换 `ai/03.核心概念知识体系/` 目录下的所有模块文件。

## ✨ 功能特性

- ✅ 自动提取 frontmatter 元数据
- ✅ 生成侧边栏导航（带图标）
- ✅ 支持代码块语法高亮
- ✅ 处理表格、列表、引用块
- ✅ 自动转换 `.md` 链接为 `.html`
- ✅ 响应式设计
- ✅ 中文字体优化

## 🧪 测试

运行测试脚本验证转换逻辑：

```bash
# 测试代码块正则表达式
python skills/markdown-convert-html/script/test_regex.py

# 测试段落包装逻辑
python skills/markdown-convert-html/script/test_process.py
```

## 📖 相关文档

- [项目总体指南](../../.claude/CLAUDE.md)
- [使用规则](../../.claude/rules/md2html.md)
- [技能详细说明](./SKILL.md)
- [技能详细说明（英文）](./SKILL_en.md)
