---
title: "第2章：BMAD 核心概念体系深度拆解"
date: 2026-05-15
series: "AI 驱动开发方法论 — BMAD 框架深度解析与实战"
chapter: 2
chapter_type: chapter
tags: [BMAD, Agent, Skills, Workflow, Checkpoint, AI工程化, 角色化智能体]
category: AI工程化
prev: "01-AI辅助开发演进与BMAD诞生.md"
next: "03-BMAD方法实战—从概念到效果的完整演示.md"
---

# 第2章：BMAD 核心概念体系深度拆解

在上一章中，我们建立了理解 BMAD 的认知基座：它不是一个提示词模板库，而是一套让 AI 以专业角色参与软件全生命周期的工程化方法论。我们梳理了其核心设计哲学——"专业分工的 Agent + 可组合的 Skills + 结构化的 Workflow + 检查点质量闸门"四位一体架构。本章将从设计哲学进入实现细节，逐一拆解这四大支柱的内部构造，并揭示它们之间的三维协同机制。

理解这些概念不是为了记忆清单，而是为了掌握一套**可推理的工程框架**——当你面对一个具体的项目场景时，能够准确判断应该激活哪个 Agent、编排哪些 Skills、在哪个 Checkpoint 设置审查闸门。

## 1 Agent 智能体体系：六位专业协作者

BMAD 的 Agent 体系是整个框架中最具辨识度的设计。六个角色化智能体——Mary、John、Sally、Winston、Amelia、Paige——分别对应软件开发中的六个专业角色。但它们绝不仅是六个不同的提示词模板。每个智能体拥有独立的方法论根基、行为准则、技能菜单和持久上下文，构成了一套**深度角色化的专业分工体系**。

### 1.1 Agent 的结构化定义

从源码层面看，每个 Agent 由 `SKILL.md`（行为协议）和 `customize.toml`（配置定义）两个核心文件构成。SKILL.md 定义了 Agent 的激活流程——从配置解析、人格采纳、持久事实加载到菜单分发，共八个标准步骤。customize.toml 则定义了 Agent 的灵魂：

| 配置维度 | 作用 | 示例（Winston/架构师） |
|---------|------|----------------------|
| `identity` | 方法论根基 | Martin Fowler 实用主义 + Werner Vogels 云规模思想 |
| `role` | 职责边界 | 将 PRD 和 UX 转化为技术架构决策 |
| `communication_style` | 表达风格 | 冷静务实，以权衡替代裁决 |
| `principles` | 行为准则（数组） | "三次重复再抽象"、"无聊技术保稳定"、"开发者生产力即架构" |
| `persistent_facts` | 持久上下文 | `file:{project-root}/**/project-context.md` |
| `menu` | 可调度技能列表 | CA（创建架构）、IR（实施就绪检查） |

**关键设计细节：** `persistent_facts` 是 Agent 的长期记忆锚点。每个 Agent 默认加载 `project-context.md` 文件作为全局上下文。这意味着无论当前对话讨论什么主题，Agent 始终掌握项目的基本技术栈、编码规范和架构约束。这正是解决第1章所述"上下文丢失"问题的工程手段——关键信息不依赖对话历史传递，而是通过文件系统持久化并按需加载。

### 1.2 六个角色的职责边界与协作关系

六个 Agent 按其在工作流中的活跃阶段，自然形成了上下游的协作链：

| Agent | 角色 | 活跃阶段 | 核心职责 | 方法论根基 | 可用技能（详见速查表） |
|-------|------|---------|---------|-----------|---------|
| Mary | 业务分析师 | 分析 | 市场研究、竞品分析、需求引导 | Porter 战略模型 + Minto 金字塔原理 | BP、MR、DR、TR、CB、WB、DP（7个） |
| John | 产品经理 | 规划 | PRD 创建/验证、Epic 拆分、实施就绪 | Marty Cagan + Teresa Torres 思维 | CP、VP、EP、CE、IR、CC（6个） |
| Sally | UX 设计师 | 规划 | UX 设计规格 | Don Norman 人本设计 + Cooper 角色模型 | CU（1个） |
| Winston | 系统架构师 | 方案设计 | 技术架构决策 | Fowler 实用主义 + Vogels 云规模思想 | CA、IR（2个） |
| Amelia | 高级工程师 | 实施 | Story 实现、代码审查、Sprint 管理 | Kent Beck TDD + 红-绿-重构 | DS、QD、QA、CR、SP、CS、ER（7个） |
| Paige | 技术文档专家 | 全阶段 | 文档生成、图表绘制、概念解释 | Julia Evans 可读性 + Tufte 视觉精确性 | DP、WD、MG、VD、EC（5个） |

这张表格揭示了一个重要的设计规律：**Agent 的技能数量与其职责广度正相关，而非与权力层级正相关。** Mary（分析师）和 Amelia（开发者）各拥有 7 个技能，因为分析和实现阶段的工作类型最为多样；Sally（UX 设计师）和 Winston（架构师）各只有 1-2 个技能，因为设计和架构阶段的输出高度聚焦。各技能代码的详细含义参见第 2.2 节的速查表。

**跨阶段协作的关键设计：** 注意 John（产品经理）和 Winston（架构师）都拥有 `IR`（实施就绪检查）技能。这不是功能重复，而是**视角互补**。John 从需求完整性和用户价值视角验证就绪性，Winston 从技术可行性和架构一致性视角验证就绪性。只有两个维度同时通过，项目才能进入实施阶段。

### 1.3 Agent 的激活与人格保持机制

Agent 的激活遵循严格的八步协议：

```
Step 1: 配置解析 → 三层定制化合并（基础→团队→个人）
Step 2: 前置步骤 → activation_steps_prepend 中的自定义初始化
Step 3: 人格采纳 → 角色、身份、沟通风格、行为准则
Step 4: 持久事实 → 加载 project-context.md 等全局上下文
Step 5: 配置加载 → 读取 config.yaml 中的用户名、语言、输出路径
Step 6: 用户问候 → 以 Agent 角色和指定语言问候用户
Step 7: 后置步骤 → activation_steps_append 中的自定义初始化
Step 8: 菜单分发 → 展示技能菜单或直接调度已明确意图
```

其中最具工程价值的设计是 **"人格保持"（Persona Persistence）**。SKILL.md 中明确要求：一旦激活，Agent 的人格、持久事实、图标前缀和语言设定将在整个会话中持续生效，直到用户主动解除。这意味着如果激活了 Amelia（开发者），她不会在编码过程中突然切换为产品经理的思维方式来评价需求——她会严格以工程师的视角执行任务。

**图标前缀（Icon Prefix）** 是一个看似微小但极具实用性的设计。每个 Agent 在输出时都带有专属图标前缀（Mary=📊、John=📋、Sally=🎨、Winston=🏗️、Amelia=💻、Paige=📚）。在多 Agent 协作或长会话中，开发者一眼就能识别当前是哪个 Agent 在发言，有效防止角色混淆。

### 1.4 设计原则的差异化塑造

每个 Agent 拥有三条独有的行为原则，这些原则不是装饰性描述，而是**约束 LLM 行为的工程护栏**。对比一下核心差异：

**Mary（分析师）的原则：**

- "Every finding grounded in verifiable evidence"——每项发现必须基于可验证的证据
- "Requirements stated with absolute precision"——需求表述必须绝对精确
- "Every stakeholder voice represented"——每个利益相关方的声音都要被代表

这三条原则将 Mary 的行为锚定在"严谨的实证分析"上。她不会基于直觉做出市场判断，不会使用模糊的需求描述，也不会忽视少数利益相关方的诉求。

**Amelia（开发者）的原则：**

- "No task complete without passing tests"——没有通过测试，任务不算完成
- "Red, green, refactor — in that order"——红-绿-重构，严格按序执行
- "Tasks executed in the sequence written"——任务按书写顺序执行

这三条原则将 Amelia 的行为锚定在"测试驱动的工程纪律"上。她不会跳过测试先写实现代码，不会在红灯阶段做重构，也不会自行调整任务的执行顺序。

**Winston（架构师）的原则：**

- "Rule of Three before abstraction"——三次重复再抽象
- "Boring technology for stability"——无聊技术保稳定
- "Developer productivity is architecture"——开发者生产力即架构

这三条原则将 Winston 的行为锚定在"务实的工程权衡"上。他不会在只有一个用例时就设计通用抽象，不会追求最新最酷的技术栈，也不会为了架构的"优雅"牺牲开发效率。

这种差异化的原则设计，本质上是**在 LLM 的注意力空间中植入角色化的决策偏好**，使得同一个 LLM 在不同 Agent 人格下表现出截然不同的专业判断。

## 2 Skills 技能系统：42 个原子能力单元

如果说 Agent 是 BMAD 的"人格层"，那么 Skills 就是它的"能力层"。42 个技能构成了 BMAD 方法论的可执行基座——每个技能都是一个独立的、可编排的、可定制的原子能力单元。

### 2.1 Skills 的分层架构

42 个技能分为两大模块：

| 模块 | 技能数量 | 定位 |
|------|---------|------|
| Core（核心模块） | 14 个 | 通用能力，跨阶段可用 |
| BMM（方法模块） | 28 个 | 阶段专用，按工作流编排 |

**Core 模块**提供的是不依赖特定开发阶段的通用能力。**BMM 模块**则按四阶段工作流严格分布，承载了从分析到实施的具体执行逻辑。下方的速查表给出了全部 42 个技能的概览。

### 2.2 Skills 速查表

> **阅读说明：** "代码"列对应 Agent 菜单中的缩写（如 `BP`、`MR`）。标记 ★ 的为**必需关卡**（Required Gate），不可跳过。标记"直接调用"的技能不在任何 Agent 菜单中，需通过 `/bmad:bmad-xxx` 斜杠命令调用。

#### Core 模块（14 个）——跨阶段通用能力

| 代码 | 技能名称 | 功能描述 | 调用方式 |
|------|---------|---------|---------|
| BP | brainstorming | 引导式头脑风暴，使用多种创意技术发散和收敛想法 | Mary 菜单 |
| PM | party-mode | 多 Agent 圆桌讨论，每个 Agent 作为独立子代理参与对话 | 直接调用 |
| — | help | 分析当前状态和用户意图，推荐下一步应使用的技能 | 直接调用 |
| ID | index-docs | 为指定目录生成或更新 index.md 文档索引 | 直接调用 |
| SD | shard-doc | 将大型 Markdown 文档按二级标题拆分为多个小文件 | 直接调用 |
| PR | editorial-review-prose | 文案级编辑审查，检查文字表达和沟通问题 | 直接调用 |
| SR | editorial-review-structure | 结构级编辑审查，提出裁剪、重组和简化建议 | 直接调用 |
| RA | review-adversarial-general | 对抗性审查，以批评视角产出发现报告 | 直接调用 |
| RE | review-edge-case-hunter | 边缘用例探测，遍历所有分支路径报告未处理场景 | 直接调用 |
| DI | distillator | 无损 LLM 优化压缩，将源文档蒸馏为高信息密度版本 | 直接调用 |
| — | customize | 编写和更新已安装 BMAD 技能的定制化覆盖配置 | 直接调用 |
| DP ★ | document-project | 分析存量项目，生成供人类和 LLM 消费的项目文档 | Mary / Paige 菜单 |
| GP ★ | generate-project-context | 生成 project-context.md，定义项目级 AI 规则 | 直接调用 |
| AE | advanced-elicitation | 推动LLM重新审视、细化和改进其近期输出 | 直接调用 |

#### BMM 分析阶段（7 个）——需求发现与市场洞察

| 代码 | 技能名称 | 功能描述 | 调用方式 |
|------|---------|---------|---------|
| BP | brainstorming | 项目级头脑风暴（与 Core 共享，分析阶段激活） | Mary 菜单 |
| MR | market-research | 市场与竞品研究，产出竞争格局和客户洞察报告 | Mary 菜单 |
| DR | domain-research | 领域与行业研究，深入业务领域建模 | Mary 菜单 |
| TR | technical-research | 技术与架构研究，评估技术选型和可行性 | Mary 菜单 |
| CB | product-brief | 通过引导式或自主发现创建/更新产品简报 | Mary 菜单 |
| WB | prfaq | Working Backwards PRFAQ 挑战，逆向锻造产品概念 | Mary 菜单 |
| DP | document-project | 分析现有项目产出文档（分析阶段复用） | Mary 菜单 |

#### BMM 规划阶段（7 个）——需求到设计的转化

| 代码 | 技能名称 | 功能描述 | 调用方式 |
|------|---------|---------|---------|
| CP ★ | create-prd | 专家引导式 PRD 创建，产出产品需求文档 | John 菜单 |
| VP | validate-prd | 验证 PRD 的完备性、精简性、组织性和一致性 | John 菜单 |
| EP | edit-prd | 更新已有的产品需求文档 | John 菜单 |
| CU | create-ux-design | 引导完成 UX 设计规格，为架构和实施提供设计依据 | Sally 菜单 |
| CA ★ | create-architecture | 引导式架构决策文档创建，保持实施不偏离轨道 | Winston 菜单 |
| CE ★ | create-epics-and-stories | 将 PRD 拆分为 Epic 和 Story 清单驱动开发 | John 菜单 |
| IR ★ | check-implementation-readiness | 确保 PRD、UX、架构和 Story 清单四方对齐 | John / Winston 菜单 |

#### BMM 方案设计阶段（1 个）——实施排期

| 代码 | 技能名称 | 功能描述 | 调用方式 |
|------|---------|---------|---------|
| SP ★ | sprint-planning | 生成或更新 Sprint 计划，排列实施任务顺序 | Amelia 菜单 |

#### BMM 实施阶段（7 个）——编码、测试与交付

| 代码 | 技能名称 | 功能描述 | 调用方式 |
|------|---------|---------|---------|
| CS | create-story | 为 Story 注入完整实施上下文，准备开发 | Amelia 菜单 |
| DS ★ | dev-story | 按红-绿-重构循环实现 Story 的测试和代码 | Amelia 菜单 |
| QD | quick-dev | 统一快速流程——明确意图、规划、实现、审查、交付 | Amelia 菜单 |
| CR | code-review | 发起多维质量面的综合代码审查 | Amelia 菜单 |
| — | checkpoint-preview | LLM 辅助的人机交互式变更审查 | 直接调用 |
| QA | qa-generate-e2e-tests | 为已有功能生成 API 和端到端自动化测试 | Amelia 菜单 |
| CC | correct-course | 实施中途发现重大变更需求时，确定纠偏方案 | John 菜单 |
| ER | retrospective | Epic 级别的工作回顾和经验提炼 | Amelia 菜单 |

### 2.3 BMM 技能的阶段分布与依赖关系

28 个 BMM 技能按工作流阶段分布如下：

| 阶段 | 技能列表 | 必需关卡 |
|------|---------|---------|
| 分析（Analysis） | brainstorming, market-research, domain-research, technical-research, product-brief, prfaq, document-project | 无（分析阶段鼓励探索） |
| 规划（Planning） | **create-prd**, validate-prd, edit-prd, create-ux-design, **create-architecture**, **create-epics-and-stories**, **check-implementation-readiness** | create-prd、create-architecture、create-epics-and-stories、check-implementation-readiness |
| 方案设计（Solutioning） | **sprint-planning** | sprint-planning |
| 实施（Implementation） | sprint-status, create-story, **dev-story**, code-review, checkpoint-preview, qa-generate-e2e-tests, retrospective | dev-story |

**必需关卡（Required Gate）** 是理解 BMAD 质量控制机制的关键概念。标记为"必需"的技能是不可跳过的执行节点。它们构成了一条刚性链：

```
create-prd → create-architecture → create-epics-and-stories
    → check-implementation-readiness → sprint-planning → dev-story
```

每一个箭头代表一个前置依赖。开发者不可能在没有 PRD 的情况下创建架构，不可能在没有架构的情况下拆分 Epic，也不可能在没有通过实施就绪检查的情况下进入编码。这不是流程的冗余，而是基于一个工程判断：**上游信息的缺失会在下游被 LLM 以"幻觉"的方式补偿，其代价远高于等待上游就绪**。

### 2.4 技能的内部构造

每个技能由一组结构化文件组成：

- **SKILL.md**：技能的入口文件，定义目标、角色、激活流程和执行逻辑
- **steps/**：分步骤执行文件（大型技能如 dev-story 包含 10 个步骤）
- **templates/**：输出模板（如 PRD 模板、架构决策模板）
- **checklist.md**：执行检查清单
- **customize.toml**：定制化配置面

以 `dev-story`（开发故事）技能为例，其执行流程包含 10 个严格有序的步骤：

1. **发现并加载故事文件**——从 Sprint 状态文件中定位下一个 `ready-for-dev` 的故事
2. **加载项目上下文**——读取项目编码规范、架构约束
3. **检测审查续做**——判断是全新开始还是代码审查后的续做
4. **标记故事进行中**——更新 Sprint 状态文件
5. **红-绿-重构循环实现**——先写失败测试，再最小实现，最后重构
6. **编写综合测试**——单元测试、集成测试、端到端测试
7. **运行验证与测试**——运行全量测试套件，确认无回归
8. **验证并标记完成**——所有验证通过后才能标记任务完成
9. **故事完成与标记审查**——执行完成定义检查清单，更新状态为 `review`
10. **完成沟通与用户支持**——向用户报告实现摘要

这个十步流程体现了 BMAD 对"AI 编码"的工程化治理。特别值得注意的是步骤 8 中的验证门禁——SKILL.md 中明确要求"NEVER mark a task complete unless ALL conditions are met — NO LYING OR CHEATING"（除非所有条件满足否则绝不标记任务完成——禁止欺骗）。这种措辞不是夸张，而是对 LLM "讨好型"倾向（倾向于声称任务已完成以取悦用户）的针对性约束。

## 3 Workflow 工作流：四阶段流程编排

Workflow 是 BMAD 的"编排层"，它将 Agent 和 Skills 组织为一条从分析到实施的有序流水线。

### 3.1 四阶段的流转逻辑

BMAD 的四阶段工作流遵循严格的单向依赖关系：

```
分析（Analysis）
  ↓ 产出：产品简报、市场研究报告、PRFAQ
规划（Planning）
  ↓ 产出：PRD、UX 设计规格、架构决策、Epic/Story 清单
方案设计（Solutioning）
  ↓ 产出：Sprint 计划、Story 文件
实施（Implementation）
  ↓ 产出：代码、测试、审查报告
```

每个阶段的输出工件存放在两个标准目录中：

- **规划工件**：`_bmad-output/planning-artifacts/`——存放 PRD、架构文档、Epic 清单等
- **实施工件**：`_bmad-output/implementation-artifacts/`——存放 Sprint 状态、Story 文件等

工件目录的位置通过 `config.yaml` 全局配置，所有 Agent 和技能通过 `{planning_artifacts}` 和 `{implementation_artifacts}` 占位符引用。这意味着如果团队希望将工件输出到其他位置，只需修改一处配置即可。

### 3.2 状态追踪与断点续做

BMAD 的状态追踪机制通过文件级元数据实现。以 Sprint 状态文件（`sprint-status.yaml`）为例，它记录每个 Story 的当前状态：

```
development_status:
  epic-1: "complete"
  1-1-user-registration: "complete"
  1-2-user-authentication: "in-progress"
  1-3-password-reset: "ready-for-dev"
```

Story 文件本身也包含 `Status` 字段，与 Sprint 状态文件形成**双写一致性**。当 `dev-story` 技能开始实现一个 Story 时，它会同时更新 Story 文件的 `Status` 字段和 Sprint 状态文件中对应的条目。

这种基于文件的状态追踪带来了两个关键能力：

**断点续做。** 会话中断后，Agent 通过读取 Sprint 状态文件即可恢复上下文——找到第一个 `ready-for-dev` 或 `in-progress` 的 Story，加载其文件内容，从上次中断的位置继续。无需重新描述项目背景，无需手动指定 Story 编号。

**可审计性。** 每个工件的当前状态可通过文件系统直接追溯。在金融行业的合规审查场景中，这意味着审计人员可以直接检查 `_bmad-output/` 目录下的工件文件和状态标记，确认项目是否遵循了既定流程。

### 3.3 实施就绪检查：规划到实施的守门人

`check-implementation-readiness`（实施就绪检查）是规划阶段与实施阶段之间最关键的质量闸门。它的角色定位明确表述为：

> "You are an expert Product Manager, renowned and respected in the field of requirements traceability and spotting gaps in planning. Your success is measured in spotting the failures others have made in planning."

这段角色定义揭示了一个精妙的设计意图：就绪检查不是由实施者（Amelia/开发者）执行的自检，而是由产品视角的独立审查者执行的交叉验证。它要回答的核心问题是——"规划文档之间是否存在遗漏、不一致或逻辑断裂？"

具体来说，它检查四个维度的对齐性：

1. **PRD 完整性**——需求是否覆盖了所有用户场景和边界条件
2. **UX 规格对齐**——UX 设计是否与 PRD 中的功能需求一一对应
3. **架构决策覆盖**——技术架构是否为每个 Epic 提供了实现路径
4. **Epic/Story 可执行性**——Story 是否具备开发所需的全部上下文（验收标准、技术约束、依赖关系）

只有四个维度全部通过，项目才能获得进入实施阶段的"通行证"。

## 4 Checkpoint 检查点：人机协作的质量闸门

Checkpoint 是 BMAD 中最具创新性的机制之一。它不是简单的"暂停等待确认"，而是一套精心设计的 **LLM 辅助人机交互式审查流程**。

### 4.1 checkpoint-preview 的五步审查流程

`checkpoint-preview` 技能将代码审查从"扫一眼 diff"升级为结构化的渐进式审查。其五步流程为：

```
Step 1: 定位（Orientation）→ Step 2: 导览（Walkthrough）→ Step 3: 细节审查（Detail Pass）→ Step 4: 测试（Testing）→ Step 5: 决策（Wrap-Up）
```

**Step 1: 定位（Orientation）。** 自动识别需要审查的变更来源——可能是 PR、提交、分支、Story 文件或 Sprint 状态。一旦定位变更，计算变更的"表面积统计"：变更文件数、涉及模块数、逻辑行数、架构边界跨越次数、新增公共接口数。这些量化指标帮助审查者快速建立对变更规模的直觉判断。

**Step 2: 导览（Walkthrough）。** 按设计意图（而非文件顺序）组织变更内容。这一步的核心创新是**关注点分组（Concern Grouping）**——将跨文件的、服务于同一设计意图的变更归组。例如，"输入验证"这一关注点可能同时涉及控制器层的参数校验、服务层的业务规则和数据库层的约束。导览将这些分散在不同文件中的相关变更聚合呈现，而非按文件逐个罗列。

**Step 3: 细节审查（Detail Pass）。** 聚焦于最高风险的位置。系统通过分析变更模式自动识别风险热点——如跨模块的修改、新引入的公共接口、并发相关的代码路径等。

**Step 4: 测试（Testing）。** 引导审查者关注测试覆盖的充分性。

**Step 5: 决策（Wrap-Up）。** 审查者做出最终裁决：**Approve**（批准发布）、**Rework**（返回重做）或 **Discuss**（进一步讨论）。

### 4.2 从 diff 到审查建议的智能转化

checkpoint-preview 最有价值的设计在于**审查建议路线（Suggested Review Order）** 的自动生成。当 Story 文件包含 `## Suggested Review Order` 章节时，审查流程会按预设路线引导审查者逐步浏览关键代码位置，每个位置以 `path:line` 格式呈现（如 `src/auth/middleware.ts:42`），在 IDE 终端中可直接点击跳转。

当没有预设路线时，系统会通过 `generate-trail.md` 从 diff 中自动生成一条审查路线。其生成逻辑遵循"从意图到实现"的顺序——先呈现最高层的设计意图（为什么做这个变更），再逐层深入到具体的实现细节（怎么做的），确保审查者始终在理解了"为什么"的前提下去评价"怎么做"。

## 5 三层配置系统：从框架到团队的适配层

BMAD 的可定制性通过三层配置覆盖机制实现，其合并规则在源码层面有精确的定义：

| 配置层级 | 文件位置 | 优先级 | 合并规则 |
|---------|---------|--------|---------|
| 基础配置 | `{skill-root}/customize.toml` | 最低（默认值） | 提供所有字段的基线 |
| 团队配置 | `_bmad/custom/{skill-name}.toml` | 中等 | 覆盖基础配置 |
| 个人配置 | `_bmad/custom/{skill-name}.user.toml` | 最高 | 覆盖团队配置 |

合并规则遵循以下精确语义：

- **标量（Scalar）**：覆盖——高优先级的值替换低优先级的值
- **表（Table）**：深度合并——递归合并嵌套结构
- **以 `code` 或 `id` 键索引的表数组**：匹配替换 + 新增——已存在的条目按 code/id 匹配替换，新条目追加
- **普通数组**：追加——高优先级的数组元素追加到低优先级数组末尾

这套合并规则由 `_bmad/scripts/resolve_customization.py` 脚本统一执行。每个 Agent 激活时的第一步就是调用这个脚本解析三层配置，确保运行时行为与定制意图一致。

**实际应用场景：** 假设团队希望 Mary（分析师）在分析金融产品时始终遵循"银保监合规优先"的原则。只需在 `_bmad/custom/bmad-agent-analyst.toml` 中添加：

```toml
[[agent.principles]]
"Compliance with banking regulations takes precedence over market speed."
```

这条原则会通过数组追加规则合并到 Mary 默认的三条原则之后，形成团队级别的行为约束。而无需修改框架的任何源文件。

## 6 Agent × Skills × Workflow：三维协同模型

至此，我们已经拆解了 Agent、Skills、Workflow 和 Checkpoint 四大核心概念。但 BMAD 的真正威力不在于单个概念的精巧，而在于它们之间的协同机制。本节将从三个维度揭示这种协同关系。

### 6.1 Agent 与 Skills 的绑定：能力菜单机制

Agent 与 Skills 的关系不是"一个 Agent 执行所有技能"，而是**通过菜单（Menu）机制进行有界绑定**。每个 Agent 的 customize.toml 中定义了一个 `[[agent.menu]]` 数组，每个条目包含 `code`（技能代码）、`description`（描述）和 `skill`（技能名称）或 `prompt`（直接指令）。

这意味着：

- Mary（分析师）**只能**调用 BP、MR、DR、TR、CB、WB、DP 七个技能
- Winston（架构师）**只能**调用 CA、IR 两个技能
- Amelia（开发者）**只能**调用 DS、QD、QA、CR、SP、CS、ER 七个技能

技能菜单的设计逻辑是：**Agent 的专业边界决定了其可调度的技能范围**。Winston 不会去创建 PRD，John 不会去写代码，Amelia 不会去做市场调研。这不是能力的限制，而是**职责的隔离**——确保每个阶段由具备相应专业判断力的 Agent 负责执行。

### 6.2 Skills 与 Workflow 的映射：阶段归属机制

28 个 BMM 技能按阶段归属，形成技能-工作流映射：

| 工作流阶段 | 负责的主要 Agent | 该阶段的核心技能链 |
|-----------|----------------|-----------------|
| 分析 | Mary（分析师） | brainstorming → market-research / domain-research / technical-research → product-brief → prfaq |
| 规划 | John（产品经理）+ Sally（UX）+ Winston（架构师） | create-prd → validate-prd → create-ux-design → create-architecture → create-epics-and-stories → check-implementation-readiness |
| 方案设计 | John + Winston | sprint-planning |
| 实施 | Amelia（开发者） | create-story → dev-story → code-review → checkpoint-preview → retrospective |

注意规划阶段是**多 Agent 协作**的典型场景：John 负责需求定义（PRD），Sally 负责 UX 设计规格，Winston 负责架构决策。三个 Agent 共同贡献于规划阶段的输出工件，但各自只在其专业领域内活动。

### 6.3 协同运作的完整实例

以一个具体的用户场景来展示三维协同的运作方式：

**场景：** 开发者启动一个新的金融产品功能——"智能风控规则引擎"。

**阶段一：分析。** 开发者激活 Mary（分析师）。Mary 加载项目上下文，展示菜单。开发者选择 MR（市场研究）和 TR（技术研究）。Mary 执行 `bmad-market-research` 和 `bmad-technical-research` 技能，产出市场分析报告和技术可行性报告，写入 `_bmad-output/planning-artifacts/`。

**阶段二：规划。** 开发者依次激活 John、Sally、Winston。John 执行 `bmad-create-prd`，基于 Mary 的分析报告产出 PRD。Sally 执行 `bmad-create-ux-design`，基于 PRD 产出 UX 设计规格。Winston 执行 `bmad-create-architecture`，基于 PRD 和 UX 产出架构决策文档。最后，John（或 Winston）执行 `bmad-check-implementation-readiness`，交叉验证所有规划工件的对齐性。

**阶段三：方案设计。** John 执行 `bmad-create-epics-and-stories`，将 PRD 拆分为 Epic 和 Story 清单。Amelia 执行 `bmad-sprint-planning`，生成 Sprint 状态文件。

**阶段四：实施。** Amelia 执行 `bmad-dev-story`，按红-绿-重构循环实现每个 Story。每完成一个 Story，状态从 `ready-for-dev` 变为 `in-progress` 再变为 `review`。开发者调用 `bmad-checkpoint-preview` 对完成的 Story 进行结构化审查。审查通过后，Story 状态更新为 `complete`。

**贯穿全流程：** Paige（文档专家）可以在任意阶段被激活，执行文档生成、图表绘制或概念解释。

这个完整流程展示了 BMAD 的核心价值主张：**每一个产出物都有明确的负责人（Agent）、可追溯的输入来源（上游工件）和结构化的质量保障（检查点和必需关卡）**。AI 不再是"无所不能但无所专精"的通用助手，而是以专业角色的身份参与到一个有序的工程流程中。

## 7 核心概念的协作关系总结

将本章的分析浓缩为一张三维协同模型图：

```
              Agent（角色层）
             /    |    \
           Mary  John  Winston  ...
          /       |        \
    Skills（能力层）          Checkpoint（质量层）
      |        |                |
  brainstorming  create-prd   checkpoint-preview
  market-research validate-prd  code-review
  ...            ...           ...
         \       |       /
          Workflow（编排层）
          分析 → 规划 → 方案设计 → 实施
```

**Agent 决定"谁来做"**——六个专业角色各自在其领域内提供深度专业判断。

**Skills 决定"做什么"**——42 个原子技能覆盖从市场研究到代码审查的全链路能力（速查表见第 2.2 节）。

**Workflow 决定"什么时候做"**——四阶段流程编排确保执行的有序性和依赖关系的完整性。

**Checkpoint 决定"做到什么程度算合格"**——人机协作的审查机制在每个关键节点设置质量闸门。

四者协同，构成了一个从"模糊想法"到"可运行代码"的完整工程化路径。

## 8 本章小结与下章预告

本章完成了对 BMAD 四大核心概念的深度拆解。关键结论如下：

**Agent 体系的本质是角色化分工。** 六个 Agent 不是六个提示词模板，而是六个具备独立方法论根基、行为准则和技能边界的专业协作者。其价值不在于"谁能做更多"，而在于"每个角色在其专业领域内做到更深"。

**Skills 体系的本质是原子化能力编排。** 42 个技能按阶段归属，通过"必需关卡"机制形成刚性依赖链。这种设计将"AI 自由发挥"转变为"按流程执行"，同时保留了"anytime"技能的灵活性。

**Workflow 的本质是工件驱动的状态机。** 四阶段流程不是文档化的流程图，而是通过文件系统中的状态标记和工件依赖关系实际执行的工程流程。

**Checkpoint 的本质是结构化的人机协作审查。** 五步审查流程将"扫一眼 diff"升级为按设计意图组织的渐进式审查，使人类的审查质量与 AI 的执行质量同步提升。

然而，BMAD 并非 AI 驱动开发方法论的唯一选择。OpenSpec 以开放规格驱动为核心范式，Superpowers 以 Claude Code 高效实践为目标，它们从不同角度回应了相同的行业痛点。在下一章中，我们将对三大框架进行横向对比——从设计哲学、能力矩阵到适用场景——帮助你在面对具体项目时做出准确的选型判断。
