# Markdown 转 HTML 规则

当用户需要以下操作时，优先使用 markdown-convert-html 技能：

1. 将 .md 文件转换为 HTML
2. 从 markdown 创建网页
3. 生成 HTML 文档
4. 转换 AI 文档为展示页面
5. 提到"markdown 转 html"、"md2html"、"生成HTML"等关键词

## 执行方式

### 方法 1：使用 Python 转换工具（推荐）

```bash
# 转换指定文件
python skills/markdown-convert-html/script/convert_md_to_html.py "path/to/file.md"

# 转换所有默认文件 (ai/03.核心概念知识体系/)
python skills/markdown-convert-html/script/convert_md_to_html.py
```

### 方法 2：使用技能系统

参考技能规范文档：
- 中文：`skills/markdown-convert-html/SKILL.md`
- 英文：`skills/markdown-convert-html/SKILL_en.md`

## 输出规范

- HTML 文件与 markdown 文件同名，但使用 `.html` 扩展名
- 所有 HTML 文件都是自包含的（嵌入式 CSS/JS）
- 使用 UTF-8 编码
- 响应式设计（移动端断点：968px 和 640px）

## 设计标准

### 配色方案
- 主色：`#2563eb` (蓝色)
- 次要色：`#667eea` (紫色)
- 强调色：`#764ba2` (深紫色)
- 背景色：`#f5f7fa` (浅灰色)
- 英雄区渐变：`linear-gradient(135deg, #667eea 0%, #764ba2 100%)`

### 字体
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC',
             'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
line-height: 1.8;
```

## 关键特性

生成的 HTML 页面必须包含：
- ✅ 侧边栏导航（粘性定位）
- ✅ 代码高亮（深色主题）
- ✅ 响应式布局
- ✅ 平滑滚动
- ✅ 返回顶部按钮
- ✅ 打印友好样式

## 参考文档

- 项目总体指南：`.claude/CLAUDE.md`
- 技能详细规范：`skills/markdown-convert-html/SKILL.md`
- CSS 模板：`ai/AI转型启动会.html`

## 注意事项

⚠️ **始终先编辑 `.md` 文件，然后重新生成 `.html`**

⚠️ **HTML 文件是生成的产物，不应手动编辑**

⚠️ **确保中文字符正确显示（UTF-8 编码）**
