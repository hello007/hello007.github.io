#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch convert all markdown files to HTML
"""

import sys
from pathlib import Path

# Import the conversion function
sys.path.insert(0, str(Path(__file__).parent / 'skills' / 'markdown-convert-html' / 'script'))
from convert_md_to_html import convert_file

# 需要转换的文件列表
files_to_convert = [
    'ai/AI转型启动会.md',
    'ai/团队向AI方向转型实操指南.md',
    'ai/03.核心概念知识体系/README.md',
    'ai/03.核心概念知识体系/01.AI基础层概念详解.md',
    'ai/03.核心概念知识体系/02.AI应用层核心技术详解.md',
    'ai/03.核心概念知识体系/03.工程架构层概念详解.md',
    'ai/03.核心概念知识体系/04.数据与知识层概念详解.md',
    'ai/03.核心概念知识体系/05.安全与合规层概念详解.md',
    'ai/03.核心概念知识体系/06.工作方法论与工具链详解.md',
    'ai/03.核心概念知识体系/07.前沿AI概念详解.md',
    'ai/04.Skills/Skills从零到应用指南.md',
    'ai/11.VibeCoding/link.md',
    'ai/21.agent/00-开篇词.md',
    'ai/21.agent/01-第一章-什么是AI-Agent.md',
    'ai/21.agent/02-第二章-Agent的大脑从何而来.md',
    'ai/21.agent/03-第三章-Agent的三大核心支柱.md',
    'ai/21.agent/04-第四章-Agent架构全景图.md',
    'ai/21.agent/05-第五章-LLM如何当Agent的决策大脑.md',
    'ai/21.agent/06-第六章-Agent的记忆秘密.md',
    'ai/21.agent/07-第七章-Agent的手脚怎么长.md',
    'ai/21.agent/08-第八章-多Agent系统.md',
    'ai/21.agent/09-第九章-Agent实战案例库.md',
    'ai/21.agent/10-第十章-构建你的第一个Agent.md',
    'ai/21.agent/11-第十一章-Agent的雷区与边界.md',
    'ai/21.agent/12-第十二章-未来已来.md',
    'ai/21.agent/A-附录-术语对照表.md',
    'ai/31.HarnessEngineering/00-开篇总序.md',
    'ai/31.HarnessEngineering/01-第一章-破题.md',
    'ai/31.HarnessEngineering/02-第二章-正名.md',
    'ai/31.HarnessEngineering/03-第三章-核心辨析.md',
    'ai/31.HarnessEngineering/04-第四章-四大支柱.md',
    'ai/31.HarnessEngineering/05-第五章-工具全景图.md',
    'ai/31.HarnessEngineering/06-第六章-实战五步法.md',
    'ai/31.HarnessEngineering/07-第七章-避坑指南.md',
    'ai/31.HarnessEngineering/08-第八章-全案复盘.md',
    'ai/31.HarnessEngineering/09-第九章-未来趋势.md',
    'ai/31.HarnessEngineering/10-第十章-行动指南.md',
]

def main():
    print("=" * 80)
    print("Batch Markdown to HTML Converter")
    print("=" * 80)
    print(f"Total files to convert: {len(files_to_convert)}")
    print()

    success_count = 0
    fail_count = 0
    failed_files = []

    for i, md_file in enumerate(files_to_convert, 1):
        md_path = Path(md_file)

        if not md_path.exists():
            print(f"[{i}/{len(files_to_convert)}] SKIP: {md_file} (not found)")
            fail_count += 1
            failed_files.append((md_file, "File not found"))
            continue

        try:
            print(f"[{i}/{len(files_to_convert)}] Converting: {md_file}")
            html_path = md_path.with_suffix('.html')
            convert_file(str(md_path), str(html_path))
            print(f"  [OK] Success")
            success_count += 1

        except Exception as e:
            print(f"  [ERROR] Exception: {e}")
            fail_count += 1
            failed_files.append((md_file, str(e)))

        print()

    print("=" * 80)
    print("Conversion Summary")
    print("=" * 80)
    print(f"Success: {success_count}/{len(files_to_convert)}")
    print(f"Failed:  {fail_count}/{len(files_to_convert)}")

    if failed_files:
        print("\nFailed files:")
        for file, error in failed_files:
            print(f"  - {file}")
            print(f"    Error: {error[:100]}")

    print("=" * 80)

    return fail_count == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
