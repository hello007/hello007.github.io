---
name: markdown-convert-html
description: Convert markdown files to beautiful, responsive HTML pages with sidebar navigation, styled content cards, code highlighting, and professional design. Use this skill whenever the user asks to convert markdown to HTML, wants to create a web page from a markdown file, needs to generate HTML documentation, mentions converting .md files to web pages, or wants to create styled HTML from markdown content. Always use this for markdown-to-HTML conversion tasks.
compatibility: Requires Read, Write tools
---

# Markdown to HTML Converter

This skill converts markdown files into beautiful, responsive HTML pages with professional styling and modern design.

## What This Skill Does

Transforms markdown files into production-ready HTML pages that include:
- Responsive layout with sticky sidebar navigation
- Logo and subtitle area
- Card-based content organization
- Time tags (for presentation materials)
- Syntax-highlighted code blocks
- Styled tables, lists, and typography
- Multiple content box styles (info, warning, success, highlight)
- Q&A question-and-answer box styles
- Smooth scrolling and back-to-top button
- Chinese font optimization
- Mobile-responsive design
- Print-friendly styles

## When to Use

Use this skill whenever you need to:
- Convert a markdown file to HTML
- Create a web page from markdown documentation
- Generate styled HTML from markdown content
- Transform .md files into professional web pages
- Create responsive HTML documentation
- Convert presentation materials to demo web pages

## Conversion Process

### Step 1: Read the Input Markdown

Read the source markdown file specified by the user. If the user provides markdown content directly, use that instead.

### Step 2: Generate HTML Structure

Create a complete HTML5 page with the following structure:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Extract from first # heading or filename]</title>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎯</text></svg>">
    <link rel="shortcut icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎯</text></svg>">
    <style>
        /* Include all styles here */
    </style>
</head>
<body>
    <!-- Page content -->
</body>
</html>
```

### Step 3: Implement Core Design Features

#### Layout Structure

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

#### Sidebar Navigation Design

```css
/* Logo area */
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

/* Navigation menu */
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

#### Hero Section

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

#### Color Scheme

```css
/* Primary colors */
--primary-color: #2563eb;
--secondary-color: #667eea;
--accent-color: #764ba2;

/* Background colors */
--bg-color: #f5f7fa;
--card-bg: #ffffff;

/* Text colors */
--text-primary: #1f2937;
--text-secondary: #374151;
--text-tertiary: #4b5563;
--text-muted: #666;

/* Gradients */
--hero-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

#### Typography

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
line-height: 1.8;
```

### Step 4: Style Content Elements

#### Headings

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

#### Code Blocks

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

#### Tables

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

#### Content Boxes

Implement multiple types of boxes for special content:

**1. Info Box (Indigo)**

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

**2. Warning Box (Yellow)**

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

**3. Success Box (Green)**

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

**4. Highlight Box (Blue)**

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

#### Q&A Question-and-Answer Box (Special Style)

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

#### Time Tags

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

#### Lists

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

#### Blockquotes

```css
blockquote {
    margin: 20px 0;
    padding: 15px 20px;
    border-left: 4px solid #2563eb;
    background: #f8fafc;
    color: #4b5563;
    border-radius: 0 8px 8px 0;
}

blockquote p {
    margin: 0;
    line-height: 1.8;
}

blockquote strong {
    color: #1f2937;
}
```

**Conversion Rules:**
- Lines starting with `>` convert to `<blockquote>`
- Consecutive quote lines merge into one blockquote
- Remove `>` prefix, preserve markdown formatting (bold, italic, etc.)
- Wrap each quote line in `<p>` tags

**Example:**

```markdown
> **Business Director:** "Everyone's talking about AI, can we build a smart customer service too?"
>
> **My response at the time:** "This... needs evaluation, it's quite complex technically..."
```

Should convert to:

```html
<blockquote>
<p><strong>Business Director:</strong> "Everyone's talking about AI, can we build a smart customer service too?"</p>
<p><strong>My response at the time:</strong> "This... needs evaluation, it's quite complex technically..."</p>
</blockquote>
```

### Step 5: Add Interactive Features

#### Smooth Scrolling

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

#### Back-to-Top Button

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
// Show/hide based on scroll position
window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        backToTop.classList.add('show');
    } else {
        backToTop.classList.remove('show');
    }
});
```

#### Active Navigation Link

```javascript
// Update active link based on scroll position
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

### Step 6: Convert Markdown Elements

#### Headings

- Extract all `#`, `##`, `###` headings
- Generate IDs for navigation: `id="heading-name"`
- Automatically add to sidebar navigation
- Wrap `h2` sections in `<section>` tags with content-card class

**Navigation Icon Auto-Selection Rules:**

The system automatically selects appropriate Emoji icons based on keywords in the heading:

| Icon | Keywords | Use Case |
|------|----------|----------|
| 🎯 | 掌握、目标、学习 | Learning objectives, mastery points |
| 📖 | 详解、详细、说明、介绍 | Detailed explanations, introductions |
| 🤖 | AI, 智能, 模型, LLM, 大语言 | AI models, LLM related |
| ⚙️ | 应用、技术、开发 | Application technology, development |
| 🏗️ | 工程、架构、框架、系统 | Engineering architecture, system design |
| 📊 | 数据、知识、向量、数据库 | Data processing, knowledge base, vector database |
| 🔒 | 安全、合规、隐私、防护 | Security protection, compliance |
| 🛠️ | 方法、工具、技巧、实践 | Tools and methods, practices |
| 💡 | 概念、基础、入门、原理 | Basic concepts, principles |
| ⭐ | 核心、重要、关键 | Core content, key points |
| 🎨 | 设计、模式、架构 | Design patterns, architecture |
| ✅ | 测试、验证、检查 | Testing, verification, checklists |
| ❓ | 问题、问答、Q&A、FAQ | Q&A, FAQ |
| ⚠️ | 警告、注意、提示 | Warnings, notices |
| 🚀 | 进阶、前沿、高级、深入 | Advanced content, cutting-edge tech |
| 📝 | 总结、回顾、概览 | Summaries, reviews, overviews |
| 🔧 | 环境、配置、安装、部署 | Environment configuration, deployment |
| ⚡ | 性能、优化、提升 | Performance optimization |
| 🎬 | 示例、案例、演示 | Examples, demos, case studies |
| 📋 | 协议、标准、规范 | Protocols, standards, specifications |
| 🤝 | 协作、通信、交互 | Collaboration, communication, interaction |
| 📁 | 资源、参考、文档 | Resources, documentation |
| 📚 | *default* | Other general content |

#### Code Blocks

**Fenced Code Blocks:**

Correctly convert fenced code blocks (```):

```markdown
​```java
public class Example {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
​```
```

Should convert to:

```html
<pre><code class="language-java">public class Example {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}</code></pre>
```

**Key Conversion Rules:**

1. **Detect fenced code blocks**: Look for three or more backticks (```)
2. **Extract language identifier**: The language at the start (e.g., java, bash) should become the class value, like `class="language-java"`
3. **Preserve full content**: All content within the code block (including newlines, indentation) must be preserved exactly
4. **Don't convert markdown inside code blocks**: Markdown syntax within code blocks should not be processed
5. **Output structure**:
   - Outer: `<pre>` tag (preserves whitespace and formatting)
   - Inner: `<code>` tag (contains actual code)
   - Optional: `class="language-xxx"` for syntax highlighting

**Common Mistakes:**

❌ **Wrong approach:**
- Convert ``` to `<code>` tags (this causes formatting chaos)
- Wrap code content in `<p>` tags
- Merge multi-line code into single line
- Keep language identifier as text content

✅ **Correct approach:**
- Completely remove ``` markers, output nothing
- Wrap code content with `<pre><code>`
- Preserve all newlines and indentation
- Convert language identifier to class attribute

**Inline Code:**

```markdown
This is `inline code` example
```

Should convert to:

```html
This is <code>inline code</code> example
```

Content wrapped in single backticks should convert to `<code>` tags.

#### Tables

- Convert markdown tables to HTML `<table>`
- Add `<thead>` and `<tbody>` structure
- Apply zebra stripe hover effect

#### Lists

- Convert `-` and `*` to `<ul>`
- Convert `1.` to `<ol>`
- Preserve nested list structure

#### Emphasis

- `**bold**` → `<strong>`
- `*italic*` → `<em>`
- `` `code` `` → `<code>`

#### Links

- `[text](url)` → `<a href="url">text</a>`
- Add target="_blank" for external links
- **Auto-convert `.md` extension to `.html`**: Links pointing to `.md` files are automatically converted to `.html`
  - Example: `[Document](guide.md)` → `<a href="guide.html">Document</a>`

### Step 7: Special Content Detection

Detect and convert special markdown patterns to content boxes:

**Info box pattern:**

```markdown
<div class="info-box">
<h4>💡 Information</h4>
<p>Content here...</p>
</div>
```

**Warning box pattern:**

```markdown
<div class="warning-box">
<h4>⚠️ Warning</h4>
<p>Content here...</p>
</div>
```

**Success box pattern:**

```markdown
<div class="success-box">
<h4>✅ Success</h4>
<p>Content here...</p>
</div>
```

**Highlight box pattern:**

```markdown
<div class="highlight-box">
<h4>💡 Highlight</h4>
<p>Content here...</p>
</div>
```

**Q&A question-and-answer box pattern:**

```markdown
<div class="qa-box">
<div class="question">Q: Question title</div>
<div class="answer">
<p><strong>A:</strong> Answer content</p>
</div>
</div>
```

### Step 8: Output the HTML File

Write the complete HTML to a file with the same name as the input markdown file, but with `.html` extension.

## File Naming

- Input: `filename.md`
- Output: `filename.html`

If the input file doesn't follow this pattern, use the filename provided by the user.

## Responsive Design

```css
/* Tablet devices */
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

/* Mobile devices */
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

## Print Styles

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

## Quality Checklist

Before completing, ensure:
- [ ] All headings are properly converted with IDs
- [ ] Sidebar navigation includes all major headings
- [ ] Logo and subtitle display correctly
- [ ] Time tags are applied correctly (if applicable)
- [ ] Hero section gradient background is correct
- [ ] Code blocks use dark theme styling
- [ ] Tables have proper headers and styling
- [ ] Content box styles are correct
- [ ] Q&A question-and-answer box styles are correct (if applicable)
- [ ] Smooth scrolling works
- [ ] Back-to-top button appears on scroll
- [ ] Active navigation link updates on scroll
- [ ] Responsive design works on mobile devices
- [ ] Chinese characters display correctly
- [ ] All links work properly
- [ ] Print styles are included

## Important Notes

- Always use UTF-8 encoding for proper Chinese character support
- Include viewport meta tag for responsive design
- Embed all CSS and JavaScript inline (no external dependencies)
- Use semantic HTML5 elements (`<aside>`, `<main>`, `<section>`, `<nav>`)
- Ensure accessibility (proper heading hierarchy, alt text, etc.)
- Test responsive breakpoints at 968px and 640px
- Include print-friendly styles (hide sidebar, remove shadows)
- Use emoji icons to enhance visual appeal
- Maintain consistent design style with AI转型启动会.html
