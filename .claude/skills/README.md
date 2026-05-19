# Project Skills

This directory contains project-level Claude skills.

## 📁 Available Skills

### markdown-convert-html
Converts markdown files to beautiful, responsive HTML pages with sidebar navigation, styled content cards, code highlighting, and professional design.

**Location:** `skills/markdown-convert-html/`

**Features:**
- ✅ Responsive layout with sticky sidebar navigation
- ✅ Card-based content organization
- ✅ Syntax-highlighted code blocks (dark theme)
- ✅ Styled tables and typography
- ✅ Multiple content box styles (info, warning, success, highlight)
- ✅ Smooth scrolling and back-to-top button
- ✅ Chinese font optimization
- ✅ Mobile-responsive design
- ✅ Print-friendly styles

## 🚀 How to Use

### Using the Skill

When working in this project, you can use the markdown-convert-html skill by saying things like:

- "Convert this markdown file to HTML"
- "将这个 markdown 文件转换为 HTML"
- "Create a web page from this markdown"
- "Generate HTML from the markdown file"

### Example Usage

```bash
# Example: Convert a markdown file
"Convert README.md to HTML"
"将 docs/API.md 转换为 HTML 页面"
```

## 📂 Skill Structure

```
markdown-convert-html/
├── script/                    # Scripts directory
│   ├── convert_md_to_html.py  # Main conversion tool
│   ├── test_regex.py          # Regex testing script
│   └── test_process.py        # Paragraph processing test
├── SKILL.md                   # Skill instructions (Chinese)
├── SKILL_en.md                # Skill instructions (English)
├── README.md                  # This file
└── evals/                     # Test cases
    ├── evals.json            # Test case definitions
    ├── test-simple.md        # Simple test file
    ├── test-complex.md       # Complex test with tables, code blocks
    └── test-chinese.md       # Chinese content test
```

## 🔧 Development

### Using the Python Tool

The conversion can also be done directly using the Python script:

```bash
# Convert a specific file
python skills/markdown-convert-html/script/convert_md_to_html.py "path/to/file.md"

# Convert all default files
python skills/markdown-convert-html/script/convert_md_to_html.py
```

### Testing the Conversion

Test the conversion logic:

```bash
# Test code block regex patterns
python skills/markdown-convert-html/script/test_regex.py

# Test paragraph wrapping logic
python skills/markdown-convert-html/script/test_process.py
```

### Modifying the Skill

To customize the skill behavior, edit the `SKILL.md` file:

```bash
# Edit the skill configuration
code skills/markdown-convert-html/SKILL.md
```

### Testing the Skill

Test files are available in the `evals/` directory:

```bash
# Test with simple markdown
"Convert evals/test-simple.md to HTML"

# Test with complex content
"Convert evals/test-complex.md to HTML"

# Test with Chinese content
"将 evals/test-chinese.md 转换为 HTML"
```

## 📝 Output

The skill generates complete HTML5 files with:
- Embedded CSS (no external dependencies)
- Responsive design
- Interactive JavaScript features
- UTF-8 encoding for Chinese support
- Print-friendly styles

Output files are saved with the same name as the input markdown file, but with `.html` extension.

## 🎨 Customization

### Changing Colors

Edit the CSS color variables in `SKILL.md`:
- Primary: `#2563eb` (blue)
- Background: `#f5f7fa` (light gray)
- Accent gradients: `#667eea` to `#764ba2`

### Modifying Layout

Adjust the layout structure in the skill instructions to customize:
- Sidebar width
- Content padding
- Responsive breakpoints
- Font sizes

## 📊 Test Results

The skill has been tested with:
- ✅ Simple markdown files
- ✅ Complex documents with tables and code
- ✅ Chinese content
- ✅ Nested lists and emphasis
- ✅ Links and images
- ✅ Multiple heading levels

## 🤝 Contributing

To improve this skill:
1. Test it with various markdown files
2. Identify edge cases or issues
3. Modify `SKILL.md` accordingly
4. Test changes with the eval files

## 📄 License

This skill is part of the project and follows the same license.
