# All In AI

> AI 转型实践指南与资源分享

本站点是关于团队 AI 转型的实践指南和宣贯材料，旨在帮助团队顺利实现 AI 方向的转型。

## 📄 内容概览

### 🎯 团队转型指南

#### [AI 转型启动会](./ai/AI转型启动会.html)

AI 转型项目的启动会议材料，用于团队宣贯和目标对齐。

**主要内容：**

- AI 转型的背景与意义
- 转型目标与预期成果
- 实施计划与时间节点
- 团队协作与分工

#### [团队向 AI 方向转型实操指南](./ai/团队向AI方向转型实操指南.html)

详细的团队 AI 转型实施指南，包含转型策略、实施步骤、最佳实践等内容。

**主要内容：**

- AI 转型规划与路线图
- 团队能力建设方案
- 技术选型与工具推荐
- 实施过程中的注意事项

### 💡 转型经验分享

#### [从 Java 架构师到 AI 技术专家：我的转型之路（虚构版）](./ai/AI转型之路.html)

一线架构师的真实转型历程记录：18个月从传统 Java 开发到 AI 技术专家的完整心路历程、学习路径和实战经验。

**主要内容：**

- 转型背景与动机
- 技术学习路径
- 实战案例分享
- 经验总结与反思
- 9个完整章节

### 🎮 VibeCoding 学习资源

#### [VibeCoding 项目链接汇总](./ai/11.VibeCoding/link.html)

汇总 5 个核心 VibeCoding 开源项目，按难度从易到难排序，提供完整学习路径推荐。

**包含项目：**

- **easy-vibe** - 零基础 AI 编程教育课程
- **AICodingGuide** - AI 编程实战指南（工具使用）
- **awesome-vibe-coding** - Vibe Coding 工具资源列表
- **vibe-coding-cn** - Vibe Coding 中文指南（方法论深入）
- **aicodeguide** - AI 辅助编程全面指南（系统化理论）

**学习路径：**

- 路径 A：完全零基础（3-6 个月系统化学习）
- 路径 B：有编程基础（1-2 个月快速通道）
- 路径 C：团队转型（3 个月计划）

### 📚 核心概念知识体系

#### [核心概念知识体系总览](./ai/03.核心概念知识体系/README.html)

从基础到应用、从理论到实践的完整 AI 知识体系，涵盖 7 个核心模块，系统化学习 AI 应用开发所需的核心概念。

**七大核心模块：**

1. [AI 基础层概念详解](./ai/03.核心概念知识体系/01.AI基础层概念详解.html) - LLM、Prompt、Token、Embedding 等核心概念
2. [AI 应用层核心技术详解](./ai/03.核心概念知识体系/02.AI应用层核心技术详解.html) - RAG、向量数据库、Agent、Function Calling
3. [工程架构层概念详解](./ai/03.核心概念知识体系/03.工程架构层概念详解.html) - LangChain4j、Spring AI、性能优化
4. [数据与知识层概念详解](./ai/03.核心概念知识体系/04.数据与知识层概念详解.html) - 文档分块、数据清洗、知识库构建
5. [安全与合规层概念详解](./ai/03.核心概念知识体系/05.安全与合规层概念详解.html) - Prompt Injection 防护、数据隐私
6. [工作方法论与工具链详解](./ai/03.核心概念知识体系/06.工作方法论与工具链详解.html) - Prompt-First 开发、Cursor 使用
7. [前沿 AI 概念详解](./ai/03.核心概念知识体系/07.前沿AI概念详解.html) - Prompt Engineering、Context Engineering、MCP 协议

**学习计划：**

- 3 个月系统化学习路径
- 适合 3-10 人 Java 技术团队
- 每周 2-3 个主题，理论与实践结合

## 📦 项目结构

```text
hello007.github.io/
├── _config.yml                        # Jekyll 配置文件
├── index.html                         # 网站首页（导航卡片）
├── README.md                          # 项目说明
├── .claude/                           # Claude Code 配置
│   ├── CLAUDE.md                     # 项目指南
│   ├── rules/                         # 规则文件
│   │   └── md2html.md               # Markdown转HTML规则
│   └── settings.local.json            # 本地设置
├── skills/                            # Claude 技能定义
│   └── markdown-convert-html/         # Markdown转HTML转换技能
│       ├── script/                    # 脚本目录
│       │   ├── convert_md_to_html.py # 主转换工具
│       │   ├── test_regex.py         # 测试脚本
│       │   └── test_process.py       # 测试脚本
│       ├── SKILL.md                   # 技能说明（中文）
│       ├── SKILL_en.md                # 技能说明（英文）
│       ├── README.md                  # 技能文档
│       └── evals/                    # 测试用例
└── ai/                                # AI 转型相关页面
    ├── 团队向AI方向转型实操指南.md/html
    ├── AI转型启动会.md/html
    ├── AI转型之路.md/html
    ├── 11.VibeCoding/
    │   └── link.md/html              # VibeCoding项目链接汇总
    └── 03.核心概念知识体系/
        ├── README.md/html              # 总览页面
        ├── 01.AI基础层概念详解.md/html
        ├── 02.AI应用层核心技术详解.md/html
        ├── 03.工程架构层概念详解.md/html
        ├── 04.数据与知识层概念详解.md/html
        ├── 05.安全与合规层概念详解.md/html
        ├── 06.工作方法论与工具链详解.md/html
        └── 07.前沿AI概念详解.md/html
```

## 🛠️ 技术栈

- **静态托管**: GitHub Pages (Jekyll minimal theme)
- **内容管理**: Markdown + 自定义 Python 转换工具
- **设计系统**: 响应式布局，支持移动端
- **AI 工具**: Claude Code（开发效率工具）
- **协作系统**: Claude Skills（可复用技能库）

## 🌐 在线访问

- **GitHub Pages**: [https://hello007.github.io](https://hello007.github.io)
- **在线预览**: [https://hello007.github.io/](https://hello007.github.io)

## 🚀 快速开始

### 本地预览

```bash
# 克隆仓库
git clone https://github.com/hello007/hello007.github.io.git

# 进入目录
cd hello007.github.io

# 启动 Jekyll 本地服务器
bundle exec jekyll serve

# 访问 http://localhost:4000
```

### 转换 Markdown 文件

```bash
# 转换指定文件
python skills/markdown-convert-html/script/convert_md_to_html.py "path/to/file.md"

# 转换所有默认文件
python skills/markdown-convert-html/script/convert_md_to_html.py
```

## 📝 更新日志

- **2026-03-15**:
  - 新增 VibeCoding 学习资源（5个项目链接汇总）
  - 添加核心概念知识体系（7大模块）
  - 添加 AI 转型之路（虚构版）
  - 优化网站首页布局，添加分类导航
  - 修复导航跟踪功能
  - 添加返回首页链接
- **2025-03**: 初始化项目，添加 AI 转型相关文档页面

## 📧 联系方式

如有问题或建议，欢迎通过 [Issues](https://github.com/hello007/hello007.github.io/issues) 反馈。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 📄 许可证

**License**: MIT © [hello007](https://github.com/hello007)

---

