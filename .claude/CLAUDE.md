# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在此仓库中工作时提供指导。

## 项目概述

这是一个 GitHub Pages 网站 (`hello007.github.io`)，用于 AI 转型文档。该网站为向 AI 开发转型的团队提供实用指南和资源。

**网站地址：** https://hello007.github.io

**技术栈：**
- 通过 GitHub Pages 进行静态网站托管
- 使用 Jekyll（minimal 主题）生成网站
- 自定义 Python 工具将 Markdown 转换为 HTML
- 带有嵌入式 CSS/JS 的响应式 HTML

## 项目结构

```
hello007.github.io/
├── _config.yml                 # Jekyll 配置
├── index.html                  # 带导航卡片的着陆页
├── skills/                     # Claude 技能定义
│   └── markdown-convert-html/  # Markdown转HTML转换技能
│       ├── script/                 # 脚本目录
│       │   ├── convert_md_to_html.py   # 主工具：将 MD 转换为 HTML
│       │   └── test_*.py               # 转换器测试脚本
│       ├── SKILL.md               # 技能说明（中文）
│       ├── SKILL_en.md            # 技能说明（英文）
│       └── evals/                 # 测试用例
├── ai/                         # 文档内容
│   ├── AI转型启动会.md/html
│   ├── 团队向AI方向转型实操指南.md/html
│   └── 03.核心概念知识体系/    # 核心知识库
│       ├── 01.AI基础层概念详解.md/html
│       ├── 02.AI应用层核心技术详解.md/html
│       ├── ... (共7个模块)
│       └── README.md/html
└── .claude/
    ├── CLAUDE.md               # 项目指南
    ├── rules/                  # Claude 规则
    │   └── md2html.md          # Markdown转HTML规则
    └── settings.local.json     # 本地 Claude 设置
```

## 核心工具

### convert_md_to_html.py

位于 `skills/markdown-convert-html/convert_md_to_html.py`，用于将 markdown 文档转换为样式化 HTML 页面的主要工具。

**使用方法：**
```bash
# 转换指定文件
python skills/markdown-convert-html/script/convert_md_to_html.py "path/to/file.md"

# 转换所有默认文件 (ai/03.核心概念知识体系/)
python skills/markdown-convert-html/script/convert_md_to_html.py
```

**功能特性：**
- 提取 frontmatter 元数据（文档定位、学习目标、适合人群）
- 从 `##` 标题生成侧边栏导航
- 处理带语言标识符的代码块
- 支持表格、列表、强调、链接
- 创建带粘性侧边栏的响应式 HTML
- 使用 `ai/AI转型启动会.html` 作为 CSS 模板

**关键实现细节：**
- 使用占位符系统在 markdown 处理期间保护代码块
- 跟踪 `in_pre_block` 状态以防止代码块内出现 `<p>` 标签
- 从模板 HTML 文件中提取 CSS

### Skills 系统

`skills/` 目录包含可复用的 Claude 技能。主要技能是 `markdown-convert-html/`，它提供了将 markdown 转换为专业样式 HTML 的说明。

**技能结构：**
- `SKILL.md` - 主要技能说明（双语：中文/English）
- `evals/` - 验证测试用例
- `evals.json` - 测试用例定义

## 文档标准

### Markdown Frontmatter

`ai/03.核心概念知识体系/` 中的所有文档 markdown 文件应包含：

```markdown
# 标题

**文档定位：** [定位说明]
**学习目标：** [学习目标]
**适合人群：** [目标受众]
**重要说明：** [可选说明]

## 内容从这里开始...
```

### HTML 输出规范

- 输出文件与输入文件同名，但使用 `.html` 扩展名
- 所有 HTML 文件都是自包含的（嵌入式 CSS/JS）
- 使用 UTF-8 编码支持中文字符
- 响应式设计，移动端断点为 968px 和 640px

### 设计语言

**配色：**
- 主色：`#2563eb` (蓝色)
- 次要色：`#667eea` (紫色)
- 强调色：`#764ba2` (深紫色)
- 背景色：`#f5f7fa` (浅灰色)
- 英雄区渐变：`linear-gradient(135deg, #667eea 0%, #764ba2 100%)`

**字体：**
```
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC',
             'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
line-height: 1.8;
```

## 常见任务

### 添加新文档

1. 在相应的 `ai/` 子目录中创建 markdown 文件
2. 包含正确的 frontmatter（文档定位、学习目标、适合人群）
3. 使用 `##` 标题作为主要章节（自动生成导航）
4. 转换为 HTML：
   ```bash
   python skills/markdown-convert-html/script/convert_md_to_html.py "path/to/new-file.md"
   ```

### 更新现有文档

1. 编辑 `.md` 文件
2. 重新运行转换以更新 `.html`
3. 两个文件应保持同步

### 测试转换器更改

可使用以下测试脚本：
```bash
python skills/markdown-convert-html/script/test_regex.py      # 测试代码块正则表达式模式
python skills/markdown-convert-html/script/test_process.py    # 测试段落包装逻辑
```

## 文件命名规范

- Markdown 文件使用描述性中文名称：`01.AI基础层概念详解.md`
- HTML 文件镜像 markdown 名称：`01.AI基础层概念详解.html`
- 数字前缀（01.、02.）用于目录排序
- 使用 `README.md` 作为目录概览页面

## 重要说明

- **始终先编辑 `.md` 文件**，然后重新生成 `.html`
- `skills/markdown-convert-html/script/convert_md_to_html.py` 脚本是权威转换器 - 使用它而不是手动编辑 HTML
- HTML 文件是生成的产物，不应手动编辑
- 使用 `skills/markdown-convert-html/evals/` 中的测试文件测试 markdown 转 HTML 转换
- 网站主要内容为中文 - 确保 UTF-8 编码和正确的中文字体支持
