---
title: "第4章：四大框架横向对比 — BMAD vs OpenSpec vs Superpowers vs gstack"
date: 2026-05-15
series: "AI 驱动开发方法论 — BMAD 框架深度解析与实战"
chapter: 4
chapter_type: chapter
tags: [BMAD, OpenSpec, Superpowers, gstack, 框架对比, 规格驱动, TDD, AI工程化, 方法论]
category: AI工程化
prev: "03-BMAD方法实战—从概念到效果的完整演示.md"
next: "05-融合实践—构建AI驱动开发工作流.md"
---

# 第4章：四大框架横向对比 — BMAD vs OpenSpec vs Superpowers vs gstack

在第3章中，我们通过完整的实战演示，直观感受了 BMAD 各核心功能的实际效果——Agent 激活后的角色化交互、Skills 的结构化产出、Checkpoint 的五步审查流程、四阶段工作流的端到端运作，以及三层配置的定制化能力。这些实战体验让我们对 BMAD 的价值主张有了具体的认知。

然而，BMAD 并非 AI 驱动开发方法论的唯一解。在同一时期，至少还有三个框架从不同角度回应了同一个行业痛点——如何让 AI 可控、可重复地参与软件开发。OpenSpec 以"规格驱动开发"（Specification-Driven Development, SDD）为核心范式，主张将规格确立为人类和 AI 共同认可的单一事实来源。Superpowers 以 Claude Code 等 AI 编码工具的高效实践为目标，通过可组合的技能系统和 TDD 纪律，将 AI 编码从"自由发挥"约束为"按流程执行"。gstack 由 YC 总裁兼 CEO Garry Tan 创建，以创业者的产品思维和全能型 AI 工程团队为核心理念，提供从 CEO 级别产品评审到浏览器端 QA 的端到端覆盖。

四个框架，四种设计哲学，四类目标用户。理解它们的异同，不是为了评选"最佳框架"，而是为了在实际项目中做出准确的选型判断——甚至在多数场景下，做出正确的组合决策。本章将从设计哲学、核心架构、能力矩阵、适用场景四个维度，对四大框架进行系统化的横向对比。

## 1 OpenSpec：规格即契约的开放驱动范式

### 1.1 核心理念：规格驱动开发（SDD）

OpenSpec 由 Fission AI 团队构建，其核心理念可以浓缩为一句话：**让规格成为人类和 AI 共同认可的"单一事实来源"（Single Source of Truth）**。在 OpenSpec 的世界观中，AI 编码助手之所以产出不可预测的结果，根本原因在于需求只存在于对话历史的临时上下文中——没有被持久化、没有被结构化、没有被验证。一旦上下文窗口溢出或会话中断，AI 就失去了对"要构建什么"的准确理解。

OpenSpec 的回应方式是在代码和对话之间插入一个轻量级规格层。这个规格层不是传统软件工程中厚重的设计文档，而是一组以 Markdown 文件形式存在的、人类和 AI 都可以直接读写的结构化工件。

### 1.2 四大设计原则

OpenSpec 明确声明了四条设计原则，每一条都蕴含着对传统软件工程方法论的反思性取舍。

**Fluid not rigid — 流动而非僵硬。** 没有阶段门禁，没有必须按顺序完成的步骤。开发者可以在任何时候修改任何工件。这意味着 OpenSpec 不强制执行 BMAD 式的"必需关卡"链——你可以在没有完成 proposal 的情况下直接写 tasks，也可以在实施过程中回头修改 specs。

**Iterative not waterfall — 迭代而非瀑布。** 边构建边学习，边完善。规格不是一次性写完的静态文档，而是随着开发进展不断演化的活文档。这个原则直接回应了传统 SDD 最大的批评——"写规格的时间比写代码还多"。

**Easy not complex — 简单而非复杂。** 轻量级设置，最小仪式感。OpenSpec 的初始化只需要 `npm install -g @fission-ai/openspec@latest` 和 `openspec init` 两条命令。没有复杂的项目结构要求，没有多层次的配置文件。

**Brownfield-first — 棕地优先。** 与现有代码库协作，而不只是面向绿地项目。这是 OpenSpec 与 BMAD 在定位上的一个关键差异。BMAD 的完整工作流（从分析到实施）天然适用于新项目启动；OpenSpec 则更侧重于在已有代码库中引入结构化的变更管理。

### 1.3 核心架构：变更驱动的工作流

OpenSpec 的文件架构围绕"变更"（Change）这一核心概念组织：

```
openspec/
├── specs/              # 事实来源（当前系统行为的规格描述）
└── changes/           # 提议的修改
    ├── add-feature/   # 单个变更文件夹
    ├── fix-bug/       # 另一个变更
    └── archive/       # 已完成的变更归档
```

每个变更文件夹包含四个工件：

| 工件 | 作用 | 对标 BMAD 工件 |
|------|------|---------------|
| `proposal.md` | 意图和范围描述——为什么做，做什么 | 产品简报 / PRD 的概述部分 |
| `specs/` | 变更内容的规格描述——需求和行为定义 | PRD 的详细需求 + UX 规格 |
| `design.md` | 技术方法——怎么做 | 架构决策文档 |
| `tasks.md` | 实施清单——具体步骤 | Epic/Story 清单 |

这个映射关系揭示了一个重要观察：OpenSpec 的四个工件本质上对应了 BMAD 规划阶段的四类输出，但以一种更扁平、更轻量的方式组织。

### 1.4 关键创新：Delta Specs 与场景格式

OpenSpec 最具辨识度的技术创新是 **Delta Specs（差异规格）**。传统规格描述系统当前的全部行为，而 Delta Specs 只描述变更部分——使用 `ADDED`、`MODIFIED`、`REMOVED` 三种操作标记。这种设计的实际价值在于：当系统已有数千行规格文档时，开发者不需要重写整个规格来描述一个新功能，只需要标注差异部分。

在需求描述层面，OpenSpec 采用 `Given/When/Then` 场景格式（源自行为驱动开发 BDD），配合 RFC 2119 关键词（`SHALL`、`MUST`、`SHOULD`）来精确表达需求强度。这种组合在金融行业的合规场景中尤其有价值——审计人员可以通过关键词直接识别哪些是强制要求（`SHALL`/`MUST`），哪些是建议（`SHOULD`）。

### 1.5 工作流：从提议到归档

OpenSpec 的工作流可以概括为五步循环：

```
START CHANGE → CREATE ARTIFACTS → IMPLEMENT TASKS → VERIFY WORK → ARCHIVE CHANGE
```

与 BMAD 的四阶段工作流相比，OpenSpec 的流程更短、更轻量。但它缺少 BMAD 中的"实施就绪检查"这样的质量闸门——在 OpenSpec 中，是否具备足够的规划信息来开始实施，更多依赖开发者的自主判断。

### 1.6 工具兼容性：20+ AI 编码工具

OpenSpec 另一个显著的差异化特征是其广泛的工具兼容性。通过斜杠命令（如 `/opsx:propose`、`/opsx:apply`、`/opsx:archive`），OpenSpec 支持 Claude Code、GitHub Copilot、Gemini CLI、Cursor、OpenCode 等 20 余种 AI 编码工具。这意味着团队不必因为选择 OpenSpec 而锁定特定的 AI 工具供应商。

## 2 Superpowers：技能系统化的高效实践方法论

### 2.1 核心理念：流程纪律重于天赋能力

Superpowers 由 Jesse Vincent 和 Prime Radiant 团队创建，其核心理念可以用创建者的一句话来概括：**"将工作计划做到足够清晰，以至于一个充满热情但缺乏判断力的初级工程师也能遵循执行。"** 这里的"初级工程师"指的正是当前的 AI 编码代理——能力强大但缺乏全局判断力。

Superpowers 的四条哲学原则深刻影响了其设计取舍：

**Test-Driven Development（测试驱动开发）。** 始终先编写测试。这不是建议，而是硬性约束。Superpowers 的 TDD 技能明确要求"删除在测试之前编写的代码"——这种极端表述针对的是 AI 代理的常见倾向：跳过测试直接编写实现代码以尽快展示结果。

**Systematic over ad-hoc（系统化优于临时性）。** 流程优于猜测。当遇到问题时，不是凭直觉尝试各种方案，而是遵循结构化的调试流程。这一原则直接催生了 `systematic-debugging`（系统化调试）技能。

**Complexity reduction（复杂度消减）。** 简单性是首要目标。Superpowers 的设计语言反复强调 YAGNI（You Aren't Gonna Need It）和 DRY（Don't Repeat Yourself），这与 BMAD 中 Winston（架构师）的"Boring technology for stability"原则形成呼应。

**Evidence over claims（证据优于声明）。** 验证前不要宣称成功。这一原则体现在 `verification-before-completion`（完成前验证）技能中——AI 代理必须在完成声明之前，证明问题确实已被解决。

### 2.2 核心机制：Skills（技能）系统

Superpowers 的核心构建块是**技能（Skills）**——以 Markdown 格式编写的可重用 AI 能力单元。每个技能像一份清单（Checklist），确保 AI 编码代理可靠地执行特定流程。

技能的设计哲学有一个关键洞察：**技能添加的是结构而非新能力**。AI 代理本身已经具备编写代码、调试、设计架构的能力；技能的作用是确保这些能力以正确的顺序、在正确的条件下被触发。

### 2.3 核心技能库：全流程覆盖

Superpowers 的技能库按功能分为四组：

**测试类。** `test-driven-development`——强制执行 RED-GREEN-REFACTOR 循环。值得注意的是，该技能包含了一份"测试反模式参考"，列出了 AI 代理常见的测试错误模式（如测试之间的隐式依赖、过度 mock 导致测试失去意义等）。

**调试类。** `systematic-debugging`（4 阶段根因分析）和 `verification-before-completion`（确保问题真正解决）。其中 `systematic-debugging` 的四个阶段——根因追踪（Root-Cause Tracing）、纵深防御（Defense-in-Depth）、条件等待（Condition-Based Waiting）——直接回应了 AI 代理"猜测性调试"的通病。

**协作类。** 这是 Superpowers 技能库中最丰富的类别：`brainstorming`（苏格拉底式设计完善）、`writing-plans`（将工作分解为 2-5 分钟小任务）、`subagent-driven-development`（并行代理工作流）、`executing-plans`（批量执行）、`requesting-code-review`（预审查清单）、`receiving-code-review`（响应审查反馈）、`using-git-worktrees`（并行开发分支）、`finishing-a-development-branch`（完成后合并/PR 决策）。

**元技能。** `writing-skills`（创建新技能）和 `using-superpowers`（技能系统介绍）。`writing-skills` 技能的存在意味着 Superpowers 具备自我扩展能力——团队可以基于统一的技能编写规范，创建适合自身需求的定制化技能。

### 2.4 工作流：从头脑风暴到分支完成

Superpowers 的标准工作流如下：

```
brainstorming → using-git-worktrees → writing-plans → subagent-driven-development / executing-plans → test-driven-development → requesting-code-review → finishing-a-development-branch
```

这个工作流有两个值得深入分析的设计特征。

**第一，"brainstorming"作为入口。** Superpowers 明确要求 AI 代理在看到用户开始构建东西时，**不要**立即跳入编码，而是先退一步通过苏格拉底式提问（Socratic questioning）梳理真实意图。这对应了 BMAD 中分析阶段的探索性工作，但以更轻量的方式实现。

**第二，"subagent-driven-development"的并行执行模型。** 当工作计划足够详细后，Superpowers 会为每个任务分配一个独立的子代理（Subagent），由子代理执行实现，主代理负责两阶段审查——先检查规格合规性（Spec Compliance），再检查代码质量（Code Quality）。这种设计利用了 AI 编码工具的并行能力，使得复杂任务可以在多个子代理间并行推进。

### 2.5 自动触发机制

Superpowers 的一个重要设计决策是**技能的自动触发**。与 BMAD 需要开发者主动选择激活哪个 Agent 和哪个技能不同，Superpowers 的技能通过 Hooks（钩子）机制在特定时间点自动注入上下文。这意味着开发者不需要记住"在什么时候应该调用什么技能"——系统会自动判断当前上下文并激活相关技能。

这个设计取舍体现了两种不同的哲学：BMAD 倾向于**显式控制**（开发者明确知道当前处于什么阶段、哪个 Agent 在工作），Superpowers 倾向于**隐式引导**（系统自动判断并提供正确的结构）。两者各有优劣，我们在第5章的融合实践中将讨论如何结合两者的优势。

## 3 gstack：创业者驱动的全能 AI 工程团队

### 3.1 核心理念：从创始人视角重塑 AI 开发工作流

gstack 由 Y Combinator 总裁兼 CEO Garry Tan 创建，其核心理念根植于创业公司的实战经验：**将一个全能 AI 工程团队装进每个创始人的口袋。** 与 BMAD 的"虚拟产品团队"概念相似，但 gstack 的角色设定更贴近创业公司的实际运作——不是分配 6 个专业角色，而是提供 23 个专精技能，每个技能对应一个具体的工程任务。

gstack 的设计哲学可以用三条原则概括：

**CEO 级产品思维。** gstack 独创的 `/office-hours`（办公时间）和 `/plan-ceo-review`（CEO 评审）技能，将 YC 加速器中"与合伙人对话"的模式内化为 AI 工作流。这意味着 AI 不仅执行编码任务，还参与产品决策层面的审视——从"这个东西用户真的需要吗"到"这个优先级正确吗"。

**真实世界验证。** gstack 的 `/qa`（质量保证）技能会打开真实的 Chromium 浏览器进行测试，而不是依赖模拟器或截图对比。这是所有四个框架中唯一一个执行真实浏览器端测试的——BMAD 的 Checkpoint 是人工审查流程，OpenSpec 的验证依赖开发者自主判断，Superpowers 的 TDD 在代码层面运行。

**多模型协作。** gstack 的 `/codex`（第二意见）技能可以在不同 AI 模型之间获取独立的第二意见，形成交叉验证。这种设计回应了一个实际担忧：如果主要 AI 模型对某个技术决策的判断有偏差，跨模型的第二意见可以提供纠偏信号。

### 3.2 核心机制：Sprint 过程与专精技能

gstack 的核心工作单元是 **Sprint**——一个结构化的 7 步迭代周期：

```
Think（思考）→ Plan（规划）→ Build（构建）→ Review（审查）→ Test（测试）→ Ship（交付）→ Reflect（复盘）
```

这个 Sprint 过程与 BMAD 的四阶段工作流有本质区别。BMAD 的分析→规划→方案设计→实施是一个瀑布式的阶段推进，每个阶段有明确的闸门。gstack 的 Sprint 则是一个可以快速迭代的循环——Think→Reflect 形成闭环，每个 Sprint 结束后自动进入下一个。

gstack 提供 **23 个专精技能**和 **8 个增强工具**，按功能领域分组：

**产品决策类。** `/office-hours`（YC 合伙人风格的产品审视）、`/plan-ceo-review`（CEO 级别优先级评审）、`/reflect`（Sprint 复盘与学习沉淀）。

**设计与前端类。** `/design-shotgun`（生成多个设计变体供选择）、`/design-html`（将设计稿转化为生产级 HTML/CSS）。这两个技能构成了 gstack 独有的设计管线——从概念设计到可交付代码的一站式转换。

**工程执行类。** `/build`（Sprint 构建）、`/review`（代码审查）、`/qa`（浏览器端测试）、`/test`（自动化测试）、`/ship`（交付与部署）。

**安全与治理类。** `/cso`（首席安全官审查）——执行 OWASP Top 10 检查和 STRIDE 威胁建模，这是四个框架中唯一内置安全审计流程的。

**知识管理类。** GBrain——持久化知识库，存储 AI 代理在多次会话中积累的项目知识。这解决了 AI 编码的一个普遍痛点：长会话中的上下文丢失。GBrain 的设计思路与 BMAD 的 `_bmad-output/` 文件持久化有异曲同工之处，但 gstack 更侧重于 AI 代理自身的知识积累。

### 3.3 并行化与规模化能力

gstack 的一个显著差异化特征是 **Conductor（指挥器）**——支持同时运行 10-15 个并行 Sprint。这意味着大型项目可以将功能模块拆分为独立的 Sprint，由不同的 AI 代理并行推进，通过 Conductor 统一协调。

配合 `continuous` 检查点模式（自动 WIP 提交），gstack 在规模化场景下展现出独特的优势：当项目复杂度需要多个并行工作流时，gstack 的 Conductor 提供了比 BMAD 单线程工作流更强的并行处理能力。

### 3.4 工具兼容性：10+ AI 代理

gstack 支持 Claude Code、Codex CLI、Cursor、Factory Droid、Gemini CLI、OpenCode 等 10 余种 AI 编码工具，与 OpenSpec 的跨工具策略一致，而非 BMAD 的 Claude Code 深度绑定策略。

### 3.5 目标用户定位

gstack 的目标用户画像与 BMAD、OpenSpec、Superpowers 有明显差异：

- **创始人 / CEO**——需要快速将产品想法转化为可交付代码，且需要 CEO 级别的产品审视
- **首次使用 Claude Code 的开发者**——gstack 提供开箱即用的技能集，降低入门门槛
- **技术负责人 / Staff 工程师**——需要管理多个并行工作流的规模化 AI 开发

## 4 四大框架的能力矩阵对比

### 4.1 设计哲学对比

四个框架在设计哲学层面的差异，本质上是四个不同问题域的聚焦：

| 维度 | BMAD | OpenSpec | Superpowers | gstack |
|------|------|----------|-------------|--------|
| **核心问题** | 如何让 AI 以专业角色参与软件全生命周期？ | 如何让人类和 AI 对"构建什么"达成一致？ | 如何让 AI 编码代理高效可靠地执行开发任务？ | 如何将一个全能 AI 工程团队装进创始人的口袋？ |
| **设计原点** | 软件交付流程的工程化治理 | 需求与实现之间的契约对齐 | AI 编码行为的纪律约束 | 创业公司的全栈产品开发经验 |
| **关键隐喻** | 虚拟产品团队（6个专业角色） | 活的规格文档（单一事实来源） | 技能清单（确保可靠执行的检查列表） | Sprint 迭代循环（Think→Ship→Reflect） |
| **对 AI 的定位** | 专业协作者（需要角色化和分工） | 契约对齐方（需要共享规格） | 能力强大但需要纪律的初级工程师 | 全能工程团队成员（从产品到测试全覆盖） |
| **核心理念** | 角色化分工 + 流程编排 | 规格驱动开发（SDD） | TDD + 系统化流程 | CEO 产品思维 + 真实世界验证 |

**深层差异分析：** BMAD 假设 AI 需要被赋予明确的专业角色才能提供深度专业判断；OpenSpec 假设 AI 产出的不可预测性源于需求的不明确，因此优先解决"共识"问题；Superpowers 假设 AI 的能力已经足够，问题在于缺乏执行纪律，因此聚焦于"流程约束"；gstack 假设 AI 可以承担从产品决策到浏览器测试的全栈角色，但需要以创业公司的高效迭代模式来组织。四种假设在各自的适用场景中都是成立的——这正是四者互补的理论基础。

### 4.2 架构特征对比

| 维度 | BMAD | OpenSpec | Superpowers | gstack |
|------|------|----------|-------------|--------|
| **组织单元** | Agent（6个角色化智能体） | Change（变更文件夹） | Skill（Markdown 技能文件） | Sprint（7步迭代周期） |
| **能力粒度** | 42 个 Skills + 6 个 Agent | 4 类工件（proposal/specs/design/tasks） | 12 个核心技能 | 23 个专精技能 + 8 个增强工具 |
| **工作流阶段** | 4 阶段（分析→规划→方案设计→实施） | 5 步循环（提议→工件→实施→验证→归档） | 7 步流程（头脑风暴→worktree→计划→执行→TDD→审查→完成） | 7 步循环（Think→Plan→Build→Review→Test→Ship→Reflect） |
| **质量闸门** | 强闸门（实施就绪检查 + Checkpoint） | 弱闸门（依赖开发者自主验证） | 中等闸门（TDD 红-绿-重构 + 代码审查） | 中等闸门（Review + 真实浏览器 QA + /cso 安全审计） |
| **状态追踪** | 文件级元数据（Sprint 状态 YAML + Story 状态字段） | 文件系统（changes/ 目录结构） | Git 分支状态（worktree 管理并行开发） | GBrain 持久知识库 + Conductor 并行协调 |
| **配置系统** | 三层覆盖（基础→团队→个人） | CLI 配置 + profile 选择 | Markdown 技能文件 + Hooks 脚本 | 技能文件 + GBrain 知识配置 |
| **持久化方式** | 文件系统（\_bmad-output/ 目录） | 文件系统（openspec/ 目录） | 文件系统 + Git 工作树 | 文件系统 + Git 自动 WIP 提交 |
| **并行能力** | 单线程工作流 | 单变更线性流程 | 子代理并行执行 | Conductor 支持 10-15 并行 Sprint |

### 4.3 工具生态与兼容性对比

| 维度 | BMAD | OpenSpec | Superpowers | gstack |
|------|------|----------|-------------|--------|
| **主要载体** | Claude Code Skills | npm 包 + 斜杠命令 | Claude Code / Codex / Gemini CLI 插件 | 技能文件（多工具兼容） |
| **安装方式** | 项目级 Skills 安装 | `npm install -g` + `openspec init` | 插件市场安装或 Marketplace 注册 | 技能文件安装 + GBrain 初始化 |
| **支持的 AI 工具** | Claude Code（主要） | 20+ 工具（Claude Code、Copilot、Gemini CLI 等） | Claude Code、Codex CLI、Factory Droid、Gemini CLI、OpenCode、Cursor 等 | Claude Code、Codex CLI、Cursor、Factory Droid、Gemini CLI、OpenCode 等 10+ |
| **扩展机制** | `customize.toml` 三层配置 | 社区 Schema Bundles | `writing-skills` 元技能自建 | 技能文件自定义 + GBrain 知识注入 |
| **初始化仪式** | 中等（需要理解 Agent 体系） | 低（两条命令即可开始） | 低（插件安装后自动生效） | 低（技能开箱即用） |

**关键差异：工具兼容性与集成深度。** OpenSpec、Superpowers 和 gstack 都明确追求跨工具兼容性，而 BMAD 目前主要面向 Claude Code。gstack 在多工具兼容的基础上，还通过 `/codex` 实现跨模型第二意见，在工具生态层面提供了独特的多模型协作能力。

### 4.4 可定制性与扩展性对比

| 维度 | BMAD | OpenSpec | Superpowers | gstack |
|------|------|----------|-------------|--------|
| **定制深度** | 深（Agent 人格、原则、技能菜单均可定制） | 中（工件模板、CLI 配置可调） | 浅（技能文件可修改，但官方不建议贡献新技能） | 中（技能文件可自定义，GBrain 知识可注入） |
| **团队适配** | 强（三层配置系统天然支持团队级定制） | 中（profile 机制支持不同工作模式） | 弱（主要面向个人开发者优化） | 中（Conductor 协调多并行 Sprint，适合小团队） |
| **行业适配** | 强（可注入行业特定原则和合规要求） | 中（可通过 RFC 2119 关键词表达合规强度） | 弱（通用开发方法论，无行业特定设计） | 中（内置 /cso 安全审计，OWASP Top 10 + STRIDE） |
| **扩展贡献** | 支持自定义 Skills 创建 | 支持社区 Schema Bundles | 官方态度保守，不建议贡献新技能 | MIT 开源，技能文件可自由扩展 |

**对金融行业团队的意义：** BMAD 的三层配置系统允许团队在基础框架上叠加金融行业的合规约束（如"银保监合规优先"原则），而不修改框架源文件。OpenSpec 的 RFC 2119 关键词体系（`MUST`/`SHALL`/`SHOULD`）在需求表达层面提供了合规强度的精确标记。gstack 的 `/cso` 安全审计技能直接覆盖 OWASP Top 10 和 STRIDE 威胁建模，在安全层面提供了开箱即用的行业级检查。Superpowers 目前没有行业特定的适配机制。

## 5 适用场景分析

### 5.1 各框架的最佳适用场景

**BMAD 最适合：中大型项目的结构化交付。** 当项目需要从需求分析走到编码实现的完整流程，且团队希望在 AI 参与的每个阶段设置质量闸门时，BMAD 的四阶段工作流和检查点机制提供了最强的流程控制力。典型场景包括：

- 新产品或新模块的从零启动
- 需要完整文档链（PRD→UX→架构→Story）的金融级项目
- 多人协作的 AI 辅助开发，需要明确的角色分工和工件管理
- 对开发过程可审计性有合规要求的场景

**OpenSpec 最适合：既有系统的迭代开发与需求管理。** 当项目已经存在代码库，需要在不破坏既有结构的前提下引入结构化的变更管理时，OpenSpec 的棕地优先设计和 Delta Specs 机制提供了最平滑的接入路径。典型场景包括：

- 存量系统的功能迭代和缺陷修复
- 团队使用多种 AI 编码工具，需要统一的规格上下文
- 需求变更频繁，规格需要快速迭代更新的场景
- 多人团队需要围绕"当前系统行为"建立共享认知

**Superpowers 最适合：个人开发者或小团队的高效编码执行。** 当开发者的主要痛点不是"如何规划"而是"如何让 AI 更可靠地编码"时，Superpowers 的 TDD 纪律、系统化调试和自动触发的技能系统提供了最强的执行保障。典型场景包括：

- 个人开发者使用 Claude Code 进行日常编码
- 需要快速验证想法的原型开发
- TDD 文化已经建立的团队，希望 AI 遵循相同的纪律
- 需要并行子代理加速开发的大型编码任务

**gstack 最适合：创业团队的全栈产品开发。** 当团队需要从产品构思到可交付代码的快速迭代，且希望 AI 参与产品决策层面时，gstack 的 Sprint 循环、CEO 级产品审视和真实浏览器 QA 提供了最贴近创业公司节奏的开发体验。典型场景包括：

- 创业团队从零构建产品的快速迭代
- 需要产品级 UI/UX 设计和前端开发的场景（design-shotgun + design-html 管线）
- 需要多并行 Sprint 推进多个功能模块的规模化开发
- 对安全性有要求的项目（/cso 安全审计）
- 需要跨模型第二意见降低决策偏差的场景（/codex）

### 5.2 场景选型决策矩阵

以下决策矩阵帮助开发者根据项目特征快速定位最合适的框架（或框架组合）：

| 项目特征 | 推荐框架 | 理由 |
|---------|---------|------|
| 新项目，需要完整从需求到代码的流程 | BMAD | 四阶段工作流提供完整的结构化交付路径 |
| 存量项目，需要引入结构化变更管理 | OpenSpec | 棕地优先设计 + Delta Specs 的增量描述 |
| 个人开发者，希望 AI 编码更可靠 | Superpowers | 自动触发技能 + TDD 纪律，零仪式感 |
| 创业团队，需要快速产品迭代 | gstack | Sprint 循环 + CEO 级产品审视 + 真实浏览器 QA |
| 金融级项目，需要合规可审计 | BMAD + OpenSpec | BMAD 的流程控制 + OpenSpec 的 RFC 2119 合规标记 |
| 多工具团队，需要统一规格层 | OpenSpec | 20+ 工具兼容性，跨工具统一规格 |
| 大型编码任务，需要并行执行 | gstack / Superpowers | gstack 的 Conductor 10-15 并行 Sprint；Superpowers 的 subagent 并行工作流 |
| 需要从规划到实施的全链路质量保障 | BMAD | 实施就绪检查 + Checkpoint 双重闸门 |
| 需求频繁变更，规格需要快速迭代 | OpenSpec | 流动性设计，无阶段门禁 |
| 需要 UI/UX 设计到代码的一站式转换 | gstack | design-shotgun 多方案生成 + design-html 生产级代码转换 |
| 对安全性有高要求的项目 | gstack + BMAD | gstack 的 /cso 安全审计（OWASP + STRIDE）+ BMAD 的合规定制层 |

## 6 四者的互补关系：不是替代，而是组合

### 6.1 互补的理论基础

四个框架并非互斥的竞争关系，而是覆盖 AI 驱动开发不同侧面的互补体系。这种互补性可以通过一个四维模型来理解：

```
          流程编排（Process Orchestration）
                 ↑
                 |
            BMAD ●
                 |
                 |
  规格共识 ●————+————● 执行纪律       ● 全栈产品化
  (OpenSpec)     |     (Superpowers)   (gstack)
                 |
                 ↓
```

**BMAD 占据"流程编排"维度的高地。** 它解决的核心问题是"谁在什么时间做什么"——通过 Agent 角色化分工和 Workflow 阶段编排，确保 AI 开发流程的有序性。当你需要一个完整的从需求到代码的结构化交付流程时，BMAD 是最成熟的选择。

**OpenSpec 占据"规格共识"维度的高地。** 它解决的核心问题是"人类和 AI 对构建什么是否达成一致"——通过结构化的规格工件和 Delta Specs 机制，确保需求理解的准确性。当你需要在多工具环境中建立共享的规格上下文时，OpenSpec 是最实用的选择。

**Superpowers 占据"执行纪律"维度的高地。** 它解决的核心问题是"AI 编码代理是否能可靠地执行已定义的任务"——通过 TDD 循环、系统化调试和自动触发的技能系统，确保编码执行的质量。当你需要让 AI 编码行为遵循工程纪律时，Superpowers 是最高效的选择。

**gstack 占据"全栈产品化"维度的高地。** 它解决的核心问题是"如何将 AI 的能力从编码执行提升到产品级交付"——通过 CEO 级产品审视、真实浏览器 QA、安全审计和设计管线，将 AI 从编码工具提升为产品开发伙伴。当你需要 AI 参与从产品决策到可交付产品的全流程时，gstack 提供了最完整的覆盖。

### 6.2 互补的具体切入点

四个框架之间存在多个天然的互补切入点：

**BMAD + OpenSpec：规格层的统一。** BMAD 的规划阶段产出 PRD、UX 规格、架构决策文档和 Epic/Story 清单，这些工件可以映射为 OpenSpec 的 proposal、specs、design 和 tasks 四类工件。通过这种映射，BMAD 的规划产出可以被 OpenSpec 的规格层持久化管理，使得后续的变更可以通过 Delta Specs 进行增量描述，而不需要重新运行 BMAD 的完整规划流程。

**BMAD + Superpowers：实施阶段的纪律增强。** BMAD 的实施阶段由 Amelia（开发者 Agent）通过 `dev-story` 技能执行，采用红-绿-重构循环。Superpowers 的 `test-driven-development` 技能提供了更详细的 TDD 约束（包含测试反模式参考），`systematic-debugging` 揀供了 BMAD 没有覆盖的 4 阶段根因分析流程。将 Superpowers 的执行纪律注入 BMAD 的实施阶段，可以显著提升编码质量。

**OpenSpec + Superpowers：规格驱动的可靠执行。** OpenSpec 定义了"构建什么"，Superpowers 约束了"怎么构建"。OpenSpec 的 tasks.md 工件可以直接作为 Superpowers `writing-plans` 技能的输入，将结构化的任务清单转化为 2-5 分钟的原子化执行步骤，然后通过 `subagent-driven-development` 并行执行。

**gstack + BMAD：产品思维与流程治理的结合。** gstack 的 `/office-hours` 和 `/plan-ceo-review` 可以为 BMAD 的分析和规划阶段注入产品层面的审视，而 BMAD 的 Checkpoint 机制可以为 gstack 的 Sprint 循环增加更严格的质量闸门。gstack 的 `/cso` 安全审计可以补充 BMAD 在安全领域的专项检查。

**gstack + Superpowers：全栈产品化与执行纪律的融合。** gstack 提供了从产品决策到设计管线的全栈覆盖，但编码执行层面的纪律约束不如 Superpowers 精细。将 Superpowers 的 TDD 纪律和系统化调试注入 gstack 的 Build→Review→Test 阶段，可以在保持产品视角的同时提升代码质量。

**四者融合：完整的 AI 驱动开发闭环。** 理想的融合路径是：使用 BMAD 的 Agent 体系和 Workflow 进行全生命周期的流程编排，使用 OpenSpec 的规格层建立持久的"单一事实来源"和跨工具的规格共享，使用 Superpowers 的执行纪律约束 AI 编码代理的实施行为，使用 gstack 的产品思维和全栈能力覆盖从产品决策到真实浏览器验证的完整交付链。这种融合不是简单的功能叠加，而是在四个维度上同时获得最佳实践。

### 6.3 融合的边界条件

互补并不意味着在所有场景下都需要四者并用。融合的边界条件取决于项目特征：

- **小型项目**（个人开发者，快速原型）：Superpowers 或 gstack 独立使用即可满足需求
- **中型项目**（2-5 人团队，既有代码库迭代）：OpenSpec + Superpowers 组合提供规格管理和执行纪律
- **创业项目**（小团队快速产品迭代）：gstack 独立使用或 gstack + Superpowers 增强执行纪律
- **大型项目**（5+ 人团队，新系统或重大重构）：BMAD + OpenSpec + Superpowers + gstack 四者融合，覆盖从规划到实施的完整需求
- **合规敏感项目**（金融、医疗等行业）：BMAD + OpenSpec + gstack 组合，利用 BMAD 的流程可审计性、OpenSpec 的 RFC 2119 合规标记和 gstack 的 /cso 安全审计

## 7 本章小结与下章预告

本章完成了 BMAD、OpenSpec、Superpowers、gstack 四大框架的系统性横向对比。关键结论如下：

**设计哲学的差异反映了问题域的聚焦。** BMAD 聚焦"流程编排"，通过角色化 Agent 和结构化 Workflow 解决 AI 参与全生命周期的有序性问题。OpenSpec 聚焦"规格共识"，通过 SDD 范式和 Delta Specs 解决人类与 AI 的需求对齐问题。Superpowers 聚焦"执行纪律"，通过 TDD 和系统化技能解决 AI 编码行为的可靠性问题。gstack 聚焦"全栈产品化"，通过 CEO 级产品思维、真实浏览器 QA 和安全审计解决 AI 从编码工具到产品开发伙伴的跨越问题。四者不是竞争关系，而是互补关系。

**能力矩阵揭示了各自的强项与盲区。** BMAD 强在结构化交付流程和质量闸门，但在跨工具兼容性方面受限。OpenSpec 强在开放规格驱动和广泛的工具兼容性，但缺乏强有力的质量闸门机制。Superpowers 强在执行纪律和自动触发的技能系统，但在团队级定制和行业适配方面较浅。gstack 强在产品级覆盖（设计管线、浏览器 QA、安全审计、并行 Sprint），但在深度定制和大型团队治理方面不如 BMAD 成熟。

**四者的组合价值大于单一框架的独立价值。** BMAD 的规划产出可以映射为 OpenSpec 的规格工件，OpenSpec 的任务清单可以作为 Superpowers 执行计划的输入，Superpowers 的 TDD 纪律可以增强 BMAD 实施阶段的编码质量，gstack 的产品思维和安全审计可以补充其他三个框架在产品决策和安全领域的不足。这种互补关系为下一章的融合实践奠定了理论基础。

在下一章中，我们将从理论走向实践——具体展示如何构建一个融合四大框架优势的 AI 驱动开发工作流。我们将讨论映射策略（BMAD 工件如何对应 OpenSpec 规格）、注入策略（Superpowers 技能如何集成到 BMAD 实施阶段）、产品化策略（gstack 的 Sprint 循环和产品审视如何融入整体流程）以及端到端的融合工作流设计。
