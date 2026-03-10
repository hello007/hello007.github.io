---
name: markdown-convert-html
description: 将 markdown 文件转换为美观、响应式的 HTML 页面，包含侧边栏导航、样式化内容卡片、代码高亮和专业设计。当用户要求将 markdown 转换为 HTML、想要从 markdown 文件创建网页、需要生成 HTML 文档、提及将 .md 文件转换为网页，或想要从 markdown 内容创建样式化 HTML 时，使用此技能。始终将此技能用于 markdown 转 HTML 转换任务。
compatibility: 需要 Read、Write 工具
---

# Markdown 转 HTML 转换器

此技能将 markdown 文件转换为具有专业样式和现代设计的美观、响应式 HTML 页面。

## 技能功能

将 markdown 文件转换为生产就绪的 HTML 页面，包括：
- 带有粘性侧边栏导航的响应式布局
- Logo 和副标题区域
- 基于卡片的内容组织
- 时间标签（适用于宣讲材料）
- 语法高亮的代码块
- 样式化的表格、列表和排版
- 多种内容框样式（信息、警告、成功、高亮）
- Q&A 问答框样式
- 平滑滚动和返回顶部按钮
- 中文字体优化
- 移动端响应式设计
- 打印友好样式

## 使用时机

在以下情况下使用此技能：
- 将 markdown 文件转换为 HTML
- 从 markdown 文档创建网页
- 从 markdown 内容生成样式化 HTML
- 将 .md 文件转换为专业网页
- 创建响应式 HTML 文档
- 转换宣讲材料为演示网页

## 转换流程

### 步骤 1：读取输入的 Markdown

读取用户指定的源 markdown 文件。如果用户直接提供 markdown 内容，则使用该内容。

### 步骤 2：生成 HTML 结构

创建具有以下结构的完整 HTML5 页面：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[从第一个 # 标题或文件名提取]</title>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎯</text></svg>">
    <link rel="shortcut icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎯</text></svg>">
    <style>
        /* 在此包含所有样式 */
    </style>
</head>
<body>
    <!-- 页面内容 -->
</body>
</html>
```

### 步骤 3：实现核心设计特性

#### 布局结构

```css
.container {
    display: flex;
    max-width: 1400px;
    margin: 0 auto;
    padding: 20px;
    gap: 30px;
}

.sidebar {
    width: 280px;
    flex-shrink: 0;
    position: sticky;
    top: 20px;
    height: fit-content;
    max-height: calc(100vh - 40px);
    overflow-y: auto;
    background: white;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}

.main-content {
    flex: 1;
    min-width: 0;
}
```

#### 侧边栏导航设计

```css
/* Logo 区域 */
.logo {
    font-size: 24px;
    font-weight: bold;
    color: #2563eb;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.logo-icon {
    font-size: 32px;
}

.subtitle {
    font-size: 13px;
    color: #666;
    margin-bottom: 25px;
    padding-bottom: 20px;
    border-bottom: 1px solid #e5e7eb;
}

/* 导航菜单 */
.nav-menu {
    list-style: none;
}

.nav-item {
    margin-bottom: 8px;
}

.nav-link {
    display: block;
    padding: 10px 15px;
    color: #4b5563;
    text-decoration: none;
    border-radius: 8px;
    transition: all 0.3s;
    font-size: 14px;
}

.nav-link:hover {
    background: #f3f4f6;
    color: #2563eb;
}

.nav-link.active {
    background: #2563eb;
    color: white;
}
```

#### 英雄区域（Hero Section）

```css
.hero-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 50px 40px;
    border-radius: 12px;
    margin-bottom: 30px;
    box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
}

.hero-meta {
    display: flex;
    gap: 30px;
    margin-top: 20px;
    flex-wrap: wrap;
}

.meta-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 15px;
}

.meta-icon {
    font-size: 20px;
}
```

#### 配色方案

```css
/* 主色调 */
--primary-color: #2563eb;
--secondary-color: #667eea;
--accent-color: #764ba2;

/* 背景色 */
--bg-color: #f5f7fa;
--card-bg: #ffffff;

/* 文本色 */
--text-primary: #1f2937;
--text-secondary: #374151;
--text-tertiary: #4b5563;
--text-muted: #666;

/* 渐变 */
--hero-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

#### 字体

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
line-height: 1.8;
```

### 步骤 4：样式化内容元素

#### 标题

```css
h1 {
    font-size: 42px;
    margin-bottom: 15px;
    font-weight: 700;
}

h2 {
    font-size: 32px;
    color: #1f2937;
    margin: 50px 0 25px;
    padding-bottom: 15px;
    border-bottom: 3px solid #2563eb;
    font-weight: 700;
}

h3 {
    font-size: 24px;
    color: #374151;
    margin: 35px 0 20px;
    font-weight: 600;
}

h4 {
    font-size: 20px;
    color: #4b5563;
    margin: 30px 0 15px;
    font-weight: 600;
}
```

#### 代码块

```css
pre {
    background: #1f2937;
    color: #f3f4f6;
    padding: 20px;
    border-radius: 8px;
    overflow-x: auto;
    margin: 20px 0;
    font-size: 14px;
    line-height: 1.6;
}

code {
    background: #f3f4f6;
    color: #dc2626;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 13px;
}

pre code {
    background: transparent;
    color: inherit;
    padding: 0;
}
```

#### 表格

```css
table {
    width: 100%;
    border-collapse: collapse;
    margin: 25px 0;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

th {
    background: #2563eb;
    color: white;
    padding: 16px;
    text-align: left;
    font-weight: 600;
    font-size: 15px;
}

td {
    padding: 16px;
    border-bottom: 1px solid #e5e7eb;
    font-size: 15px;
}

tr:last-child td {
    border-bottom: none;
}

tr:hover {
    background: #f9fafb;
}
```

#### 内容框

为特殊内容实现多种类型的框：

**1. 信息框（靛蓝色）**

```css
.info-box {
    background: #e0e7ff;
    border-left: 4px solid #6366f1;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}

.info-box h4 {
    color: #4338ca;
    margin-bottom: 10px;
}
```

**2. 警告框（黄色）**

```css
.warning-box {
    background: #fef3c7;
    border-left: 4px solid #f59e0b;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}

.warning-box h4 {
    color: #b45309;
    margin-bottom: 10px;
}
```

**3. 成功框（绿色）**

```css
.success-box {
    background: #d1fae5;
    border-left: 4px solid #10b981;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}

.success-box h4 {
    color: #047857;
    margin-bottom: 10px;
}
```

**4. 高亮框（蓝色）**

```css
.highlight-box {
    background: #eff6ff;
    border-left: 4px solid #2563eb;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}

.highlight-box h4 {
    color: #1d4ed8;
    margin-bottom: 10px;
}
```

#### Q&A 问答框（特殊样式）

```css
.qa-box {
    background: #f9fafb;
    border-radius: 12px;
    padding: 30px;
    margin: 30px 0;
    border-left: 5px solid #2563eb;
}

.question {
    font-size: 18px;
    font-weight: 600;
    color: #1f2937;
    margin-bottom: 15px;
}

.answer {
    color: #4b5563;
    line-height: 1.8;
}
```

#### 时间标签

```css
.time-tag {
    display: inline-block;
    background: #fef3c7;
    color: #92400e;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 15px;
}
```

#### 列表

```css
ul, ol {
    margin: 15px 0;
    padding-left: 25px;
}

li {
    margin-bottom: 12px;
    color: #4b5563;
    line-height: 1.8;
}
```

### 步骤 5：添加交互功能

#### 平滑滚动

```javascript
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
```

#### 返回顶部按钮

```css
.back-to-top {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: #2563eb;
    color: white;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: none;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    transition: all 0.3s;
    font-size: 24px;
}

.back-to-top.show {
    display: flex;
}
```

```javascript
// 根据滚动位置显示/隐藏
window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        backToTop.classList.add('show');
    } else {
        backToTop.classList.remove('show');
    }
});
```

#### 活动导航链接

```javascript
// 滚动时更新活动导航链接
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section[id]');
    const scrollPosition = window.pageYOffset + 100;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');

        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.classList.add('active');
                }
            });
        }
    });
});
```

### 步骤 6：转换 Markdown 元素

#### 标题

- 提取所有 `#`、`##`、`###` 标题
- 为导航生成 ID：`id="heading-name"`
- 自动添加到侧边栏导航
- 将 `h2` 章节包装在带有 content-card 类的 `<section>` 标签中

#### 代码块

**Fenced Code Blocks（围栏代码块）：**

正确转换 fenced code blocks（```）：

```markdown
​```java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
​```
```

应转换为：

```html
<pre><code class="language-java">public class Example {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}</code></pre>
```

**关键转换规则：**

1. **检测 fenced code blocks**：查找三个或更多反引号（```）
2. **提取语言标识符**：开头的语言（如 java、bash）应作为 class 值，如 `class="language-java"`
3. **保留完整内容**：代码块内的所有内容（包括换行、缩进）必须原样保留
4. **不要转换代码块内的 markdown**：代码块内的 markdown 语法不应被处理
5. **输出结构**：
   - 外层：`<pre>` 标签（保留空白和格式）
   - 内层：`<code>` 标签（包含实际代码）
   - 可选：`class="language-xxx"` 用于语法高亮

**常见错误：**

❌ **错误做法：**
- 将 ``` 转换为 `<code>` 标签（这会导致格式混乱）
- 将代码内容包装在 `<p>` 标签中
- 将多行代码合并成单行
- 保留语言标识符作为文本内容

✅ **正确做法：**
- 完整移除 ``` 标记，不输出任何内容
- 用 `<pre><code>` 包装代码内容
- 保留所有换行和缩进
- 将语言标识符转换为 class 属性

**Inline Code（行内代码）：**

```markdown
这是 `行内代码` 示例
```

应转换为：

```html
这是 <code>行内代码</code> 示例
```

使用单个反引号包裹的内容应转换为 `<code>` 标签。

#### 表格

- 将 markdown 表格转换为 HTML `<table>`
- 添加 `<thead>` 和 `<tbody>` 结构
- 应用斑马纹悬停效果

#### 列表

- 将 `-` 和 `*` 转换为 `<ul>`
- 将 `1.` 转换为 `<ol>`
- 保留嵌套列表结构

#### 强调

- `**粗体**` → `<strong>`
- `*斜体*` → `<em>`
- `` `代码` `` → `<code>`

#### 链接

- `[文本](url)` → `<a href="url">文本</a>`
- 为外部链接添加 target="_blank"

### 步骤 7：特殊内容检测

检测并将特殊的 markdown 模式转换为内容框：

**信息框模式：**

```markdown
<div class="info-box">
<h4>💡 信息</h4>
<p>内容在这里...</p>
</div>
```

**警告框模式：**

```markdown
<div class="warning-box">
<h4>⚠️ 警告</h4>
<p>内容在这里...</p>
</div>
```

**成功框模式：**

```markdown
<div class="success-box">
<h4>✅ 成功</h4>
<p>内容在这里...</p>
</div>
```

**高亮框模式：**

```markdown
<div class="highlight-box">
<h4>💡 高亮</h4>
<p>内容在这里...</p>
</div>
```

**Q&A 问答框模式：**

```markdown
<div class="qa-box">
<div class="question">Q：问题标题</div>
<div class="answer">
<p><strong>A：</strong>答案内容</p>
</div>
</div>
```

### 步骤 8：输出 HTML 文件

将完整的 HTML 写入与输入 markdown 文件同名的文件，但使用 `.html` 扩展名。

## 文件命名

- 输入：`filename.md`
- 输出：`filename.html`

如果输入文件不遵循此模式，请使用用户提供的文件名。

## 响应式设计

```css
/* 平板设备 */
@media (max-width: 968px) {
    .container {
        flex-direction: column;
    }

    .sidebar {
        width: 100%;
        position: static;
        max-height: none;
    }
}

/* 移动设备 */
@media (max-width: 640px) {
    .content-card {
        padding: 25px;
    }

    h1 {
        font-size: 32px;
    }

    h2 {
        font-size: 26px;
    }

    .hero-meta {
        flex-direction: column;
        gap: 10px;
    }
}
```

## 打印样式

```css
@media print {
    .sidebar {
        display: none;
    }

    .container {
        max-width: 100%;
    }

    .content-card {
        box-shadow: none;
        page-break-inside: avoid;
    }

    .back-to-top {
        display: none;
    }
}
```

## 质量检查清单

完成之前，确保：
- [ ] 所有标题都已正确转换并带有 ID
- [ ] 侧边栏导航包含所有主要标题
- [ ] Logo 和副标题正确显示
- [ ] 时间标签正确应用（如适用）
- [ ] 英雄区域渐变背景正确
- [ ] 代码块使用深色主题样式
- [ ] 表格具有正确的标题和样式
- [ ] 内容框样式正确
- [ ] Q&A 问答框样式正确（如适用）
- [ ] 平滑滚动正常工作
- [ ] 返回顶部按钮在滚动时显示
- [ ] 活动导航链接在滚动时更新
- [ ] 响应式设计在移动设备上正常工作
- [ ] 中文字符正确显示
- [ ] 所有链接正常工作
- [ ] 包含打印样式

## 重要说明

- 始终使用 UTF-8 编码以正确支持中文字符
- 包含 viewport 元标签以实现响应式设计
- 将所有 CSS 和 JavaScript 内联嵌入（无外部依赖）
- 使用语义化 HTML5 元素（`<aside>`, `<main>`, `<section>`, `<nav>`）
- 确保可访问性（正确的标题层次、alt 文本等）
- 在 968px 和 640px 处测试响应式断点
- 包含打印友好样式（隐藏侧边栏、移除阴影）
- 使用 Emoji 图标增强视觉效果
- 保持与 AI转型启动会.html 一致的设计风格
