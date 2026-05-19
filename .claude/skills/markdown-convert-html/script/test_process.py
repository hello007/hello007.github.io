#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

# Simulate the process_paragraphs function
def process_paragraphs(content):
    lines = content.split('\n')
    results = []
    in_paragraph = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        print(f"Line {i}: '{stripped[:50]}...' if len(stripped) > 50 else '{stripped}'")

        # Check condition
        starts_with_lt = stripped.startswith('<')
        has_special_tag = any(tag in stripped for tag in ['<h', '<pre', '<ul', '<ol', '<li', '<table', '<div', '<block'])
        condition = not stripped or (starts_with_lt and has_special_tag)

        print(f"  starts_with '<': {starts_with_lt}, has_special_tag: {has_special_tag}, condition: {condition}")

        if condition:
            if in_paragraph:
                results.append('</p>')
                in_paragraph = False
            if stripped:
                results.append(line)
        elif stripped.startswith('```'):
            if in_paragraph:
                results.append('</p>')
                in_paragraph = False
            results.append(line)
        else:
            if not in_paragraph:
                results.append('<p>')
                in_paragraph = True
            results.append(line)

    if in_paragraph:
        results.append('</p>')

    return '\n'.join(results)


test_content = '''<pre><code>好的Prompt = 好的输出
差的Prompt = 差的输出</code></pre>'''

print("Input:")
print(test_content)
print("\n" + "="*60 + "\n")

result = process_paragraphs(test_content)

print("\n" + "="*60 + "\n")
print("Output:")
print(result)
