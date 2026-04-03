#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown to HTML Converter
Converts markdown files to HTML with the same styling as AI转型启动会.html
"""

import re
import os
import urllib.request
from pathlib import Path

def read_template():
    """Read the template HTML file to extract styles and structure"""
    # Get project root (script/ -> markdown-convert-html/ -> skills/ -> root)
    project_root = Path(__file__).parent.parent.parent.parent
    template_path = project_root / "ai" / "AI转型启动会.html"
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract CSS from style tag
    css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    css = css_match.group(1) if css_match else ""

    # Clean up leading/trailing whitespace from extracted CSS
    css = css.strip()

    # Append blockquote styles (not in template)
    blockquote_css = """
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
"""

    # Mermaid diagram styles
    mermaid_css = """
/* Mermaid diagrams */
.mermaid {
    background: white;
    padding: 20px;
    border-radius: 8px;
    margin: 20px 0;
    text-align: center;
    min-height: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.mermaid svg {
    max-width: 100%;
    height: auto;
}

/* Mindmap specific styles */
.mermaid .mindmap-node {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
}

pre code.language-mermaid {
    background: white;
    color: #1f2937;
    padding: 0;
    border-radius: 8px;
}
"""

    return css + '\n\n' + blockquote_css + mermaid_css

def download_mermaid_js(target_path):
    """Download mermaid.min.js from CDN to local path

    Args:
        target_path: Path where mermaid.min.js should be saved

    Returns:
        bool: True if download successful, False otherwise
    """
    mermaid_url = "https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.0/mermaid.min.js"

    try:
        # Create parent directory if it doesn't exist
        target_path.parent.mkdir(parents=True, exist_ok=True)

        print(f"[DOWNLOAD] Downloading mermaid.min.js from CDN...")
        print(f"[DOWNLOAD] Target: {target_path}")

        # Download with progress indication
        def show_progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            if total_size > 0:
                percent = min(100, downloaded * 100 / total_size)
                print(f"\r[DOWNLOAD] Progress: {percent:.1f}%", end='', flush=True)

        urllib.request.urlretrieve(mermaid_url, target_path, show_progress)
        print()  # New line after progress

        file_size = target_path.stat().st_size / (1024 * 1024)  # Size in MB
        print(f"[OK] Downloaded mermaid.min.js ({file_size:.1f} MB)")
        return True

    except Exception as e:
        print(f"[ERROR] Failed to download mermaid.min.js: {e}")
        # Clean up partial download if it exists
        if target_path.exists():
            target_path.unlink()
        return False

def generate_html_from_markdown(md_content, title, css, use_local_mermaid=False):
    """Convert markdown content to HTML with full styling

    Args:
        md_content: Markdown content
        title: Document title
        css: CSS styles
        use_local_mermaid: If True, use local mermaid.js instead of CDN
    """

    # Code blocks - process BEFORE other conversions to protect them
    code_blocks = []
    placeholder_template = "___CODE_BLOCK_{}___"
    has_mermaid = False  # Track if page contains mermaid diagrams

    def extract_code_block(match):
        nonlocal has_mermaid
        language = match.group(1) if match.group(1) else ''
        code = match.group(2)
        # Check if this is a mermaid code block
        if language and language.lower() == 'mermaid':
            has_mermaid = True
        idx = len(code_blocks)
        code_blocks.append((language, code))
        return placeholder_template.format(idx)

    # Extract and protect code blocks (support optional leading whitespace)
    # Matches both standard ``` and indented ``` (with spaces/tabs before)
    html_content = re.sub(r'^\s*```(\w*)\n(.*?)\n^\s*```', extract_code_block, md_content, flags=re.DOTALL | re.MULTILINE)

    # Extract metadata from frontmatter
    doc_position = re.search(r'\*\*文档定位：\*\*\s*(.*?)\n', md_content)
    learning_goal = re.search(r'\*\*学习目标：\*\*\s*(.*?)\n', md_content)
    target_audience = re.search(r'\*\*适合人群：\*\*\s*(.*?)\n', md_content)

    doc_position = doc_position.group(1).strip() if doc_position else ""
    learning_goal = learning_goal.group(1).strip() if learning_goal else "见标题"
    target_audience = target_audience.group(1).strip() if target_audience else "所有人"

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

        # Select emoji based on heading content
        emoji = "📚"  # Default

        # Priority matching (check in order)
        if any(keyword in heading for keyword in ["掌握", "目标", "学习"]):
            emoji = "🎯"
        elif any(keyword in heading for keyword in ["详解", "详细", "说明", "介绍"]):
            emoji = "📖"
        elif any(keyword in heading for keyword in ["AI", "智能", "模型", "LLM", "大语言"]):
            emoji = "🤖"
        elif any(keyword in heading for keyword in ["应用", "技术", "开发"]):
            emoji = "⚙️"
        elif any(keyword in heading for keyword in ["工程", "架构", "框架", "系统"]):
            emoji = "🏗️"
        elif any(keyword in heading for keyword in ["数据", "知识", "向量", "数据库"]):
            emoji = "📊"
        elif any(keyword in heading for keyword in ["安全", "合规", "隐私", "防护"]):
            emoji = "🔒"
        elif any(keyword in heading for keyword in ["方法", "工具", "技巧", "实践"]):
            emoji = "🛠️"
        elif any(keyword in heading for keyword in ["概念", "基础", "入门", "原理"]):
            emoji = "💡"
        elif any(keyword in heading for keyword in ["核心", "重要", "关键"]):
            emoji = "⭐"
        elif any(keyword in heading for keyword in ["设计", "模式", "架构"]):
            emoji = "🎨"
        elif any(keyword in heading for keyword in ["测试", "验证", "检查"]):
            emoji = "✅"
        elif any(keyword in heading for keyword in ["问题", "问答", "Q&A", "FAQ"]):
            emoji = "❓"
        elif any(keyword in heading for keyword in ["警告", "注意", "提示"]):
            emoji = "⚠️"
        elif any(keyword in heading for keyword in ["进阶", "前沿", "高级", "深入"]):
            emoji = "🚀"
        elif any(keyword in heading for keyword in ["总结", "回顾", "概览"]):
            emoji = "📝"
        elif any(keyword in heading for keyword in ["环境", "配置", "安装", "部署"]):
            emoji = "🔧"
        elif any(keyword in heading for keyword in ["性能", "优化", "提升"]):
            emoji = "⚡"
        elif any(keyword in heading for keyword in ["示例", "案例", "演示"]):
            emoji = "🎬"
        elif any(keyword in heading for keyword in ["协议", "标准", "规范"]):
            emoji = "📋"
        elif any(keyword in heading for keyword in ["协作", "通信", "交互"]):
            emoji = "🤝"
        elif any(keyword in heading for keyword in ["资源", "参考", "文档"]):
            emoji = "📁"

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

        # Select emoji based on heading content
        emoji = "📚"  # Default

        # Priority matching (check in order)
        if any(keyword in heading for keyword in ["掌握", "目标", "学习"]):
            emoji = "🎯"
        elif any(keyword in heading for keyword in ["详解", "详细", "说明", "介绍"]):
            emoji = "📖"
        elif any(keyword in heading for keyword in ["AI", "智能", "模型", "LLM", "大语言"]):
            emoji = "🤖"
        elif any(keyword in heading for keyword in ["应用", "技术", "开发"]):
            emoji = "⚙️"
        elif any(keyword in heading for keyword in ["工程", "架构", "框架", "系统"]):
            emoji = "🏗️"
        elif any(keyword in heading for keyword in ["数据", "知识", "向量", "数据库"]):
            emoji = "📊"
        elif any(keyword in heading for keyword in ["安全", "合规", "隐私", "防护"]):
            emoji = "🔒"
        elif any(keyword in heading for keyword in ["方法", "工具", "技巧", "实践"]):
            emoji = "🛠️"
        elif any(keyword in heading for keyword in ["概念", "基础", "入门", "原理"]):
            emoji = "💡"
        elif any(keyword in heading for keyword in ["核心", "重要", "关键"]):
            emoji = "⭐"
        elif any(keyword in heading for keyword in ["设计", "模式", "架构"]):
            emoji = "🎨"
        elif any(keyword in heading for keyword in ["测试", "验证", "检查"]):
            emoji = "✅"
        elif any(keyword in heading for keyword in ["问题", "问答", "Q&A", "FAQ"]):
            emoji = "❓"
        elif any(keyword in heading for keyword in ["警告", "注意", "提示"]):
            emoji = "⚠️"
        elif any(keyword in heading for keyword in ["进阶", "前沿", "高级", "深入"]):
            emoji = "🚀"
        elif any(keyword in heading for keyword in ["总结", "回顾", "概览"]):
            emoji = "📝"
        elif any(keyword in heading for keyword in ["环境", "配置", "安装", "部署"]):
            emoji = "🔧"
        elif any(keyword in heading for keyword in ["性能", "优化", "提升"]):
            emoji = "⚡"
        elif any(keyword in heading for keyword in ["示例", "案例", "演示"]):
            emoji = "🎬"
        elif any(keyword in heading for keyword in ["协议", "标准", "规范"]):
            emoji = "📋"
        elif any(keyword in heading for keyword in ["协作", "通信", "交互"]):
            emoji = "🤝"
        elif any(keyword in heading for keyword in ["资源", "参考", "文档"]):
            emoji = "📁"

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

    # Images - convert markdown image syntax to HTML (must be before links)
    def convert_image(match):
        alt = match.group(1)
        src = match.group(2)
        # Convert .md extension to .html in src
        if src.endswith('.md'):
            src = src[:-3] + '.html'
        # Return image tag (will be treated as block-level element in wrap_paragraphs)
        return f'<img src="{src}" alt="{alt}" style="max-width: 100%; height: auto; border-radius: 8px; margin: 20px 0;">'

    html_content = re.sub(r'!\[([^\]]+?)\]\(([^\)]+?)\)', convert_image, html_content)

    # Links - convert .md to .html in href (after images to avoid conflict)
    def convert_link(match):
        text = match.group(1)
        url = match.group(2)
        # Convert .md extension to .html
        if url.endswith('.md'):
            url = url[:-3] + '.html'
        return f'<a href="{url}">{text}</a>'

    html_content = re.sub(r'\[([^\]]+?)\]\(([^\)]+?)\)', convert_link, html_content)

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
        in_blockquote = False  # Track if inside blockquote

        for line in lines:
            stripped = line.strip()

            # Check if entering or exiting a <pre> block
            if '<pre>' in line or '<pre ' in line:
                in_pre_block = True
                if in_paragraph:
                    result.append('</p>')
                    in_paragraph = False
                if in_blockquote:
                    result.append('</blockquote>')
                    in_blockquote = False
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

            # Handle blockquote (lines starting with >)
            if line.startswith('>'):
                # Remove the > prefix and optional space
                quote_content = line[1:].lstrip() if line.startswith('> ') else line[1:].strip()

                if not in_blockquote:
                    if in_paragraph:
                        result.append('</p>')
                        in_paragraph = False
                    result.append('<blockquote>')
                    in_blockquote = True

                result.append(f'<p>{quote_content}</p>')
                continue
            elif in_blockquote and stripped:
                # End blockquote when non-empty, non-quote line encountered
                result.append('</blockquote>')
                in_blockquote = False

            # Skip empty lines, already converted elements, and special patterns
            if not stripped:
                if in_paragraph:
                    result.append('</p>')
                    in_paragraph = False
                if in_blockquote:
                    result.append('</blockquote>')
                    in_blockquote = False
                continue

            if stripped.startswith('<'):
                # Check if this is a block-level tag or inline tag
                block_tags = ['</p>', '<p', '<h1', '<h2', '<h3', '<h4', '<h5', '<h6',
                             '</h1>', '</h2>', '</h3>', '</h4>', '</h5>', '</h6>',
                             '<ul', '</ul>', '<ol', '</ol>', '<li', '</li>',
                             '<table', '</table>', '<thead', '</thead>', '<tbody', '</tbody>',
                             '<tr', '</tr>', '<th', '</th>', '<td', '</td>',
                             '<pre', '</pre>', '<blockquote', '</blockquote>',
                             '<div', '</div>', '<section', '</section>',
                             '<main', '</main>', '<aside', '</aside>', '<nav', '</nav>',
                             '<img', '<hr']  # Add img and hr as block-level elements
                is_block_tag = any(stripped.startswith(tag) for tag in block_tags)

                if is_block_tag:
                    # This is a block-level tag, close current paragraph
                    if in_paragraph:
                        result.append('</p>')
                        in_paragraph = False
                    result.append(line)
                else:
                    # This is an inline tag (like <strong>, <a>, etc.), wrap in paragraph
                    # But close the paragraph after it if it's a complete line
                    if not in_paragraph:
                        result.append('<p>')
                        in_paragraph = True
                    result.append(line)
                    # Check if this line is just an inline tag (like <strong>text</strong> without other text)
                    # If so, close the paragraph to prevent merging with next line
                    if stripped.startswith('<') and not stripped.startswith('</') and '>' in stripped:
                        # This looks like a complete inline tag on its own line
                        # Close the paragraph to prevent merging
                        result.append('</p>')
                        in_paragraph = False
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
        if in_blockquote:
            result.append('</blockquote>')

        return '\n'.join(result)

    html_content = wrap_paragraphs(html_content)

    # Restore code blocks
    for i, (language, code) in enumerate(code_blocks):
        placeholder = placeholder_template.format(i)

        # Special handling for mermaid diagrams
        if language and language.lower() == 'mermaid':
            # Mermaid needs plain text in a div, not in pre/code tags
            code_html = f'<div class="mermaid">{code}</div>'
        else:
            lang_class = f' class="language-{language}"' if language else ''
            escaped_code = escape_html(code)
            code_html = f'<pre><code{lang_class}>{escaped_code}</code></pre>'

        html_content = html_content.replace(placeholder, code_html)

    # Handle horizontal rules
    html_content = re.sub(r'^---+$', '<hr style="border: none; border-top: 2px solid #e5e7eb; margin: 30px 0;">', html_content, flags=re.MULTILINE)

    # Generate mermaid loader script based on whether page has mermaid diagrams
    if has_mermaid:
        if use_local_mermaid:
            # Use local mermaid.js file
            mermaid_loader = """    <!-- Load Mermaid from local assets folder -->
    <script src="./assets/mermaid.min.js"></script>
    <script>
        // Initialize Mermaid when page loads
        document.addEventListener('DOMContentLoaded', function() {
            if (document.querySelectorAll('.mermaid').length === 0) {
                console.log('No mermaid diagrams found');
                return;
            }
            console.log('Initializing mermaid from local file...');

            if (typeof mermaid !== 'undefined') {
                mermaid.initialize({
                    startOnLoad: true,
                    theme: 'default',
                    securityLevel: 'loose',
                    mindmap: {
                        padding: 10,
                        useMaxWidth: true
                    },
                    logLevel: 'debug'
                });
                console.log('Mermaid initialized successfully from local file');
            } else {
                console.error('Local mermaid.js failed to load');
                document.querySelectorAll('.mermaid').forEach(function(el) {
                    el.style.border = '2px solid #f59e0b';
                    el.style.padding = '20px';
                    el.style.background = '#fef3c7';
                    el.innerHTML = '<p style="color: #92400e; margin: 0;"><strong>⚠️ Mermaid 图表加载失败</strong><br>本地文件 ./assets/mermaid.min.js 未找到。</p>';
                });
            }
        });
    </script>"""
        else:
            # Use CDN as fallback
            mermaid_loader = """    <!-- Load Mermaid from CDN (fallback) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.0/mermaid.min.js"></script>
    <script>
        // Initialize Mermaid when page loads
        document.addEventListener('DOMContentLoaded', function() {
            if (document.querySelectorAll('.mermaid').length === 0) {
                console.log('No mermaid diagrams found');
                return;
            }
            console.log('Initializing mermaid from CDN...');

            if (typeof mermaid !== 'undefined') {
                mermaid.initialize({
                    startOnLoad: true,
                    theme: 'default',
                    securityLevel: 'loose',
                    mindmap: {
                        padding: 10,
                        useMaxWidth: true
                    },
                    logLevel: 'debug'
                });
                console.log('Mermaid initialized successfully from CDN');
            } else {
                console.error('Mermaid failed to load from CDN');
                document.querySelectorAll('.mermaid').forEach(function(el) {
                    el.style.border = '2px solid #f59e0b';
                    el.style.padding = '20px';
                    el.style.background = '#fef3c7';
                    el.innerHTML = '<p style="color: #92400e; margin: 0;"><strong>⚠️ Mermaid 图表加载失败</strong><br>请检查网络连接或下载 mermaid.min.js 到本地 assets 文件夹。</p>';
                });
            }
        });
    </script>"""
    else:
        mermaid_loader = '    <!-- No mermaid diagrams in this page -->\n'

    # Build complete HTML document
    full_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{main_title}</title>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📚</text></svg>">
    <link rel="shortcut icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📚</text></svg>">
{mermaid_loader}
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
                        <a href="/" class="nav-link">🏠 返回首页</a>
                    </li>
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
        document.addEventListener('DOMContentLoaded', function() {{
            // 平滑滚动
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
                anchor.addEventListener('click', function (e) {{
                    e.preventDefault();
                    const href = this.getAttribute('href');
                    const targetId = href.substring(1);
                    const target = document.getElementById(targetId);
                    if (target) {{
                        target.scrollIntoView({{
                            behavior: 'smooth',
                            block: 'start'
                        }});
                    }}
                }});
            }});

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
                const headings = document.querySelectorAll('h2[id]');
                const scrollPosition = window.pageYOffset + 100;

                headings.forEach(heading => {{
                    const headingTop = heading.offsetTop;
                    const headingId = heading.getAttribute('id');

                    if (scrollPosition >= headingTop - 50) {{
                        document.querySelectorAll('.nav-link').forEach(link => {{
                            link.classList.remove('active');
                            if (link.getAttribute('href') === '#' + headingId) {{
                                link.classList.add('active');
                            }}
                        }});
                    }}
                }});
            }});
        }});

        // 返回顶部
        function scrollToTop() {{
            window.scrollTo({{
                top: 0,
                behavior: 'smooth'
            }});
        }}
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

def convert_file(md_path, output_path, auto_download=False):
    """Convert a single markdown file to HTML

    Args:
        md_path: Path to markdown file
        output_path: Path to output HTML file
        auto_download: If True, automatically download mermaid.min.js when needed
    """
    print(f"Converting {md_path}...")

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    css = read_template()
    title = Path(md_path).stem

    # Pre-scan markdown to check if it contains mermaid code blocks
    has_mermaid = bool(re.search(r'```mermaid\n', md_content))

    # Only check/download local mermaid.js if the file actually uses mermaid
    use_local_mermaid = False
    if has_mermaid:
        output_dir = Path(output_path).parent
        local_mermaid_path = output_dir / 'assets' / 'mermaid.min.js'

        if local_mermaid_path.exists():
            use_local_mermaid = True
            print(f"[INFO] Using local mermaid.js: {local_mermaid_path}")
        else:
            print(f"[INFO] Markdown contains mermaid diagrams, but local file not found")

            # Auto-download if requested
            if auto_download:
                print(f"[INFO] Auto-downloading mermaid.min.js...")
                if download_mermaid_js(local_mermaid_path):
                    use_local_mermaid = True
                else:
                    print(f"[INFO] Download failed, using CDN as fallback")
            else:
                print(f"[INFO] Using CDN as fallback")
                print(f"[INFO] Tip: Use --download-mermaid flag to download for offline use")
                print(f"[INFO] Or manually download to: {local_mermaid_path}")
    else:
        print(f"[INFO] No mermaid diagrams detected in markdown file")

    html_content = generate_html_from_markdown(md_content, title, css, use_local_mermaid=use_local_mermaid)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"[OK] Converted to {output_path}")

def main():
    """Main conversion function"""
    import sys
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Convert Markdown to HTML with styling')
    parser.add_argument('file', nargs='?', help='Markdown file to convert')
    parser.add_argument('--download-mermaid', action='store_true',
                        help='Automatically download mermaid.min.js when mermaid diagrams are detected')

    args = parser.parse_args()

    # Check if a specific file is provided as argument
    if args.file:
        md_file = Path(args.file)
        if not md_file.exists():
            print(f"[ERROR] File not found: {md_file}")
            sys.exit(1)

        html_file = md_file.with_suffix('.html')

        print("=" * 60)
        print("Markdown to HTML Converter")
        print("=" * 60)

        try:
            convert_file(md_file, html_file, auto_download=args.download_mermaid)
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
