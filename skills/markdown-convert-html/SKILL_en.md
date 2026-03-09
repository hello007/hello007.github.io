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
- Card-based content organization
- Syntax-highlighted code blocks
- Styled tables, lists, and typography
- Multiple content box styles (info, warning, success, highlight)
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
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📄</text></svg>">
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
- **Sidebar navigation**: Sticky on the left, contains all heading links
- **Main content area**: Right side, uses card-based sections
- **Responsive design**: Stack sidebar on top for mobile (max-width: 968px)

#### Color Scheme
Use these colors consistently:
- Primary: `#2563eb` (blue)
- Background: `#f5f7fa` (light gray)
- Card background: `#ffffff` (white)
- Text: `#4b5563` (dark gray)
- Gradient hero: Linear gradient from `#667eea` to `#764ba2`

#### Typography
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
line-height: 1.8;
```

### Step 4: Style Content Elements

#### Headings
- **h1**: 42px, bold, used in hero section
- **h2**: 32px, with bottom border (3px solid #2563eb)
- **h3**: 24px, medium weight
- **h4**: 20px, medium weight

#### Code Blocks
```css
pre {
    background: #1f2937;
    color: #f3f4f6;
    padding: 20px;
    border-radius: 8px;
    overflow-x: auto;
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
}

td {
    padding: 16px;
    border-bottom: 1px solid #e5e7eb;
}
```

#### Content Boxes
Implement 4 types of boxes for special content:

1. **Info box** (blue accent):
```css
.info-box {
    background: #e0e7ff;
    border-left: 4px solid #6366f1;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}
```

2. **Warning box** (yellow accent):
```css
.warning-box {
    background: #fef3c7;
    border-left: 4px solid #f59e0b;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}
```

3. **Success box** (green accent):
```css
.success-box {
    background: #d1fae5;
    border-left: 4px solid #10b981;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}
```

4. **Highlight box** (blue accent):
```css
.highlight-box {
    background: #eff6ff;
    border-left: 4px solid #2563eb;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}
```

#### Lists
- Styled with custom bullets
- Proper spacing (margin-bottom: 12px)
- Indentation (padding-left: 25px)

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
- Add to sidebar navigation automatically
- Wrap `h2` sections in `<section>` tags with content-card class

#### Code Blocks
- Wrap in `<pre><code>` tags
- Preserve whitespace and formatting
- Use dark theme styling

#### Tables
- Convert markdown tables to HTML `<table>`
- Add `<thead>` and `<tbody>` structure
- Apply stripe hover effect

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

### Step 7: Special Content Detection

Detect and convert special markdown patterns to content boxes:

**Info box pattern**:
```markdown
<div class="info-box">
<h4>💡 Information</h4>
<p>Content here...</p>
</div>
```

**Warning box pattern**:
```markdown
<div class="warning-box">
<h4>⚠️ Warning</h4>
<p>Content here...</p>
</div>
```

**Success box pattern**:
```markdown
<div class="success-box">
<h4>✅ Success</h4>
<p>Content here...</p>
</div>
```

**Highlight box pattern**:
```markdown
<div class="highlight-box">
<h4>💡 Highlight</h4>
<p>Content here...</p>
</div>
```

### Step 8: Output the HTML File

Write the complete HTML to a file with the same name as the input markdown file, but with `.html` extension.

## File Naming

- Input: `filename.md`
- Output: `filename.html`

If the input file doesn't follow this pattern, use the filename provided by the user.

## Quality Checklist

Before completing, ensure:
- [ ] All headings are properly converted with IDs
- [ ] Sidebar navigation includes all major headings
- [ ] Code blocks use dark theme styling
- [ ] Tables have proper headers and styling
- [ ] Content boxes are properly styled
- [ ] Smooth scrolling works
- [ ] Back-to-top button appears on scroll
- [ ] Active navigation link updates on scroll
- [ ] Responsive design works on mobile
- [ ] Chinese characters display correctly
- [ ] All links work properly
- [ ] Print styles are included

## Important Notes

- Always use UTF-8 encoding for proper Chinese character support
- Include viewport meta tag for responsive design
- Embed all CSS and JavaScript inline (no external dependencies)
- Use semantic HTML5 elements
- Ensure accessibility (proper heading hierarchy, alt text, etc.)
- Test responsive breakpoints at 968px and 640px
- Include print-friendly styles (hide sidebar, remove shadows)
