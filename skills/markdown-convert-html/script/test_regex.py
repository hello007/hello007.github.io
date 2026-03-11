#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

test_md = '''```java
// 传统编程：你要明确告诉计算机每一步怎么做
public String generateGreeting(String name) {
    return "Hello, " + name + "!"; // 确定性输出
}
```'''

print("Test markdown:")
print(test_md)
print("\n" + "="*50 + "\n")

# Test pattern 1
pattern1 = r'```(\w*)\n(.*?)\n```'
matches1 = re.findall(pattern1, test_md, flags=re.DOTALL)
print(f"Pattern 1: {pattern1}")
print(f"Matches: {matches1}")
print()

# Test pattern 2 - without language
test_md2 = '''```
好的Prompt = 好的输出
差的Prompt = 差的输出
```'''

print("Test markdown 2:")
print(test_md2)
print("\n" + "="*50 + "\n")

matches2 = re.findall(pattern1, test_md2, flags=re.DOTALL)
print(f"Pattern 1 on md2:")
print(f"Matches: {matches2}")
print()

# Test pattern 3 - using [^`]+
pattern3 = r'```(\w*)\n([^`]+)\n```'
matches3 = re.findall(pattern3, test_md, flags=re.DOTALL)
print(f"Pattern 3: {pattern3}")
print(f"Matches on md1: {matches3}")
print()

matches3b = re.findall(pattern3, test_md2, flags=re.DOTALL)
print(f"Pattern 3 on md2:")
print(f"Matches: {matches3b}")
