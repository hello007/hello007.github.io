# 核心概念知识体系 - 总览

**文档定位：** AI转型核心概念完整知识体系
**制作时间：** 2026年3月
**适用团队：** 3-10人Java技术团队
**学习周期：** 3个月核心期

---

## 📚 文档导航

本知识体系包含6个核心模块，从基础到应用，从理论到实践，全面覆盖AI应用开发所需的核心概念。

### 🎯 学习路径建议

```
第1个月：基础夯实
├─ Week 1-2：AI基础层概念
│   ├─ 理解LLM、Prompt、Token等基础
│   ├─ 掌握API调用
│   └─ 完成第一个Demo
│
└─ Week 3-4：AI应用层技术
    ├─ 掌握RAG技术
    ├─ 学习Agent开发
    └─ 理解Function Calling

第2个月：工程实践
├─ Week 5-6：工程架构层
│   ├─ 学习LangChain4j/Spring AI
│   ├─ 实现Rate Limiting和Caching
│   └─ 实现流式响应
│
└─ Week 7-8：数据与知识层
    ├─ 掌握数据分块策略
    ├─ 实现数据清洗
    ├─ 构建知识库
    └─ 实现元数据管理

第3个月：深化落地
├─ Week 9-10：安全与合规
├─ Week 11：工作方法论
└─ Week 12：综合项目实战
```

---

## 📖 模块列表

### 1. [AI基础层概念详解](./01.AI基础层概念详解.md)

**学习目标：** 建立对AI基础概念的清晰认知

**核心内容：**
- LLM（大语言模型）
- Prompt Engineering（提示词工程）
- Token（词元）
- Temperature（温度参数）
- Context Window（上下文窗口）
- Embedding（向量化）
- 模型推理 vs 训练
- Transformer架构

**适合人群：** AI初学者

**学习周期：** Week 1-2

**掌握程度：** 🎯 必须掌握 / 📖 需要了解

---

### 2. [AI应用层核心技术详解](./02.AI应用层核心技术详解.md)

**学习目标：** 掌握AI应用开发的核心技术

**核心内容：**
- RAG（检索增强生成）⭐ 核心
- Vector Database（向量数据库）⭐ 核心
- Agent（智能体）⭐ 核心
- Function Calling（函数调用）
- Chain of Thought（思维链）
- Multimodal（多模态）
- Knowledge Graph（知识图谱）

**适合人群：** 需要开发AI应用的Java开发者

**学习周期：** Week 3-6

**掌握程度：** 🎯 必须掌握 / 📖 需要了解 / 🚀 进阶学习

---

### 3. [工程架构层概念详解](./03.工程架构层概念详解.md)

**学习目标：** 掌握AI应用工程化开发的架构和工具

**核心内容：**
- LangChain4j（Java AI框架）⭐ 推荐
- Spring AI（Spring官方）
- API Rate Limiting（速率限制）
- Caching Strategy（缓存策略）
- Streaming Response（流式响应）
- Orchestration（编排）
- Observability（可观测性）

**适合人群：** 需要构建生产级AI应用的Java开发者

**学习周期：** Week 5-8

**掌握程度：** 🎯 必须掌握 / 📖 需要了解

---

### 4. [数据与知识层概念详解](./04.数据与知识层概念详解.md)

**学习目标：** 掌握构建高质量知识库的核心技术

**核心内容：**
- Chunking（分块策略）⭐ 核心
- Data Cleaning（数据清洗）
- Metadata Management（元数据管理）
- Re-ranking（重排序）
- Hybrid Search（混合检索）
- Knowledge Base Construction（知识库构建）

**适合人群：** 需要搭建RAG系统和知识库的Java开发者

**学习周期：** Week 5-8

**掌握程度：** 🎯 必须掌握 / 📖 需要了解 / 🚀 进阶学习

---

### 5. [安全与合规层概念详解](./05.安全与合规层概念详解.md)

**学习目标：** 掌握AI应用的基本安全和合规要求

**核心内容：**
- Prompt Injection（提示词注入）⭐ 重要
- Data Privacy（数据隐私）
- PII Redaction（敏感信息脱敏）
- Content Moderation（内容审核）
- Audit Logging（审计日志）

**适合人群：** 需要构建生产级AI应用的Java开发者

**学习周期：** Week 9-10（前期了解，后期深入）

**掌握程度：** 🎯 必须掌握 / 📖 需要了解

**重要说明：**
- 第1-3个月：了解基本风险和简单防护
- 第4-6个月：引入工程化安全实践
- 第7-12个月：建立金融级合规体系

---

### 6. [工作方法论与工具链详解](./06.工作方法论与工具链详解.md)

**学习目标：** 掌握AI协作的工作方式和工具

**核心内容：**

**AI编程方法论：**
- VibeCoding（氛围编程）
- SpecCoding（规范驱动开发）
- Prompt-First Development（以提示词为核心）

**AI Agent能力体系：**
- Tool Calling（工具调用）
- Planning（任务规划）
- Memory Management（记忆管理）
- RAG Skills（检索增强技能）

**推荐工具：**
- AI代码编辑器：Cursor、GitHub Copilot
- LLM API：OpenAI、Anthropic、通义千问
- AI框架：LangChain4j、Spring AI
- 向量数据库：PgVector、Milvus

**适合人群：** 所有需要转型AI开发的Java开发者

**学习周期：** 贯穿整个转型期

**掌握程度：** 🎯 必须掌握 / 📖 需要了解

---

### 7. [前沿AI概念详解](./07.前沿AI概念详解.md)

**学习目标：** 掌握2025-2026年最新AI工程方法论

**核心内容：**

**Engineering方法论：**
- Prompt Engineering（提示词工程）
- Context Engineering（上下文工程）
- Agentic Engineering（智能体工程）
- Harness Engineering（驾驭工程）

**Agent协作模式：**
- A2A（Agent to Agent）协作
- A2UI（Agent to User Interface）交互
- Skills（技能）系统

**通信协议标准：**
- MCP（Model Context Protocol）

**适合人群：** 需要深入理解AI架构的高级开发者

**学习周期：** Week 5-12

**掌握程度：** 🎯 必须掌握 / 📖 需要了解 / 🚀 进阶学习

---

## 🎯 掌握程度说明

- **🎯 必须掌握**：核心工作必备，需要深度理解和实践
- **📖 需要了解**：拓展视野，理解概念即可
- **🚀 进阶学习**：3个月后根据需要深入学习

---

## 💡 学习建议

### 1. 循序渐进

```
第1步：建立认知（Week 1-2）
├─ 阅读：AI基础层概念详解
├─ 实践：调用第一个LLM API
└─ 目标：理解AI是什么，能做什么

第2步：掌握核心技术（Week 3-6）
├─ 阅读：AI应用层核心技术详解
├─ 实践：实现RAG系统、开发Agent
└─ 目标：能独立开发AI应用

第3步：工程化实践（Week 7-8）
├─ 阅读：工程架构层概念详解
├─ 实践：使用框架、优化性能
└─ 目标：构建生产级应用

第4步：深化提升（Week 9-12）
├─ 阅读：数据与知识层、安全与合规
├─ 实践：综合项目实战
└─ 目标：达到生产可用水平
```

### 2. 理论结合实践

```
20% 理论学习
├─ 阅读文档
├─ 理解概念
└─ 掌握原理

50% 动手实践
├─ 跟着示例做
├─ 修改参数观察效果
└─ 遇到问题查文档

30% 复盘总结
├─ 总结经验教训
├─ 记录最佳实践
└─ 分享给团队
```

### 3. 建立知识体系

```
概念层：理解核心概念
├─ LLM是什么
├─ RAG如何工作
└─ Agent能做什么

技术层：掌握实现方法
├─ 如何调用API
├─ 如何实现RAG
└─ 如何开发Agent

应用层：解决实际问题
├─ 智能问答系统
├─ 文档问答系统
└─ 研发助手Agent
```

---

## 📊 学习检查清单

### 基础认知（Week 1-2）

- [ ] 理解LLM是什么，能做什么
- [ ] 掌握Prompt Engineering基础
- [ ] 理解Token、Temperature、Context Window
- [ ] 能独立调用LLM API
- [ ] 完成第一个AI Demo

### 核心技术（Week 3-6）

- [ ] 理解RAG原理，能实现基础RAG
- [ ] 掌握向量数据库使用
- [ ] 理解Agent概念，能开发简单Agent
- [ ] 掌握Function Calling
- [ ] 理解Chain of Thought

### 工程能力（Week 7-8）

- [ ] 熟练使用LangChain4j或Spring AI
- [ ] 实现Rate Limiting
- [ ] 实现多级缓存
- [ ] 实现流式响应
- [ ] 掌握编排技术

### 数据处理（Week 7-8）

- [ ] 掌握文档分块策略
- [ ] 实现数据清洗Pipeline
- [ ] 掌握元数据管理
- [ ] 能构建完整知识库

### 安全合规（Week 9-10）

- [ ] 理解Prompt Injection风险
- [ ] 实现输入验证和过滤
- [ ] 理解数据隐私要求
- [ ] 了解审计日志

### 工作方法（贯穿始终）

- [ ] 掌握Prompt-First开发
- [ ] 理解VibeCoding概念
- [ ] 熟练使用Cursor等AI工具
- [ ] 建立AI协作习惯

---

## 🔗 相关资源

### 内部文档

- [AI转型规划总指南](../10.AI转型规划-团队向AI方向转型实操指南.md)
- [团队宣贯材料](../01.团队宣贯材料-AI转型启动会.md)

### 外部资源

**官方文档：**
- [OpenAI API文档](https://platform.openai.com/docs)
- [LangChain4j文档](https://docs.langchain4j.dev/)
- [Spring AI文档](https://spring.io/projects/spring-ai)

**学习课程：**
- [DeepLearning.AI - Prompt Engineering](https://www.deeplearning.ai/short-courses/)
- [吴恩达 - AI for Everyone](https://www.coursera.org/learn/ai-for-everyone)

**工具网站：**
- [Cursor IDE](https://cursor.sh/)
- [OpenAI Playground](https://platform.openai.com/playground)
- [Hugging Face](https://huggingface.co/)

---

## ❓ 常见问题

### Q1：我需要按顺序学习所有模块吗？

**A：** 不需要。建议按学习路径：基础层 → 应用层 → 工程层 → 数据层 → 安全层 → 方法论。但可以根据实际情况调整。

### Q2：每个概念需要学到什么程度？

**A：** 注意标注的掌握程度：
- 🎯 必须掌握：深度理解，能独立实现
- 📖 需要了解：理解概念，知道何时使用
- 🚀 进阶学习：3个月后根据需要深入学习

### Q3：学习时间不够怎么办？

**A：** 优先学习：
1. AI基础层（建立认知）
2. RAG技术（核心应用）
3. LangChain4j（开发框架）
4. Prompt-First（工作方法）

其他内容可以在实践中逐步学习。

### Q4：遇到问题怎么办？

**A：**
1. 先查文档
2. 再搜索相关资料
3. 团队内讨论
4. 向AI求助（用Prompt描述问题）

---

## 📝 使用说明

### 如何使用这份知识体系？

```
1. 学习前
   ├─ 阅读"总览"了解全貌
   ├─ 确定当前学习阶段
   └─ 制定学习计划

2. 学习中
   ├─ 按顺序阅读对应模块文档
   ├─ 跟着示例动手实践
   ├─ 记录笔记和疑问
   └─ 完成练习题

3. 学习后
   ├─ 复盘总结
   ├─ 整理笔记
   ├─ 分享给团队
   └─ 应用到实际项目
```

### 文档更新说明

- **当前版本：** v1.0
- **更新时间：** 2026年3月
- **维护团队：** AI转型小组
- **反馈渠道：** 团队内部讨论

---

## 🎓 结语

这份核心概念知识体系涵盖了从AI基础到工程实践、从数据处理到安全合规的完整内容。

**记住三个关键点：**

1. **循序渐进**：不要一次性学完所有内容，按阶段逐步深入
2. **实践为主**：理论结合实践，动手做才是最快的学习方式
3. **持续迭代**：AI技术发展迅速，保持学习，持续优化

**祝学习顺利！🚀**

---

**下一步行动：**

开始学习 → [01.AI基础层概念详解](./01.AI基础层概念详解.md)

---

*文档版本：v1.0*
*制作时间：2026年3月*
*维护者：AI转型小组*
