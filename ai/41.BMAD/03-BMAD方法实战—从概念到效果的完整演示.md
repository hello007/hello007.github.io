---
title: "第3章：BMAD 方法实战 — 从概念到效果的完整演示"
date: 2026-05-15
series: "AI 驱动开发方法论 — BMAD 框架深度解析与实战"
chapter: 3
chapter_type: chapter
tags: [BMAD, Agent, Skills, Checkpoint, 实战演示, 工作流, 配置定制]
category: AI工程化
prev: "02-BMAD核心概念体系深度拆解.md"
next: "04-四大框架横向对比—BMAD与OpenSpec与Superpowers与gstack.md"
---

# 第3章：BMAD 方法实战 — 从概念到效果的完整演示

第2章完成了对 BMAD 核心概念体系的深度拆解：六位专业 Agent、42 个可编排 Skills、四阶段结构化 Workflow、Checkpoint 人机审查闸门，以及三层配置覆盖系统。我们理解了每个组件的设计意图和内部构造。

然而，理解概念与感受实际效果之间存在一道鸿沟。开发者真正关心的问题是：**这些概念用起来是什么感觉？产出的东西长什么样？值得投入学习成本吗？**

本章的目标就是跨越这道鸿沟。我们将以一个简化但完整的项目——"用户认证模块"——为线索，逐一展示 BMAD 各核心功能在实际使用中的交互体验、产出样例和定制效果。读完本章后，你应该对 BMAD 的每个主要功能形成直观的认识。

## 1 Agent 激活与角色切换的实际体验

### 1.1 激活 Mary：第一次与专业分析师对话

在 Claude Code 中激活 Mary 只需输入斜杠命令：

```
/bmad:bmad-agent-analyst
```

激活后，Mary 会执行八步协议中的标准流程：解析配置、采纳人格、加载持久事实、读取全局设置，然后以分析师的身份向用户问候。其实际输出大致如下：

> 📊 你好，Liuyang！我是 Mary，你的业务分析师。我已经准备好协助你进行市场研究、竞品分析和需求探索。你可以随时调用 `/bmad:bmad-help` 获取建议。
>
> 以下是我可以为你提供的服务：
>
> | 代码 | 描述 | 技能 |
> |------|------|------|
> | BP | 专家引导的头脑风暴 | bmad-brainstorming |
> | MR | 市场分析、竞争格局、客户需求与趋势 | bmad-market-research |
> | DR | 行业领域深度研究、领域知识与术语 | bmad-domain-research |
> | TR | 技术可行性、架构选项与实现路径 | bmad-technical-research |
> | CB | 通过引导式或自主发现创建/更新产品简报 | bmad-product-brief |
> | WB | Working Backwards PRFAQ 挑战 | bmad-prfaq |
> | DP | 分析现有项目产出文档 | bmad-document-project |
>
> 请输入代码、编号或描述你的需求。

这段问候体现了 BMAD Agent 激活的三个关键特征：

**图标前缀。** 输出以 📊 开头，这是 Mary 的专属图标。在后续的每一次交互中，这个图标都会出现在消息头部，确保用户始终知道当前发言的是 Mary 而非其他 Agent。

**个性化问候。** Mary 使用配置文件中的 `user_name`（此处为 Liuyang）和 `communication_language`（此处为中文）进行问候。问候语风格反映了其 `communication_style` 配置——"寻宝者发现模式时的兴奋感，麦肯锡备忘录的结构化表达"。

**菜单即能力边界。** Mary 展示的七个技能（BP、MR、DR、TR、CB、WB、DP）严格限定在她的职责范围内。她不会提及创建 PRD、设计架构或编写代码——这些属于其他 Agent 的专业领域。

### 1.2 切换到 Amelia：从分析思维到工程纪律

在同一会话中切换 Agent 是 BMAD 的常规操作。当分析阶段完成，开发者进入实施阶段时，激活 Amelia：

```
/bmad:bmad-agent-dev
```

> 💻 Liuyang，Amelia 在线。Story 有路径，AC 有编号，测试先行。
>
> | 代码 | 描述 | 技能 |
> |------|------|------|
> | DS | 按红-绿-重构循环实现 Story 的测试和代码 | bmad-dev-story |
> | QD | 统一快速流程 | bmad-quick-dev |
> | QA | 为已有功能生成测试 | bmad-qa-generate-e2e-tests |
> | CR | 多维综合代码审查 | bmad-code-review |
> | SP | 生成或更新 Sprint 计划 | bmad-sprint-planning |
> | CS | 为 Story 注入实施上下文 | bmad-create-story |
> | ER | Epic 级别工作回顾 | bmad-retrospective |
>
> 输入代码或告诉我你要做什么。

对比 Mary 和 Amelia 的问候语，差异一目了然：

| 维度 | Mary（分析师） | Amelia（开发者） |
|------|---------------|----------------|
| 图标 | 📊 | 💻 |
| 问候风格 | 热情而结构化 | 极简、工程化 |
| 沟通方式 | "准备好协助你进行市场研究" | "Story 有路径，AC 有编号，测试先行" |
| 隐含方法论 | Porter 战略 + Minto 金字塔 | Kent Beck TDD + 务实程序员 |
| 菜单范围 | 7个分析类技能 | 7个实施类技能 |

这种差异不是表面上的角色扮演，而是**深层的行为约束**。当你向 Mary 提问"这个功能应该怎么实现"时，她会从市场需求和竞品分析的角度回答——因为她被约束在分析师的角色内。同样的问题抛给 Amelia，她会要求你提供 Story 文件和验收标准——因为她的原则明确规定"No task complete without passing tests"。

### 1.3 Paige 在不同阶段的调用差异

Paige（技术文档专家）的特殊之处在于她是**跨阶段可用**的 Agent。这意味着在分析阶段和实施阶段调用她，产出的文档类型和风格会有显著差异。

**分析阶段调用 Paige**（例如执行 DP 技能分析存量项目）：

> 📚 好的，我来分析现有项目结构并生成项目文档。让我先扫描代码库……
>
> **项目分析报告**
>
> ## 1 项目概览
> - 技术栈：Java 17 / Spring Boot 3.2 / Spring Security / MySQL 8.0
> - 构建工具：Gradle 8.x
> - 代码规模：约 12,000 行业务代码，3,200 行测试代码
> - ……

**实施阶段调用 Paige**（例如为已完成的 Story 生成实施说明）：

> 📚 好的，基于 Story 1-2 的实施记录，我来生成面向运维的部署说明……
>
> **用户认证模块 — 实施说明**
>
> ## 1 变更范围
> - 新增：`src/auth/controller/AuthController.java`
> - 新增：`src/auth/service/TokenService.java`
> - 修改：`src/auth/config/SecurityConfig.java`
> - ……

同一 Agent 在不同上下文中展现出完全不同的产出——这不是因为 Paige "记住了"阶段信息，而是因为她的输入来源（上游工件文件）随工作流的推进而变化。分析阶段加载的是项目源码，实施阶段加载的是 Story 文件和代码变更记录。**工件驱动的上下文传递**确保了 Agent 的产出始终与当前阶段对齐。

## 2 Skills 的典型使用场景与效果

### 2.1 分析阶段：MR（市场研究）的产出样例

市场研究技能（MR）是 Mary 菜单中的高频技能。激活 Mary 后选择 MR，她会先进行主题发现：

> 📊 让我们开始你的**市场研究**。
>
> **你想研究什么主题、问题或领域？**
>
> 例如：
> - "欧洲电动汽车市场"
> - "植物基食品替代品市场"
> - "东南亚移动支付解决方案"
> - "或者任何你感兴趣的方向……"

用户输入"金融行业 AI 认证方案市场"后，Mary 进行三轮澄清（核心主题、研究目标、范围），然后进入研究执行阶段。最终产出一份结构化的市场研究报告，写入 `_bmad-output/planning-artifacts/research/` 目录：

```markdown
---
type: market-research
topic: "金融行业 AI 认证方案市场"
date: 2026-05-15
status: complete
---

# 金融行业 AI 认证方案市场研究报告

## 执行摘要
- 金融行业对 AI 身份认证的需求受监管驱动，市场规模预计 2026-2028 年
  CAGR 达 23.5%
- 核心竞争者：Face++（旷视）、Authme、Onfido（已被 Entrust 收购）
- 客户痛点集中在上行：合规成本高；下行：用户体验差

## 市场规模与趋势
### 全球市场
- 2025 年市场规模：约 78 亿美元
- 2028 年预测：约 147 亿美元（CAGR 23.5%）
- 驱动因素：KYC/AML 监管趋严、远程开户需求激增

### 中国市场
- 2025 年市场规模：约 12 亿美元
- 核心驱动力：《个人信息保护法》实施后的合规需求

## 竞争格局分析
| 厂商 | 核心能力 | 目标客户 | 定价模式 | 差异化优势 |
|------|---------|---------|---------|-----------|
| Face++ | 人脸识别 + 活体检测 | 大中型金融机构 | 按调用量计费 | 技术领先、API 生态完善 |
| Authme | 多因子认证 | 中小银行和金融科技 | SaaS 订阅 | 部署灵活、合规认证齐全 |
| Onfido | 文档 + 生物识别 | 全球跨境业务 | 按验证次数 | 覆盖 195 个国家证件 |

## 客户洞察
### 主要需求
1. 满足监管合规要求（银保监、人行反洗钱）
2. 降低人工审核成本
3. 提升用户开户转化率

### 未被满足的需求
- 中小银行缺乏定制化方案，被迫使用标准化产品
- 多渠道（柜面、APP、小程序）统一的认证体验尚未成熟
……
```

这份报告的结构体现了 Mary 的 Minto 金字塔原理训练——**结论先行**（执行摘要放在最前），**分组归类**（市场规模、竞争格局、客户洞察各自独立成章），**逻辑递进**（从宏观趋势到微观痛点）。

**关键观察：** 报告中的每个判断都附带了数据来源和推导过程，这是 Mary 的第一条原则"Every finding grounded in verifiable evidence"在产出层面的直接体现。

### 2.2 规划阶段：CP（create-prd）的引导式交互

create-prd 是 John（产品经理）的核心技能，也是 BMAD 中交互最密集的技能之一。它采用**步骤文件架构（Step-File Architecture）**，将 PRD 创建过程分解为多个微文件，按严格顺序加载和执行。

用户激活 John 后选择 CP：

> 📋 Liuyang，让我们开始创建你的产品需求文档。我将引导你逐步完成。
>
> 首先，让我检查一下是否有可用的上游工件……
>
> ✅ 发现以下上游工件：
> - `market-research-金融行业AI认证方案市场-2026-05-15.md`
>
> 我将基于这份市场研究报告作为输入。

John 会读取上游工件并进入初始化步骤。以下是 PRD 引导式创建的核心流程（简化展示）：

**Step 1（初始化）：** John 确认产品愿景和目标用户。

> 📋 基于市场研究，我理解我们要构建的是：
>
> **产品愿景：** 为中小银行提供一套可定制化的 AI 身份认证解决方案
> **目标用户：** 中小银行 IT 部门和合规部门
> **核心价值：** 在满足银保监合规要求的同时，将开户认证时间从平均 3 分钟缩短至 30 秒
>
> 这个理解准确吗？需要调整哪些部分？

**Step 2（功能需求挖掘）：** John 基于市场研究中的客户洞察，提出功能假设并请用户验证。

**Step 3（非功能需求确认）：** John 引导确认性能、安全、合规等约束。

经过多步交互后，最终产出的 PRD 文件写入 `_bmad-output/planning-artifacts/prd.md`：

```markdown
---
type: prd
status: draft
stepsCompleted: ["step-01-init", "step-02-features", "step-03-nonfunctional"]
created: 2026-05-15
---

# 产品需求文档：AI 身份认证解决方案

## 1 产品愿景与目标
### 1.1 愿景陈述
为中小银行提供一套可定制化的 AI 身份认证方案，在满足监管
合规的前提下，将开户认证时间从 3 分钟缩短至 30 秒。

### 1.2 成功指标
| 指标 | 当前基线 | 目标值 | 衡量方式 |
|------|---------|--------|---------|
| 开户认证耗时 | 3.2 分钟 | ≤ 30 秒 | 端到端计时 |
| 人工审核比例 | 45% | ≤ 10% | 审核系统统计 |
| 认证通过率 | 82% | ≥ 95% | 通过/申请比 |

## 2 用户角色
| 角色 | 描述 | 核心需求 |
|------|------|---------|
| 银行客户 | 开户或办理业务的终端用户 | 快速、安全的身份验证 |
| 审核员 | 银行合规部门工作人员 | 高效处理异常认证案例 |
| 系统管理员 | 银行 IT 部门运维人员 | 灵活配置认证策略和阈值 |

## 3 功能需求
### FR-01：多因子身份认证
**优先级：** P0
**描述：** 支持身份证 OCR + 人脸比对 + 活体检测三因子组合认证
**验收标准：**
- AC-01：系统在 5 秒内完成 OCR 识别并返回结构化结果
- AC-02：人脸比对准确率 ≥ 99.5%
- AC-03：活体检测可防御照片、视频、3D 面具三类攻击

### FR-02：认证策略引擎
**优先级：** P0
**描述：** 允许管理员根据风险等级配置不同的认证因子组合
**验收标准：**
- AC-04：支持至少 3 种预设策略模板
- AC-05：策略变更在 10 秒内生效

……
```

**关键设计细节：** PRD 文件的 frontmatter 中包含 `stepsCompleted` 数组。这不是装饰性元数据——它是**断点续做**的实现机制。如果 PRD 创建在 Step 2 时会话中断，John 在下次激活时可以读取这个数组，准确知道从哪个步骤恢复。

### 2.3 实施阶段：DS（dev-story）的红-绿-重构执行

dev-story 是 BMAD 中最复杂的技能之一，包含 10 个严格有序的执行步骤。当 Amelia 执行 DS 时，她首先从 Sprint 状态文件中定位下一个 `ready-for-dev` 的 Story：

> 💻 正在扫描 Sprint 状态……
>
> ✅ **发现待开发 Story**
> Story：`1-2-user-authentication`
> 状态：`ready-for-dev`
>
> 🚀 **开始全新实施**
> Story：1-2-user-authentication
> 首个未完成任务：Task 1 — 实现 TokenService 核心逻辑

然后进入红-绿-重构循环。这是 Kent Beck TDD 的严格实践：

**红灯阶段——先写失败测试：**

> 💻 **红灯阶段**：为 Task 1 编写失败测试
>
> ```java
> // TokenServiceTest.java
> @Test
> void shouldGenerateValidJWTToken_whenValidCredentials() {
>     TokenService tokenService = new TokenService(secretKey, expiration);
>     String token = tokenService.generateToken("user123", "TELLER");
>     
>     assertNotNull(token);
>     assertTrue(tokenService.validateToken(token));
>     assertEquals("user123", tokenService.extractUsername(token));
> }
> 
> @Test
> void shouldRejectExpiredToken() {
>     TokenService tokenService = new TokenService(secretKey, 0);
>     String token = tokenService.generateToken("user123", "TELLER");
>     
>     assertFalse(tokenService.validateToken(token));
> }
> ```
>
> ❌ 测试运行结果：2 FAILED（编译错误——TokenService 类尚不存在）

**绿灯阶段——写最小实现使测试通过：**

> 💻 **绿灯阶段**：编写最小实现
>
> ```java
> // TokenService.java
> @Service
> public class TokenService {
>     private final String secretKey;
>     private final long expiration;
>     
>     public String generateToken(String username, String role) {
>         return Jwts.builder()
>             .subject(username)
>             .claim("role", role)
>             .issuedAt(new Date())
>             .expiration(new Date(System.currentTimeMillis() + expiration))
>             .signWith(Keys.hmacShaKeyFor(secretKey.getBytes()))
>             .compact();
>     }
>     
>     public boolean validateToken(String token) {
>         try {
>             Jwts.parser()
>                 .verifyWith(Keys.hmacShaKeyFor(secretKey.getBytes()))
>                 .build()
>                 .parseSignedClaims(token);
>             return true;
>         } catch (JwtException e) {
>             return false;
>         }
>     }
>     
>     public String extractUsername(String token) {
>         return Jwts.parser()
>             .verifyWith(Keys.hmacShaKeyFor(secretKey.getBytes()))
>             .build()
>             .parseSignedClaims(token)
>             .getPayload()
>             .getSubject();
>     }
> }
> ```
>
> ✅ 测试运行结果：2 PASSED

**重构阶段——改善结构，保持测试通过：**

> 💻 **重构阶段**：提取重复的密钥解析逻辑
>
> ```java
> // 将重复的 Keys.hmacShaKeyFor(secretKey.getBytes()) 提取为字段
> @Service
> public class TokenService {
>     private final SecretKey signingKey;
>     private final long expiration;
>     
>     public TokenService(
>             @Value("${auth.jwt.secret}") String secretKey,
>             @Value("${auth.jwt.expiration}") long expiration) {
>         this.signingKey = Keys.hmacShaKeyFor(secretKey.getBytes());
>         this.expiration = expiration;
>     }
>     // ……
> }
> ```
>
> ✅ 重构后测试运行结果：2 PASSED（无回归）

在每个 Task 完成后，Amelia 会执行严格的验证门禁：

> 💻 **Task 1 验证门禁**
> - [x] 所有测试存在且 100% 通过
> - [x] 实现与 Task 描述精确匹配
> - [x] 相关验收标准已满足
> - [x] 全量测试套件无回归
>
> ✅ Task 1 标记为完成

这对应了 SKILL.md 中的硬性约束——"NEVER mark a task complete unless ALL conditions are met — NO LYING OR CHEATING"。验证门禁不是可选的最佳实践，而是**不可跳过的执行步骤**。

### 2.4 审查类技能：CR（code-review）的多维度审查输出

当 Story 实施完成后，开发者可以调用 CR 进行代码审查。BMAD 的 code-review 采用了**并行对抗审查层（Parallel Adversarial Review Layers）**的设计，模拟多个专业审查者同时工作：

> 💻 **代码审查启动**
>
> 变更范围：Story 1-2-user-authentication
> 涉及文件：8 个新增，3 个修改
>
> ---
>
> **审查层 1：Blind Hunter（盲猎者）**
> *以"假设代码有缺陷"为前提进行搜索*
>
> | 严重度 | 位置 | 发现 |
> |--------|------|------|
> | 🔴 高 | `TokenService.java:28` | JWT 密钥硬编码在构造函数参数中，应从 Vault 或 KMS 获取 |
> | 🔴 高 | `AuthController.java:45` | 登录接口缺少速率限制，存在暴力破解风险 |
> | 🟡 中 | `TokenService.java:52` | `validateToken` 吞掉了 JwtException，建议记录日志后返回 |
>
> **审查层 2：Edge Case Hunter（边缘用例猎手）**
> *遍历所有分支路径，报告未处理场景*
>
> | 严重度 | 位置 | 发现 |
> |--------|------|------|
> | 🟡 中 | `TokenService.java` | 未处理密钥长度不足导致 HMAC 初始化失败的情况 |
> | 🟢 低 | `AuthController.java:67` | `extractUsername` 返回 null 时未处理下游 NPE |
>
> **审查层 3：Acceptance Auditor（验收审计员）**
> *逐条对照 Story 验收标准检查实现*
>
> | AC 编号 | 状态 | 备注 |
> |---------|------|------|
> | AC-01 | ✅ 通过 | OCR 识别平均耗时 3.2 秒（目标 ≤ 5 秒） |
> | AC-02 | ⚠️ 部分 | 人脸比对准确率测试未包含暗光场景 |
> | AC-03 | ❌ 未覆盖 | 活体检测的 3D 面具防御测试缺失 |

最终输出一个**结构化的分类处理报告（Triage Report）**，将发现按"必须修复"、"建议修复"、"可选优化"三级分类，并给出具体的修复建议和代码位置。这种多维度的对抗性审查设计，使得单次审查的覆盖范围远超开发者自检或传统的人工 Code Review。

### 2.5 质量工具：DI（distillator）的压缩前后对比

distillator 是 BMAD 中一个独特的技术工具——它执行的是**无损压缩**而非有损摘要。其核心价值在于：将冗长的源文档压缩为高信息密度的版本，供后续 Agent 作为输入使用，从而节省上下文窗口。

以一份 2,500 字的市场研究报告为例，distillator 的压缩效果如下：

**压缩前（2,500 字 / 约 3,500 tokens）：**

```markdown
## 市场规模与趋势

全球 AI 身份认证市场在 2025 年达到了约 78 亿美元的规模。
这一增长主要受到全球范围内日益严格的 KYC（了解你的客户）
和 AML（反洗钱）监管要求的驱动。随着越来越多的金融服务
向线上迁移，传统的面对面身份验证方式已经无法满足现代
金融服务对效率和用户体验的要求。

根据多家研究机构的综合预测，到 2028 年，全球市场规模预计
将达到约 147 亿美元，年复合增长率（CAGR）约为 23.5%。

在中国市场方面，2025 年的规模约为 12 亿美元。主要的增长
驱动力来自于《个人信息保护法》的实施带来的合规需求，
以及中小银行数字化转型过程中对远程开户能力的迫切需求。
```

**压缩后（distillate，约 400 字 / 约 550 tokens）：**

```markdown
## 市场规模与趋势

- 全球 AI 身份认证市场 2025 年约 78 亿美元
- 2028 年预测约 147 亿美元（CAGR 23.5%）
- 驱动因素：KYC/AML 监管趋严、金融服务线上化
- 中国市场 2025 年约 12 亿美元
- 中国驱动因素：《个人信息保护法》合规、中小银行数字化转型
```

**压缩比：约 6.4:1。** 原文中的所有数据点（78 亿、147 亿、23.5%、12 亿）、所有因果关系（监管驱动、线上化需求）、所有约束条件（《个人信息保护法》）均被完整保留。被剥离的是过渡性语句、重复表述和解释性扩写——这些对人类阅读友好但对 LLM 消费冗余的内容。

distillator 还支持 `--validate` 标志，执行**往返验证（Round-Trip Validation）**：从压缩后的 distillate 尝试还原原文，然后对比还原结果与原文的差异，确认没有信息丢失。这一机制为"无损"声明提供了可验证的证据。

## 3 Checkpoint 审查的实操效果

### 3.1 五步审查流程的实际输出样例

checkpoint-preview 的五步审查流程是 BMAD 中最具设计感的质量机制。以审查 Story 1-2（用户认证）的代码变更为例，完整流程如下：

**Step 1：定位（Orientation）**

> 💻 **[Orientation]** → Walkthrough → Detail Pass → Testing
>
> > **Intent:** 实现用户认证模块的核心功能——JWT Token 生成与验证、登录/登出 API、认证中间件
>
> 8 files changed · 3 modules touched · ~320 lines of logic · 2 boundary crossings · 4 new public interfaces

定位步骤产出了变更的"表面积统计"：8 个文件、3 个模块、约 320 行逻辑代码、2 次跨模块边界、4 个新增公共接口。这些量化指标让审查者在 30 秒内建立对变更规模和复杂度的直觉判断。

**Step 2：导览（Walkthrough）**

> 💻 Orientation → **[Walkthrough]** → Detail Pass → Testing
>
> ### 关注点 1：认证 API 入口
> 登录和登出是整个变更的主入口，定义了外部消费者与认证模块的交互契约。
>
> - `src/auth/controller/AuthController.java:25` — POST /auth/login 端点定义
> - `src/auth/controller/AuthController.java:52` — POST /auth/logout 端点定义
> - `src/auth/dto/LoginRequest.java:1` — 登录请求数据契约
>
> ### 关注点 2：Token 生命周期管理
> JWT 的生成、验证和刷新是认证模块的核心逻辑，直接关联安全性和性能。
>
> - `src/auth/service/TokenService.java:18` — Token 生成逻辑
> - `src/auth/service/TokenService.java:45` — Token 验证与过期检查
> - `src/auth/service/TokenService.java:62` — Token 刷新机制
>
> ### 关注点 3：安全拦截层
> 认证中间件是系统的安全闸门，所有受保护资源的请求都经过此层。
>
> - `src/auth/middleware/AuthMiddleware.java:15` — 请求拦截与 Token 提取
> - `src/auth/middleware/AuthMiddleware.java:38` — 角色权限校验
> - `src/auth/config/SecurityConfig.java:20` — 安全策略配置

**关注点分组** 是这一步的核心创新。注意，"认证 API 入口"这一关注点横跨了 Controller 和 DTO 两个文件中的代码，而"Token 生命周期管理"集中在 Service 层但涉及多个方法。传统按文件顺序的审查（file1 → file2 → file3）会将服务于同一设计意图的变更碎片化呈现；而关注点分组按设计意图组织，审查者始终在理解了"为什么"的前提下去看"怎么做"。

**Step 3：细节审查（Detail Pass）**

> 💻 Orientation → Walkthrough → **[Detail Pass]** → Testing
>
> **风险热点：**
>
> 🔴 `src/auth/service/TokenService.java:28` — 密钥管理
> JWT 签名密钥通过构造函数注入字符串，建议升级为 Vault/KMS 集成。
> 风险：密钥泄露导致全线 Token 可伪造。
>
> 🟡 `src/auth/middleware/AuthMiddleware.java:38` — 角色校验
> 当前实现仅检查角色是否匹配，未实现层级权限。如 TELLER 角色不应
> 访问 ADMIN 接口但当前逻辑未区分。
>
> 🟢 `src/auth/controller/AuthController.java:25` — 日志记录
> 登录成功/失败事件建议增加结构化日志，便于审计追踪。

细节审查聚焦于风险最高的位置。系统通过分析变更模式自动识别风险热点——跨模块修改、新引入的公共接口、涉及安全敏感操作的代码路径。审查者无需通读所有 320 行代码，而是集中精力在标记为高风险的位置。

**Step 4：测试覆盖检查（Testing）**

> 💻 Orientation → Walkthrough → Detail Pass → **[Testing]**
>
> | 测试类别 | 数量 | 覆盖范围 |
> |---------|------|---------|
> | 单元测试 | 12 | TokenService(6), AuthMiddleware(4), AuthController(2) |
> | 集成测试 | 3 | 登录流程(1), Token 刷新(1), 权限拦截(1) |
> | E2E 测试 | 1 | 完整登录→操作→登出流程 |
>
> **缺口：** 暗光环境下人脸比对的测试用例缺失（AC-02 相关）。

**Step 5：决策（Wrap-Up）**

> 💻 Orientation → Walkthrough → Detail Pass → Testing → **[Wrap-Up]**
>
> ---
>
> 审查完成。对这次变更的决定是？
> - **Approve** — 批准发布（如需，我可以协助交互式修补）
> - **Rework** — 返回重做（回退提交、修订规格、尝试不同方案）
> - **Discuss** — 还有问题想讨论

### 3.2 三种决策的实际差异

**Approve（批准）：** 如果审查者确认变更质量达标，Amelia 会简要确认并主动询问是否需要交互式修补（例如在发布前修复标记为 🟢 低风险的小问题）。

**Rework（返工）：** 如果变更存在严重问题，Amelia 会帮助审查者制定返工方案——是回退整个提交，还是仅修复特定问题？是否需要修订 Story 规格？她会给出具体的、可操作的建议。

**Discuss（讨论）：** 如果审查者尚无法做出判断，Amelia 会进入开放对话模式，回答问题、探讨疑虑。讨论结束后回到决策提示。

### 3.3 关注点分组如何改善审查效率

在传统的 diff 审查中，审查者按文件顺序逐个查看变更。假设一次变更涉及 8 个文件，按文件顺序可能是：

```
AuthController.java → LoginRequest.java → TokenService.java →
AuthMiddleware.java → SecurityConfig.java → TokenServiceTest.java →
AuthControllerTest.java → AuthMiddlewareTest.java
```

审查者需要在脑中自行关联分散在不同文件中的相关变更——Controller 中的 API 定义与 DTO 中的数据契约是什么关系？Service 中的 Token 生成与 Middleware 中的验证是否一致？

关注点分组将这个认知过程前置。审查者按照"认证 API 入口"→"Token 生命周期"→"安全拦截层"的逻辑顺序浏览，每个关注点内的代码位置都已按因果关系排列。**审查的认知负载从"关联碎片"降低为"验证逻辑"**。

## 4 四阶段工作流的端到端运作

### 4.1 以"用户认证模块"演示完整流程

以下是以"用户认证模块"为项目的端到端工作流演示，展示每个阶段的输入/输出工件。

**阶段一：分析（Analysis）**

| 项目 | 内容 |
|------|------|
| 负责人 | Mary（分析师） |
| 执行技能 | MR → DR → CB |
| 输入 | 用户的初始想法："我们需要一个 AI 身份认证方案" |
| 输出工件 | `market-金融行业AI认证方案-research-2026-05-15.md`、`domain-银行业身份认证-research-2026-05-15.md`、`product-brief.md` |

**阶段二：规划（Planning）**

| 项目 | 内容 |
|------|------|
| 负责人 | John（产品经理）+ Sally（UX）+ Winston（架构师） |
| 执行技能 | CP → VP → CU → CA → CE → IR |
| 输入 | 分析阶段的全部工件 |
| 输出工件 | `prd.md`、`ux-design.md`、`architecture.md`、`epics-stories.md` |
| 必需关卡 | create-prd ✅ → create-architecture ✅ → create-epics-and-stories ✅ → check-implementation-readiness ✅ |

**阶段三：方案设计（Solutioning）**

| 项目 | 内容 |
|------|------|
| 负责人 | Amelia（开发者） |
| 执行技能 | SP |
| 输入 | `epics-stories.md`、`architecture.md` |
| 输出工件 | `sprint-status.yaml`、各 Story 文件 |

Sprint 状态文件的实际内容：

```yaml
# sprint-status.yaml
sprint_name: "Sprint 1 - 用户认证核心"
last_updated: 2026-05-15

development_status:
  epic-1: "in-progress"
  1-1-project-setup: "complete"
  1-2-user-authentication: "in-progress"
  1-3-multi-factor-auth: "ready-for-dev"
  1-4-auth-policy-engine: "ready-for-dev"
  1-5-integration-testing: "blocked"
```

**阶段四：实施（Implementation）**

| 项目 | 内容 |
|------|------|
| 负责人 | Amelia（开发者） |
| 执行技能 | CS → DS → CR → checkpoint-preview → ER |
| 输入 | Story 文件 + 项目上下文 |
| 输出工件 | 代码文件、测试文件、审查报告 |

### 4.2 状态文件如何驱动断点续做

断点续做是 BMAD 工程化设计中最具实用价值的能力之一。考虑以下场景：

开发者在实施 Story 1-2 时，完成了 3 个 Task 中的 2 个，然后下班关机。第二天重新打开会话，激活 Amelia，选择 DS。

Amelia 的第一步是读取 Sprint 状态文件：

```yaml
development_status:
  1-2-user-authentication: "in-progress"
```

然后读取 Story 文件，检查 Task 的完成状态：

```markdown
## Tasks/Subtasks
- [x] Task 1：实现 TokenService 核心逻辑
- [x] Task 2：实现 AuthController 登录/登出 API
- [ ] Task 3：实现 AuthMiddleware 请求拦截与权限校验
```

Amelia 直接从 Task 3 继续：

> 💻 ⏯️ **续做 Story 1-2-user-authentication**
>
> Story 状态：in-progress
> 首个未完成任务：Task 3 — 实现 AuthMiddleware 请求拦截与权限校验
>
> 🚀 开始实施……

**整个过程无需开发者重新描述项目背景、无需指定 Story 编号、无需回忆上次做到哪里。** 状态文件 + Story 文件的双写一致性机制，使得断点续做成为一个自动化的过程。

## 5 三层配置的定制化效果

### 5.1 修改 Agent 原则后的行为变化对比

BMAD 的三层配置系统允许团队在不修改框架源文件的前提下定制 Agent 行为。以修改 Mary 的原则为例：

**默认配置（基础层）：**

```toml
# {skill-root}/customize.toml
principles = [
  "Every finding grounded in verifiable evidence.",
  "Requirements stated with absolute precision.",
  "Every stakeholder voice represented.",
]
```

**团队覆盖配置（团队层）：**

```toml
# _bmad/custom/bmad-agent-analyst.toml
[[agent.principles]]
"Compliance with banking regulations takes precedence over market speed."
```

**合并后的实际配置：**

```toml
principles = [
  "Every finding grounded in verifiable evidence.",
  "Requirements stated with absolute precision.",
  "Every stakeholder voice represented.",
  "Compliance with banking regulations takes precedence over market speed.",
]
```

根据数组追加的合并规则，团队新增的原则被追加到基础原则之后。Mary 在后续的所有分析工作中，都会将银保监合规作为额外的决策约束——在评估竞品时会优先检查合规认证，在挖掘客户需求时会主动纳入合规视角。

**行为变化对比：**

| 维度 | 默认 Mary | 定制后的 Mary |
|------|----------|-------------|
| 竞品评估 | 优先比较技术能力和市场份额 | 额外检查是否通过银保监认证 |
| 需求挖掘 | 关注用户痛点和市场机会 | 同时关注合规约束和审计要求 |
| 风险提示 | 侧重市场风险和技术风险 | 额外提示合规风险和监管变化 |

### 5.2 添加自定义技能菜单的实际效果

除了修改原则，团队还可以通过菜单机制扩展 Agent 的能力范围。例如，为 Amelia 添加一个团队自定义的"安全扫描"技能：

```toml
# _bmad/custom/bmad-agent-dev.toml

[[agent.menu]]
code = "SS"
description = "Run security scan on changed files using OWASP guidelines"
skill = "team-security-scan"
```

合并后，Amelia 的菜单从 7 个技能扩展为 8 个：

> 💻 Liuyang，Amelia 在线。
>
> | 代码 | 描述 | 技能 |
> |------|------|------|
> | DS | 按红-绿-重构循环实现 Story | bmad-dev-story |
> | QD | 统一快速流程 | bmad-quick-dev |
> | QA | 生成测试 | bmad-qa-generate-e2e-tests |
> | CR | 多维代码审查 | bmad-code-review |
> | SP | Sprint 计划 | bmad-sprint-planning |
> | CS | Story 上下文注入 | bmad-create-story |
> | ER | Epic 回顾 | bmad-retrospective |
> | **SS** | **基于 OWASP 指南的安全扫描** | **team-security-scan** |
>
> 输入代码或告诉我你要做什么。

新增的 SS 技能以 `code` 匹配规则合并到菜单末尾。如果团队希望将 SS 插入到特定位置而非末尾，可以使用已有 code 进行替换——例如将 CR 的技能替换为安全增强版的代码审查。

**配置定制的工程意义：** 三层配置系统确保了框架的可定制性不依赖于对源文件的修改。团队可以在 `_bmad/custom/` 目录中维护自己的定制层，框架升级时只需更新基础层，团队配置通过合并规则自动叠加——不存在定制与升级之间的冲突。

## 6 本章小结与下章预告

本章通过"用户认证模块"这一简化项目，展示了 BMAD 各核心功能在实际使用中的交互体验和产出效果。关键结论如下：

**Agent 激活的本质是角色化行为的工程化触发。** 每个 Agent 不仅拥有独立的人格和沟通风格，更携带了与其角色严格匹配的方法论根基、行为原则和技能菜单。图标前缀、个性化问候和职责边界的菜单展示，共同构成了一个可感知、可信赖的角色化交互体验。

**Skills 的产出质量源于结构化的执行流程。** 无论是 MR 的市场研究报告（Minto 金字塔结构）、CP 的 PRD（步骤文件架构 + 断点续做）、DS 的代码实现（严格的红-绿-重构循环）、CR 的审查报告（并行对抗审查层），还是 DI 的压缩输出（无损压缩 + 往返验证），每个技能都有明确的产出规范和质量约束。

**Checkpoint 将代码审查从经验驱动升级为结构驱动。** 关注点分组替代了按文件顺序的碎片化审查，表面积统计和风险热点定位替代了全量扫描，三种决策模式提供了清晰的审查结论路径。

**状态文件是实现断点续做和可审计性的工程基座。** Sprint 状态文件和 Story 文件的双写一致性，使得会话中断后的恢复成为自动化过程，而非依赖开发者记忆的手动操作。

**三层配置在不修改源文件的前提下实现了行为定制。** 团队通过追加原则扩展 Agent 的决策约束，通过扩展菜单增加自定义技能，框架升级与团队定制互不干扰。

然而，BMAD 并非 AI 驱动开发方法论的唯一选择。OpenSpec 以开放规格驱动为核心范式，主张将规格确立为人类和 AI 共同认可的单一事实来源；Superpowers 以 Claude Code 高效实践为目标，通过可组合的技能系统和 TDD 纪律约束 AI 编码行为。在下一章中，我们将对三大框架进行系统化的横向对比——从设计哲学、架构特征、能力矩阵到适用场景——帮助你在面对具体项目时做出准确的选型判断。
