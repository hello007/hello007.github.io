# Complex Test Document

## Features Overview

| Feature | Status | Priority |
|---------|--------|----------|
| Responsive Design | ✅ Complete | High |
| Code Highlighting | ✅ Complete | High |
| Sidebar Navigation | ✅ Complete | Medium |
| Print Styles | ✅ Complete | Low |

## Code Examples

### JavaScript Example

```javascript
function smoothScroll() {
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
}
```

### Python Example

```python
class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        return [item * 2 for item in self.data]

    def validate(self):
        return all(isinstance(x, (int, float)) for x in self.data)
```

## Information Boxes

<div class="info-box">
<h4>💡 Information</h4>
<p>This is an informational box with important details.</p>
</div>

<div class="warning-box">
<h4>⚠️ Warning</h4>
<p>This is a warning box with cautionary information.</p>
</div>

<div class="success-box">
<h4>✅ Success</h4>
<p>This is a success box indicating positive results.</p>
</div>

<div class="highlight-box">
<h4>🎯 Highlight</h4>
<p>This is a highlight box emphasizing key points.</p>
</div>

## Nested Lists

1. First level item
   - Nested item one
   - Nested item two
2. Second level item
   - Another nested item
3. Third level item

## Emphasis and Formatting

This text has **bold** and *italic* formatting. You can also use `inline code` for emphasis.

## Links

Visit [GitHub](https://github.com) for more information.
