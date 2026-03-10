#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown to HTML Converter
Converts markdown files to HTML with the same styling as AI转型启动会.html
"""

import re
import os
from pathlib import Path

def read_template():
    """Read the template HTML file to extract styles and structure"""
    template_path = Path(__file__).parent / "ai" / "AI转型启动会.html"
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract CSS from style tag
    css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    css = css_match.group(1) if css_match else ""

    return css

def generate_html_from_markdown(md_content, title, css):
    """Convert markdown content to HTML with full styling"""

    # Code blocks - process BEFORE other conversions to protect them
    code_blocks = []
    placeholder_template = "___CODE_BLOCK_{}___"

    def extract_code_block(match):
        language = match.group(1) if match.group(1) else ''
        code = match.group(2)
        idx = len(code_blocks)
        code_blocks.append((language, code))
        return placeholder_template.format(idx)

    # Extract and protect code blocks
    html_content = re.sub(r'```(\w*)\n(.*?)\n```', extract_code_block, md_content, flags=re.DOTALL)

    # Extract metadata from frontmatter
    doc_position = re.search(r'\*\*文档定位：\*\*\s*(.*?)\n', md_content)
    learning_goal = re.search(r'\*\*学习目标：\*\*\s*(.*?)\n', md_content)
    target_audience = re.search(r'\*\*适合人群：\*\*\s*(.*?)\n', md_content)

    doc_position = doc_position.group(1).strip() if doc_position else ""
    learning_goal = learning_goal.group(1).strip() if learning_goal else ""
    target_audience = target_audience.group(1).strip() if target_audience else ""

    # Extract main title (first # heading)
    title_match = re.search(r'^#\s+(.+?)\n', md_content)
    main_title = title_match.group(1).strip() if title_match else title

    # Build navigation from ## headings
    headings = re.findall(r'^##\s+(.+?)\n', md_content, re.MULTILINE)

    # Generate navigation HTML
    nav_html = ""
    for i, heading in enumerate(headings):
        # Create ID from heading
        heading_id = re.sub(r'[^\w\u4e00-\u9fa5]+', '-', heading).strip('-').lower()
        emoji = "📚"
        if "掌握" in heading:
            emoji = "🎯"
        elif "详解" in heading:
            emoji = "📖"
        nav_html += f'''
                    <li class="nav-item">
                        <a href="#{heading_id}" class="nav-link">{emoji} {heading}</a>
                    </li>'''

    # Extract main title (first # heading)
    title_match = re.search(r'^#\s+(.+?)\n', html_content)
    main_title = title_match.group(1).strip() if title_match else title

    # Build navigation from ## headings
    headings = re.findall(r'^##\s+(.+?)\n', html_content, re.MULTILINE)

    # Generate navigation HTML
    nav_html = ""
    for i, heading in enumerate(headings):
        # Create ID from heading
        heading_id = re.sub(r'[^\w\u4e00-\u9fa5]+', '-', heading).strip('-').lower()
        emoji = "📚"
        if "掌握" in heading:
            emoji = "🎯"
        elif "详解" in heading:
            emoji = "📖"
        nav_html += f'''
                    <li class="nav-item">
                        <a href="#{heading_id}" class="nav-link">{emoji} {heading}</a>
                    </li>'''

    # Convert markdown elements to HTML
    # Remove frontmatter metadata
    html_content = re.sub(r'\*\*文档定位：\*\*.*?\n', '', html_content)
    html_content = re.sub(r'\*\*学习目标：\*\*.*?\n', '', html_content)
    html_content = re.sub(r'\*\*适合人群：\*\*.*?\n', '', html_content)
    html_content = re.sub(r'\*\*重要说明：\*\*.*?\n', '', html_content)

    # Main title
    html_content = re.sub(r'^#\s+(.+?)\n', '', html_content, count=1)

    # ## headings with ID
    html_content = re.sub(r'^##\s+(.+?)$',
                          lambda m: f'<h2 id="{re.sub(r"[^\w\u4e00-\u9fa5]+", "-", m.group(1)).strip("-").lower()}">{m.group(1)}</h2>',
                          html_content, flags=re.MULTILINE)

    # ### headings
    html_content = re.sub(r'^###\s+(.+?)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)

    # #### headings
    html_content = re.sub(r'^####\s+(.+?)$', r'<h4>\1</h4>', html_content, flags=re.MULTILINE)

    # Bold text
    html_content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html_content)

    # Italic text
    html_content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html_content)

    # Inline code
    html_content = re.sub(r'`([^`]+?)`', r'<code>\1</code>', html_content)

    # Links
    html_content = re.sub(r'\[([^\]]+?)\]\(([^\)]+?)\)', r'<a href="\2">\1</a>', html_content)

    # Unordered lists
    def convert_list(lines):
        in_list = False
        result = []
        current_list = []

        for line in lines:
            if line.strip().startswith('- ') or line.strip().startswith('* '):
                if not in_list:
                    in_list = True
                    current_list = ['<ul>']
                item_text = re.sub(r'^[\s]*[-*]\s+', '', line)
                # Handle bold and code within list items
                item_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', item_text)
                item_text = re.sub(r'`([^`]+?)`', r'<code>\1</code>', item_text)
                current_list.append(f'<li>{item_text}</li>')
            else:
                if in_list:
                    current_list.append('</ul>')
                    result.extend(current_list)
                    current_list = []
                    in_list = False
                result.append(line)

        if in_list:
            current_list.append('</ul>')
            result.extend(current_list)

        return result

    lines = html_content.split('\n')
    lines = convert_list(lines)
    html_content = '\n'.join(lines)

    # Ordered lists
    def convert_ordered_list(lines):
        in_list = False
        result = []
        current_list = []

        for line in lines:
            if re.match(r'^\s*\d+\.\s+', line):
                if not in_list:
                    in_list = True
                    current_list = ['<ol>']
                item_text = re.sub(r'^\s*\d+\.\s+', '', line)
                item_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', item_text)
                item_text = re.sub(r'`([^`]+?)`', r'<code>\1</code>', item_text)
                current_list.append(f'<li>{item_text}</li>')
            else:
                if in_list:
                    current_list.append('</ol>')
                    result.extend(current_list)
                    current_list = []
                    in_list = False
                result.append(line)

        if in_list:
            current_list.append('</ol>')
            result.extend(current_list)

        return result

    lines = html_content.split('\n')
    lines = convert_ordered_list(lines)
    html_content = '\n'.join(lines)

    # Tables
    def convert_table(match):
        table_content = match.group(0)
        lines = table_content.strip().split('\n')

        if len(lines) < 2:
            return match.group(0)

        # Parse header
        header_line = lines[0]
        headers = [h.strip() for h in header_line.split('|')[1:-1]]

        # Parse separator
        if len(lines) > 1 and '|' in lines[1]:
            lines = lines[2:]  # Skip separator line
        else:
            lines = lines[1:]

        # Parse rows
        rows = []
        for line in lines:
            if '|' in line:
                cells = [c.strip() for c in line.split('|')[1:-1]]
                if cells:
                    rows.append(cells)

        # Build HTML table
        table_html = '<table>\n'
        table_html += '<thead>\n<tr>\n'
        for h in headers:
            table_html += f'<th>{escape_html(h)}</th>\n'
        table_html += '</tr>\n</thead>\n'
        table_html += '<tbody>\n'

        for row in rows:
            table_html += '<tr>\n'
            for cell in row:
                # Format cell content
                cell_html = cell
                cell_html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', cell_html)
                cell_html = re.sub(r'`([^`]+?)`', r'<code>\1</code>', cell_html)
                table_html += f'<td>{cell_html}</td>\n'
            table_html += '</tr>\n'

        table_html += '</tbody>\n</table>'
        return table_html

    html_content = re.sub(r'((?:\|.+\|\n)+)', convert_table, html_content)

    # Paragraphs - wrap text blocks in <p> tags
    def wrap_paragraphs(text):
        lines = text.split('\n')
        result = []
        in_paragraph = False
        in_pre_block = False  # Track if inside <pre> block

        for line in lines:
            stripped = line.strip()

            # Check if entering or exiting a <pre> block
            if '<pre>' in line or '<pre ' in line:
                in_pre_block = True
                if in_paragraph:
                    result.append('</p>')
                    in_paragraph = False
                result.append(line)
                continue
            elif '</pre>' in line:
                in_pre_block = False
                result.append(line)
                continue

            # Skip paragraph processing if inside pre block
            if in_pre_block:
                result.append(line)
                continue

            # Skip empty lines, already converted elements, and special patterns
            if not stripped:
                if in_paragraph:
                    result.append('</p>')
                    in_paragraph = False
                continue

            if stripped.startswith('<'):
                if in_paragraph:
                    result.append('</p>')
                    in_paragraph = False
                result.append(line)
            elif stripped.startswith('___CODE_BLOCK_'):
                # Code block placeholder - don't wrap in p
                if in_paragraph:
                    result.append('</p>')
                    in_paragraph = False
                result.append(line)
            elif re.match(r'^[\d]+\.', stripped):
                if in_paragraph:
                    result.append('</p>')
                    in_paragraph = False
                result.append(line)
            elif stripped.startswith('- ') or stripped.startswith('* '):
                if in_paragraph:
                    result.append('</p>')
                    in_paragraph = False
                result.append(line)
            elif stripped.startswith('|'):
                if in_paragraph:
                    result.append('</p>')
                    in_paragraph = False
                result.append(line)
            else:
                if not in_paragraph:
                    result.append('<p>')
                    in_paragraph = True
                # Add line break if not first line of paragraph
                if result and result[-1] != '<p>':
                    result[-1] = result[-1] + ' ' + stripped
                else:
                    result.append(stripped)

        if in_paragraph:
            result.append('</p>')

        return '\n'.join(result)

    html_content = wrap_paragraphs(html_content)

    # Restore code blocks
    for i, (language, code) in enumerate(code_blocks):
        placeholder = placeholder_template.format(i)
        lang_class = f' class="language-{language}"' if language else ''
        escaped_code = escape_html(code)
        code_html = f'<pre><code{lang_class}>{escaped_code}</code></pre>'
        html_content = html_content.replace(placeholder, code_html)

    # Handle horizontal rules
    html_content = re.sub(r'^---+$', '<hr style="border: none; border-top: 2px solid #e5e7eb; margin: 30px 0;">', html_content, flags=re.MULTILINE)

    # Build complete HTML document
    full_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{main_title}</title>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📚</text></svg>">
    <link rel="shortcut icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📚</text></svg>">
    <style>
        {css}
    </style>
</head>
<body>
    <div class="container">
        <!-- 侧边导航 -->
        <aside class="sidebar">
            <div class="logo">
                <span class="logo-icon">📚</span>
                <span>AI核心概念</span>
            </div>
            <div class="subtitle">
                {doc_position}
            </div>

            <nav>
                <ul class="nav-menu">
                    <li class="nav-item">
                        <a href="#intro" class="nav-link active">📖 概述</a>
                    </li>
{nav_html}
                </ul>
            </nav>
        </aside>

        <!-- 主内容区 -->
        <main class="main-content">
            <!-- 英雄区域 -->
            <section class="hero-section">
                <h1>{main_title}</h1>
                <div class="hero-meta">
                    <div class="meta-item">
                        <span class="meta-icon">🎯</span>
                        <span>学习目标：{learning_goal}</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-icon">👥</span>
                        <span>适合人群：{target_audience}</span>
                    </div>
                </div>
            </section>

            <!-- 内容区域 -->
            <section id="intro" class="content-card">
                {html_content}
            </section>
        </main>
    </div>

    <!-- 返回顶部按钮 -->
    <div class="back-to-top" onclick="scrollToTop()">↑</div>

    <script>
        // 平滑滚动
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{
                        behavior: 'smooth',
                        block: 'start'
                    }});
                }}
            }});
        }});

        // 返回顶部
        function scrollToTop() {{
            window.scrollTo({{
                top: 0,
                behavior: 'smooth'
            }});
        }}

        // 返回顶部按钮显示/隐藏
        const backToTop = document.querySelector('.back-to-top');
        window.addEventListener('scroll', () => {{
            if (window.pageYOffset > 300) {{
                backToTop.classList.add('show');
            }} else {{
                backToTop.classList.remove('show');
            }}
        }});

        // 活动导航链接
        window.addEventListener('scroll', () => {{
            const sections = document.querySelectorAll('section[id]');
            const scrollPosition = window.pageYOffset + 100;

            sections.forEach(section => {{
                const sectionTop = section.offsetTop;
                const sectionHeight = section.offsetHeight;
                const sectionId = section.getAttribute('id');

                if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {{
                    document.querySelectorAll('.nav-link').forEach(link => {{
                        link.classList.remove('active');
                        if (link.getAttribute('href') === `#${{sectionId}}`) {{
                            link.classList.add('active');
                        }}
                    }});
                }}
            }});
        }});
    </script>
</body>
</html>'''

    return full_html

def escape_html(text):
    """Escape HTML special characters"""
    html_escape_table = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
    }
    return ''.join(html_escape_table.get(c, c) for c in text)

def convert_file(md_path, output_path):
    """Convert a single markdown file to HTML"""
    print(f"Converting {md_path}...")

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    css = read_template()
    title = Path(md_path).stem

    html_content = generate_html_from_markdown(md_content, title, css)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"[OK] Converted to {output_path}")

def main():
    """Main conversion function"""
    import sys

    # Check if a specific file is provided as argument
    if len(sys.argv) > 1:
        md_file = Path(sys.argv[1])
        if not md_file.exists():
            print(f"[ERROR] File not found: {md_file}")
            sys.exit(1)

        html_file = md_file.with_suffix('.html')

        print("=" * 60)
        print("Markdown to HTML Converter")
        print("=" * 60)

        try:
            convert_file(md_file, html_file)
            print("=" * 60)
            print("Conversion complete!")
            print("=" * 60)
        except Exception as e:
            print(f"[ERROR] Error converting {md_file.name}: {e}")
            import traceback
            traceback.print_exc()
        return

    # Otherwise, process all files in the default list
    base_path = Path(__file__).parent / "ai" / "03.核心概念知识体系"

    files_to_convert = [
        "01.AI基础层概念详解.md",
        "02.AI应用层核心技术详解.md",
        "03.工程架构层概念详解.md",
        "04.数据与知识层概念详解.md",
        "05.安全与合规层概念详解.md",
        "06.工作方法论与工具链详解.md"
    ]

    print("=" * 60)
    print("Markdown to HTML Converter")
    print("=" * 60)

    for filename in files_to_convert:
        md_path = base_path / filename
        html_path = base_path / filename.replace('.md', '.html')

        if md_path.exists():
            try:
                convert_file(md_path, html_path)
            except Exception as e:
                print(f"[ERROR] Error converting {filename}: {e}")
        else:
            print(f"[ERROR] File not found: {md_path}")

    print("=" * 60)
    print("Conversion complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
