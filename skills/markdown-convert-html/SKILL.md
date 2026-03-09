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
- 基于卡片的内容组织
- 语法高亮的代码块
- 样式化的表格、列表和排版
- 多种内容框样式（信息、警告、成功、高亮）
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
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📄</text></svg>">
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
- **侧边栏导航**：粘性定位在左侧，包含所有标题链接
- **主内容区**：右侧，使用基于卡片的章节
- **响应式设计**：移动端时侧边栏堆叠在顶部（max-width: 968px）

#### 配色方案
一致使用这些颜色：
- 主色：`#2563eb`（蓝色）
- 背景：`#f5f7fa`（浅灰色）
- 卡片背景：`#ffffff`（白色）
- 文本：`#4b5563`（深灰色）
- 渐变英雄区：从 `#667eea` 到 `#764ba2` 的线性渐变

#### 字体
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
line-height: 1.8;
```

### 步骤 4：样式化内容元素

#### 标题
- **h1**：42px，粗体，用于英雄区
- **h2**：32px，带有底部边框（3px solid #2563eb）
- **h3**：24px，中等字重
- **h4**：20px，中等字重

#### 代码块
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
}

td {
    padding: 16px;
    border-bottom: 1px solid #e5e7eb;
}
```

#### 内容框
为特殊内容实现 4 种类型的框：

1. **信息框**（蓝色强调）：
```css
.info-box {
    background: #e0e7ff;
    border-left: 4px solid #6366f1;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}
```

2. **警告框**（黄色强调）：
```css
.warning-box {
    background: #fef3c7;
    border-left: 4px solid #f59e0b;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}
```

3. **成功框**（绿色强调）：
```css
.success-box {
    background: #d1fae5;
    border-left: 4px solid #10b981;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}
```

4. **高亮框**（蓝色强调）：
```css
.highlight-box {
    background: #eff6ff;
    border-left: 4px solid #2563eb;
    padding: 25px;
    margin: 30px 0;
    border-radius: 0 8px 8px 0;
}
```

#### 列表
- 使用自定义项目符号样式
- 适当的间距（margin-bottom: 12px）
- 缩进（padding-left: 25px）

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
// 根据滚动位置更新活动链接
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
- 包装在 `<pre><code>` 标签中
- 保留空白和格式
- 使用深色主题样式

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

**信息框模式**：
```markdown
<div class="info-box">
<h4>💡 信息</h4>
<p>内容在这里...</p>
</div>
```

**警告框模式**：
```markdown
<div class="warning-box">
<h4>⚠️ 警告</h4>
<p>内容在这里...</p>
</div>
```

**成功框模式**：
```markdown
<div class="success-box">
<h4>✅ 成功</h4>
<p>内容在这里...</p>
</div>
```

**高亮框模式**：
```markdown
<div class="highlight-box">
<h4>💡 高亮</h4>
<p>内容在这里...</p>
</div>
```

### 步骤 8：输出 HTML 文件

将完整的 HTML 写入与输入 markdown 文件同名的文件，但使用 `.html` 扩展名。

## 文件命名

- 输入：`filename.md`
- 输出：`filename.html`

如果输入文件不遵循此模式，请使用用户提供的文件名。

## 质量检查清单

完成之前，确保：
- [ ] 所有标题都已正确转换并带有 ID
- [ ] 侧边栏导航包含所有主要标题
- [ ] 代码块使用深色主题样式
- [ ] 表格具有正确的标题和样式
- [ ] 内容框样式正确
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
- 使用语义化 HTML5 元素
- 确保可访问性（正确的标题层次、alt 文本等）
- 在 968px 和 640px 处测试响应式断点
- 包含打印友好样式（隐藏侧边栏、移除阴影）
