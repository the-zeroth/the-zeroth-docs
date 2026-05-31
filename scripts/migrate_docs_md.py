from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "docs_md"
CONTENT_ROOT = ROOT / "content" / "docs"
PUBLIC_ASSET_ROOT = ROOT / "public" / "docs-assets"
PUBLIC_IMAGE_ROOT = PUBLIC_ASSET_ROOT / "images"
PUBLIC_VIDEO_ROOT = PUBLIC_ASSET_ROOT / "videos"

VIDEO_FILES = {
    "Agent Creation Demonstration.mp4",
    "Graph Editing Demonstration.mp4",
    "Simple operation demonstration.mp4",
    "Warehouse interface display.mp4",
    "Display of the operation interface.mp4",
}


@dataclass(frozen=True)
class Page:
    source: str | None
    output: str
    title: str
    description: str
    literal: str | None = None
    asset_source: str | None = None


COMMON_PAGES = {
    "root": [
        "index",
        "start",
        "the-one-app",
        "multi-agent-architecture",
    ],
    "start": ["quick-start", "models-and-pricing", "release-notes"],
    "multi_agent": [
        "single-agent",
        "evolution",
        "more-possibilities",
    ],
    "single_agent": ["index", "model", "tools", "context", "react", "action-sequence"],
    "more_possibilities": ["index", "communication", "context-editing", "dynamic-graph"],
    "app": [
        "definition-space",
        "run",
        "settings",
    ],
    "definition_space": ["index", "profile", "mcp", "agent", "graph"],
    "run": ["index"],
    "settings": ["index", "space-management", "api-configuration"],
    "release_notes": ["index", "0-2-0", "0-1-0"],
}


OUTPUT_REMAP = {
    "multi-agent-architecture/single-agent.mdx": "multi-agent-architecture/single-agent/index.mdx",
    "multi-agent-architecture/model.mdx": "multi-agent-architecture/single-agent/model.mdx",
    "multi-agent-architecture/tools.mdx": "multi-agent-architecture/single-agent/tools.mdx",
    "multi-agent-architecture/context.mdx": "multi-agent-architecture/single-agent/context.mdx",
    "multi-agent-architecture/react.mdx": "multi-agent-architecture/single-agent/react.mdx",
    "multi-agent-architecture/action-sequence.mdx": "multi-agent-architecture/single-agent/action-sequence.mdx",
    "multi-agent-architecture/evolution.mdx": "multi-agent-architecture/evolution/index.mdx",
    "multi-agent-architecture/more-possibilities.mdx": "multi-agent-architecture/more-possibilities/index.mdx",
    "multi-agent-architecture/communication.mdx": "multi-agent-architecture/more-possibilities/communication.mdx",
    "multi-agent-architecture/context-editing.mdx": "multi-agent-architecture/more-possibilities/context-editing.mdx",
    "multi-agent-architecture/dynamic-graph.mdx": "multi-agent-architecture/more-possibilities/dynamic-graph.mdx",
    "the-one-app/definition-space.mdx": "the-one-app/definition-space/index.mdx",
    "the-one-app/profile.mdx": "the-one-app/definition-space/profile.mdx",
    "the-one-app/mcp.mdx": "the-one-app/definition-space/mcp.mdx",
    "the-one-app/agent.mdx": "the-one-app/definition-space/agent.mdx",
    "the-one-app/graph.mdx": "the-one-app/definition-space/graph.mdx",
    "the-one-app/run.mdx": "the-one-app/run/index.mdx",
    "the-one-app/settings.mdx": "the-one-app/settings/index.mdx",
    "the-one-app/space-management.mdx": "the-one-app/settings/space-management.mdx",
    "the-one-app/api-configuration.mdx": "the-one-app/settings/api-configuration.mdx",
}


ZH_META = {
    "meta.json": {
        "title": "The Zeroth Docs",
        "pages": [
            "---开始---",
            *COMMON_PAGES["root"][:2],
            "---The One 应用操作---",
            COMMON_PAGES["root"][2],
            "---Multi-Agent 工程思想---",
            COMMON_PAGES["root"][3],
        ],
    },
    "start/meta.json": {"title": "开始", "pages": COMMON_PAGES["start"]},
    "start/release-notes/meta.json": {"title": "发布记录", "pages": COMMON_PAGES["release_notes"]},
    "multi-agent-architecture/meta.json": {"title": "Multi-Agent 工程思想", "pages": COMMON_PAGES["multi_agent"]},
    "multi-agent-architecture/single-agent/meta.json": {"title": "单一 Agent", "pages": COMMON_PAGES["single_agent"]},
    "multi-agent-architecture/evolution/meta.json": {"title": "从单一 Agent 到 Multi-Agent", "pages": ["index"]},
    "multi-agent-architecture/more-possibilities/meta.json": {"title": "Multi-Agent 的更多可能", "pages": COMMON_PAGES["more_possibilities"]},
    "the-one-app/meta.json": {"title": "The One 应用操作", "pages": COMMON_PAGES["app"]},
    "the-one-app/definition-space/meta.json": {"title": "仓储（Definition Space）", "pages": COMMON_PAGES["definition_space"]},
    "the-one-app/run/meta.json": {"title": "运行", "pages": COMMON_PAGES["run"]},
    "the-one-app/settings/meta.json": {"title": "设置", "pages": COMMON_PAGES["settings"]},
}

EN_META = {
    "meta.json": {
        "title": "The Zeroth Docs",
        "pages": [
            "---Start---",
            *COMMON_PAGES["root"][:2],
            "---The One App---",
            COMMON_PAGES["root"][2],
            "---Multi-Agent Architecture---",
            COMMON_PAGES["root"][3],
        ],
    },
    "start/meta.json": {"title": "Start", "pages": COMMON_PAGES["start"]},
    "start/release-notes/meta.json": {"title": "Release Notes", "pages": COMMON_PAGES["release_notes"]},
    "multi-agent-architecture/meta.json": {"title": "Multi-Agent Architecture", "pages": COMMON_PAGES["multi_agent"]},
    "multi-agent-architecture/single-agent/meta.json": {"title": "Single Agent", "pages": COMMON_PAGES["single_agent"]},
    "multi-agent-architecture/evolution/meta.json": {"title": "From Single Agent to Multi-Agent", "pages": ["index"]},
    "multi-agent-architecture/more-possibilities/meta.json": {"title": "More Possibilities in Multi-Agent", "pages": COMMON_PAGES["more_possibilities"]},
    "the-one-app/meta.json": {"title": "The One App", "pages": COMMON_PAGES["app"]},
    "the-one-app/definition-space/meta.json": {"title": "Definition Space", "pages": COMMON_PAGES["definition_space"]},
    "the-one-app/run/meta.json": {"title": "Run", "pages": COMMON_PAGES["run"]},
    "the-one-app/settings/meta.json": {"title": "Settings", "pages": COMMON_PAGES["settings"]},
}


ZH_PAGES: list[Page] = [
    Page(
        None,
        "index.mdx",
        "欢迎",
        "了解 The One 为什么为 Multi-Agent 架构而生，以及应该从哪里开始阅读。",
        """The One 是一款专为 Multi-Agent 架构设计的桌面应用。它用来搭建、运行、观察和迭代你自己的多智能体系统。

## 核心理念

多智能体是 AI Agent 的未来，但今天的大多数探索还停留在“手写几个 Agent、硬编码几条调用链”的阶段。这个过程慢、脆弱、不可复用，也很难看清 Agent 之间到底发生了什么。

The One 的目标很直接：用一款软件来搭建任意人们能想象的 Multi-Agent 架构。

这让多智能体架构从“藏在代码里的流程”变成“可以被看见、讨论和修改的系统设计”。

The One 明确反对黑箱式 Agent 运行。在 The One 中，你可以从“上帝视角”观察一次 Graph 运行，看到 Agent 之间如何沟通、如何调用工具、如何传递状态，以及每个 Agent 当前拥有怎样的上下文。

这套透明性不是装饰功能，而是 Multi-Agent 探索的基础设施。看不清 Agent 怎么协作，就不可能系统性改进架构。

## 从这里开始

- [快速入门](./start/quick-start)：从安装到运行第一个 Multi-Agent Graph。
- [模型与价格](./start/models-and-pricing)：理解官方模型服务、第三方模型渠道和收费方式。
- [单一 Agent](./multi-agent-architecture/single-agent)：先理解一个 Agent 的构成，再进入 Multi-Agent。
- [仓储（Definition Space）](./the-one-app/definition-space)：理解 The One 如何管理 Prompt、Skill、MCP、Agent 和 Graph。
- [发布记录](./start/release-notes/0-2-0)：查看 The One 最新公开版本变化。

## 更多资源

- 下载 The One：请前往官网下载安装包。
- 支持邮箱：support@the-zeroth.com
""",
    ),
    Page("开始/快速入门.md", "start/quick-start.mdx", "快速入门", "从安装 The One 到运行第一个 Multi-Agent Graph 的最短路径。"),
    Page("开始/模型与价格.md", "start/models-and-pricing.mdx", "模型与价格", "理解官方模型服务、第三方模型渠道、订阅和用量包的边界。"),
    Page("The One的Multi-Agent工程思想/单一agent.md", "multi-agent-architecture/single-agent.mdx", "单一 Agent", "理解一个 Agent 由模型、工具和上下文共同决定。"),
    Page("The One的Multi-Agent工程思想/单一agent/模型.md", "multi-agent-architecture/model.mdx", "模型", "模型是 Agent 的大脑，不同 Agent 应该选择适合角色的模型。"),
    Page("The One的Multi-Agent工程思想/单一agent/工具.md", "multi-agent-architecture/tools.mdx", "工具", "工具让语言模型真正成为 Agent，工具边界就是能力边界。"),
    Page("The One的Multi-Agent工程思想/单一agent/上下文.md", "multi-agent-architecture/context.mdx", "上下文", "用约束、信息和任务三类上下文建立清晰的 Agent 心智。"),
    Page("The One的Multi-Agent工程思想/单一agent/ReAct.md", "multi-agent-architecture/react.mdx", "ReAct", "The One 中 Agent 默认采用推理、行动、观察再推理的运行方式。"),
    Page("The One的Multi-Agent工程思想/单一agent/行动链（action sequence）.md", "multi-agent-architecture/action-sequence.mdx", "行动链（Action Sequence）", "用行动链把复杂目标拆成更可执行的阶段路径。"),
    Page("The One的Multi-Agent工程思想/从单一agent到multi agent的演化.md", "multi-agent-architecture/evolution.mdx", "从单一 Agent 到 Multi-Agent", "解释为什么复杂任务需要多个角色清晰、上下文干净的 Agent 协作。"),
    Page("The One的Multi-Agent工程思想/multi agent的更多可能.md", "multi-agent-architecture/more-possibilities.mdx", "Multi-Agent 的更多可能", "Multi-Agent 相比单一 Agent 多出的独特能力边界。"),
    Page("The One的Multi-Agent工程思想/multi agent的更多可能/通讯方式.md", "multi-agent-architecture/communication.mdx", "通讯方式", "The One 中 Agent 之间的三种主要通讯方式。"),
    Page("The One的Multi-Agent工程思想/multi agent的更多可能/上下文编辑.md", "multi-agent-architecture/context-editing.mdx", "上下文编辑", "允许 Agent 在 Graph 中修改其他 Agent 的上下文。"),
    Page("The One的Multi-Agent工程思想/multi agent的更多可能/dynamic graph.md", "multi-agent-architecture/dynamic-graph.mdx", "Dynamic Graph", "让 Agent 在运行过程中动态创建、克隆、激活或休眠其他 Agent。"),
    Page("The One应用操作/仓储（definition space）.md", "the-one-app/definition-space.mdx", "仓储（Definition Space）", "Definition Space 是 The One 管理多智能体资源的核心仓储。"),
    Page("The One应用操作/仓储（definition space）/profile.md", "the-one-app/profile.mdx", "Profile", "编写、导入和复用 Prompt / Skill 模块。"),
    Page("The One应用操作/仓储（definition space）/mcp.md", "the-one-app/mcp.mdx", "MCP", "导入和管理常用 MCP 工具。"),
    Page("The One应用操作/仓储（definition space）/agent.md", "the-one-app/agent.mdx", "Agent", "创建具有独立模型、提示词和工具能力的 Agent 预设。"),
    Page("The One应用操作/仓储（definition space）/graph.md", "the-one-app/graph.mdx", "Graph", "用节点和边搭建可运行、可观察的 Multi-Agent Graph。"),
    Page("The One应用操作/运行.md", "the-one-app/run.mdx", "运行", "选择工作区路径和 Graph，启动一次透明的多智能体运行。"),
    Page("The One应用操作/设置.md", "the-one-app/settings.mdx", "设置", "管理账号、Definition Space、API Provider 和桌面运行环境。"),
    Page("The One应用操作/设置/仓储SPACE管理.md", "the-one-app/space-management.mdx", "仓储 Space 管理", "创建、切换、导入、导出和分享不同的 Definition Space。"),
    Page("The One应用操作/设置/api配置.md", "the-one-app/api-configuration.mdx", "API 配置", "配置官方模型服务、第三方 API Key、OAuth 和 OpenAI-compatible Provider。"),
    Page(
        None,
        "start/release-notes/index.mdx",
        "发布记录",
        "The One Desktop 的公开版本更新记录。",
        """这里收录 The One Desktop 的公开版本更新记录。

- [0.2.0](./0-2-0)：Provider 接入、Definition Space、分享平台和 Graph 语义升级。
- [0.1.0](./0-1-0)：第一个桌面端公开版本，完成仓储、编辑、运行、观察的核心闭环。
""",
    ),
    Page("开始/release notes/0.2.0/中文版.md", "start/release-notes/0-2-0.mdx", "The One 0.2.0 Release Notes", "0.2.0 带来 Provider 接入、Definition Space、分享平台和 Graph 语义升级。"),
    Page("开始/release notes/0.1.0/中文版.md", "start/release-notes/0-1-0.mdx", "The One 0.1.0 Release Notes", "0.1.0 是 The One 第一个完整桌面端公开版本。"),
]


EN_PAGES: list[Page] = [
    Page(
        None,
        "index.mdx",
        "Welcome",
        "Understand why The One exists for Multi-Agent architecture and where to start.",
        """The One is a desktop application built for Multi-Agent architecture. It helps you build, run, observe, and iterate on your own multi-agent systems.

## Core idea

Multi-Agent systems are the future of AI Agents, but most exploration today is still stuck at the stage of writing a few Agents by hand and hard-coding a few call chains. That workflow is slow, fragile, hard to reuse, and difficult to observe.

The One has a direct goal: let people build any Multi-Agent architecture they can imagine with one piece of software.

This turns Multi-Agent architecture from a hidden code path into a visible system design that can be discussed, modified, and improved.

The One is explicitly against black-box Agent execution. In The One, you can observe a Graph run from a system-level view: how Agents communicate, how they call tools, how state moves, and what context each Agent currently has.

That transparency is not decoration. It is infrastructure for Multi-Agent exploration. If you cannot see how Agents collaborate, you cannot improve the architecture systematically.

## Start here

- [Quick Start](./start/quick-start): Install The One and run your first Multi-Agent Graph.
- [Models and Pricing](./start/models-and-pricing): Understand official model service, third-party providers, subscriptions, and top-ups.
- [Single Agent](./multi-agent-architecture/single-agent): Understand one Agent before moving into Multi-Agent systems.
- [Definition Space](./the-one-app/definition-space): Learn how The One manages Prompts, Skills, MCP, Agents, and Graphs.
- [Release Notes](./start/release-notes/0-2-0): Read the latest public version notes.

## More resources

- Download The One from the official website.
- Support: support@the-zeroth.com
""",
    ),
    Page(
        None,
        "start/quick-start.mdx",
        "Quick Start",
        "The shortest path from installing The One to running your first Multi-Agent Graph.",
        """This guide takes you from installation to running your first custom Multi-Agent Graph in The One.

1. Install The One and sign in.

Download The One from the official website.

2. Start from the official default Definition Space, or download a Space you like from the sharing platform.

![Interface screenshot](./assets/image-20260531103928-b9rodqe.png)

3. Import your usual Prompts, Skills, and MCP tools, then adjust Agents and Graphs in your preferred way.

![Interface screenshot](./assets/image-20260531104008-xjbdzxl.png)

4. Choose a Graph, select the entry Agent such as PM, and start the conversation like you would in other AI Agent desktop applications.

![Interface screenshot](./assets/image-20260531104121-uinbxt8.png)
""",
        asset_source="开始/快速入门.md",
    ),
    Page(
        None,
        "start/models-and-pricing.mdx",
        "Models and Pricing",
        "Understand official model service, third-party providers, subscriptions, and top-ups.",
        """The One is The Zeroth's AI Agent desktop application. You can use The Zeroth official model service directly, or connect model accounts that you already own.

The One supports two usage modes:

1. Use The Zeroth official model service.
2. Connect your own third-party model provider.

## Official model service

This is the simplest and recommended path.

After signing in with a The Zeroth account, you can use the official model service in The One without preparing API keys or configuring model providers manually.

The Zeroth official model service is powered through OpenRouter. It gives you two practical advantages.

### Broader model selection and more stable service

OpenRouter aggregates many mainstream and frontier models. In The One, that means you can choose from model ecosystems such as OpenAI, Anthropic, Google, Meta, Mistral, DeepSeek, and others.

Compared with connecting to a single model vendor, the official service gives you more flexibility when choosing models for different Agents and tasks.

The Zeroth also maintains the integration for you, reducing the operational mess of managing several provider accounts and API keys.

### Better official-account pricing

The Zeroth accesses model services through official accounts, which usually gives users a lower operational barrier and more favorable pricing than opening and maintaining several model accounts independently.

Official model service is recommended for first-time users, users who do not want to configure API keys, users who want unified billing, and users who want to quickly test many models.

## Third-party model providers

If you already have model provider accounts, you can add your own API keys or complete OAuth authorization in The One.

Supported third-party channels include:

| Provider | Connection method |
| --- | --- |
| OpenAI | API Key |
| Anthropic Claude | API Key / Claude Code OAuth |
| Google Gemini | API Key / Gemini Code Assist OAuth |
| OpenAI Codex | OAuth |
| Custom compatible service | API Key |

Custom compatible services are useful for teams with an internal model gateway, private deployment, or any provider compatible with OpenAI-style APIs.

When you use a third-party provider, calls do not consume The Zeroth official model service quota. Cost, quota, rate limits, and model availability are decided by that provider.

## Pricing modes

The Zeroth official model service supports subscriptions and top-up packages.

### Subscription

Subscriptions are for users who keep using The One continuously. Each tier includes a different amount of official model service capacity.

| Plan | Price | Best for |
| --- | --- | --- |
| Starter | $20 / month | Light usage, personal exploration, low-frequency Agent workflows |
| Pro | $60 / month | Daily usage, Multi-Agent workflows, higher task frequency |
| Max | $200 / month | Heavy usage, complex workflows, high-frequency automation |

Every plan includes the core capabilities of The One: desktop app, Agent presets, Blueprint / Graph workflows, local execution, runtime observation, official model service, and third-party provider connection.

The main difference between plans is official model service capacity.

### Top-up package

If your current subscription capacity is not enough, you can purchase an additional top-up package.

| Package | Price | Description |
| --- | --- | --- |
| Top-up | $20 / purchase | Adds extra official model service capacity |

Top-ups do not change your subscription tier. They only increase your available official model service capacity.

## How third-party providers charge

If you use your own OpenAI, Anthropic, Gemini, or custom model service, the related cost is charged by that provider or by your organization.

The Zeroth does not deduct official model service capacity for third-party model calls.

## How to choose

For most users, official model service is the easiest path: less configuration, broader model choice, better pricing, and unified management.

If you already have provider accounts, or your company requires model calls to go through internal accounts, use third-party providers.
""",
    ),
    Page(
        None,
        "multi-agent-architecture/single-agent.mdx",
        "Single Agent",
        "Understand how one Agent is determined by model, tools, and context.",
        """At the core, every Agent is determined by three things:

1. Model

The model is the Agent's brain.

2. Available tools

Tools are the Agent's hands and feet.

3. All existing context

Context includes the system prompt and every relevant user / assistant message. It is the Agent's mind.

All context affects the Agent's behavior. The system prompt matters, but it is never the whole story.
""",
    ),
    Page(None, "multi-agent-architecture/model.mdx", "Model", "The model is the Agent's brain, and different roles need different models.", "The model is the Agent's brain. The recent model race has made one thing clear: the perfect model does not exist yet. Among top-tier models, there is no absolute winner. Each model has strengths, weaknesses, and preferred tasks.\n"),
    Page(None, "multi-agent-architecture/tools.mdx", "Tools", "Tools turn a language model into an Agent.", "Tools turn an LLM into an actual Agent. Without tools, even a powerful model is still only a chatbot. The boundary of available tools is the boundary of Agent capability, and The One's Multi-Agent architecture is built around composable tool access.\n"),
    Page(
        None,
        "multi-agent-architecture/context.mdx",
        "Context",
        "Use constraints, information, and tasks to build a clear Agent mind.",
        """Context can be divided into three categories, corresponding to three basic questions: who am I, where do I come from, and where am I going?

1. Constraints: who am I?

This includes the Agent's identity, strengths, permission boundaries, and behavioral rules.

2. Information: where do I come from?

This includes effective task-related information, such as code and documents already present in a repository.

3. Task: where am I going?

This is the work the Agent is asked to complete.

The quality of context engineering depends on whether these three areas are complete, explicit, and clear. Irrelevant context should be removed as much as possible.
""",
    ),
    Page(None, "multi-agent-architecture/react.mdx", "ReAct", "The One Agents run through reasoning, tool use, observation, and further reasoning.", "Agents in The One run with a ReAct-style architecture by default.\n\nWhen active, an Agent repeatedly reasons, calls tools, accumulates new context, and reasons again. The loop continues until the Agent calls a tool to stop itself or the user stops it directly.\n"),
    Page(None, "multi-agent-architecture/action-sequence.mdx", "Action Sequence", "Use action sequences to split complex goals into executable steps.", "As an extension of ReAct, The One provides a built-in tool set called Action Sequence.\n\nReAct lets an Agent act toward a goal and gradually approach it. But for complex tasks, chasing the final goal directly often makes a model repeatedly hit the same dead end. The One's answer is to let an Agent break a large task into a path of smaller action goals. That path is the Action Sequence.\n"),
    Page(
        None,
        "multi-agent-architecture/evolution.mdx",
        "From Single Agent to Multi-Agent",
        "Why complex tasks need multiple Agents with clear roles and clean context.",
        """## Why Multi-Agent is inevitable

A single Agent is mainly a context engineering problem. For complex tasks, Multi-Agent architecture is necessary because it keeps each Agent's context clean.

For example, software development includes product thinking, architecture, implementation, testing, operations, and review. One Agent should not carry all these identities at once. That violates the basic requirement that an Agent must know clearly who it is.

Complex tasks also contain independent subtasks. Each subtask should be handled by an Agent that only sees the information needed for that subtask. Letting one Agent read everything and do everything pollutes context and wastes capacity.

Agents are not real people. You can create more Agents by copying and shaping context. For decomposable work, this improves execution efficiency and reduces unnecessary token consumption.

## Concept mapping

### From ReAct to paired Agents

ReAct asks one Agent to review the current state after every action and reason again.

In Multi-Agent architecture, another Agent can take the reviewer role. This creates a paired-Agent pattern. In practice, the structure does not need to be rigid: a reviewer can continue the next part of the work and communicate with other Agents as the Graph evolves.
""",
    ),
    Page(None, "multi-agent-architecture/more-possibilities.mdx", "More Possibilities in Multi-Agent", "Capabilities that single-Agent systems cannot naturally provide.", "Multi-Agent systems have unique properties and possibilities that a single Agent cannot provide on its own.\n"),
    Page(None, "multi-agent-architecture/communication.mdx", "Communication", "The main ways Agents communicate in The One.", "The One provides three major ways for Agents to communicate:\n\n1. An Agent can actively call a handoff tool and transfer work to another Agent connected by an edge.\n\n2. Agents can communicate indirectly by reading and writing files in the same workspace.\n\n3. Through the Task Board tool, an Agent can start multiple sub-Agents in parallel, wait for them to finish, and then wake the main Agent with their results.\n"),
    Page(None, "multi-agent-architecture/context-editing.mdx", "Context Editing", "Agents can edit another Agent's context inside a Graph.", "Inside a Graph, if an Agent has the right tool permission, it can edit another Agent's context and reshape that Agent's working mind. Used carefully, this can improve task performance.\n"),
    Page(None, "multi-agent-architecture/dynamic-graph.mdx", "Dynamic Graph", "Agents can dynamically create, clone, activate, or suspend other Agents.", "Inside a Graph, if an Agent is given the right tool permissions, it can create, clone, activate, or suspend other Agents. This allows the Graph to expand dynamically during execution.\n"),
    Page(None, "the-one-app/definition-space.mdx", "Definition Space", "The core repository for Multi-Agent resources in The One.", "A Definition Space manages composable Multi-Agent resources:\n\n1. Prompt and Skill modules.\n2. Tool and MCP modules.\n3. Custom Agent presets.\n4. Multi-Agent Graph blueprints built by connecting different Agents with communication edges.\n"),
    Page(
        None,
        "the-one-app/profile.mdx",
        "Profile",
        "Write, import, and reuse Prompt / Skill modules.",
        """Use Profile to write or import Prompts and Skills that you reuse often.

When writing Prompts, do not cram everything into one huge Prompt. Agent editing supports combining multiple Prompts, so smaller and more reusable modules are usually better.

![Interface screenshot](./assets/image-20260531112259-64q0yuf.png)

To import a Skill, provide the repository address and Skill name.

For example, if a Skill site gives this command:

```powershell
npx skills add https://github.com/anthropics/skills --skill frontend-design
```

You should enter `source=https://github.com/anthropics/skills` and `skill=frontend-design`.

![Interface screenshot](./assets/image-20260531112630-h7jm5th.png)
""",
        asset_source="The One应用操作/仓储（definition space）/profile.md",
    ),
    Page(None, "the-one-app/mcp.mdx", "MCP", "Import and manage common MCP tools.", "Import and manage the MCP tools you use often. The workflow is similar to other modern AI Agent applications.\n\n![Interface screenshot](./assets/image-20260531112816-ehzidx6.png)\n", asset_source="The One应用操作/仓储（definition space）/mcp.md"),
    Page(None, "the-one-app/agent.mdx", "Agent", "Create Agent presets with independent models, prompts, and tools.", "In The One's Multi-Agent system, every Agent has independent configuration: model, prompt, and tools. That is why different Agents can take sharply different roles.\n\nStart by creating your first Agent:\n\n1. Give the Agent a clear name.\n2. Choose the model it should use.\n3. Select Prompt / Skill / MCP modules and optional supplemental Prompt.\n4. Select built-in tools, which determine the Agent's orchestration capability inside the Graph and its ability to interact with human users.\n\n{{video:Agent Creation Demonstration.mp4|Agent creation demo}}\n"),
    Page(None, "the-one-app/graph.mdx", "Graph", "Build a runnable and observable Multi-Agent Graph with nodes and edges.", "Every node you add to a Graph is a live LLM Agent and must be bound to an Agent preset.\n\nEdges are not fixed pipeline routes. They represent permitted communication channels between Agents. Agents not connected by an edge cannot directly communicate or hand off work. Connected Agents can communicate and transfer state, but they do not have to do so. The actual behavior depends on Agent judgment and user instruction during runtime.\n\nEdge descriptions are visible to Agents, helping them understand what the Agent on the other side is responsible for.\n\n{{video:Graph Editing Demonstration.mp4|Graph editing demo}}\n"),
    Page(None, "the-one-app/run.mdx", "Run", "Choose a workspace path and Graph, then start a transparent Multi-Agent run.", "Like other AI Agent desktop applications, you choose a run path, select a Graph blueprint, and start interacting.\n\nThe difference is visibility: in The One, you can clearly see the order and style of Agent interactions, plus the full context of each Agent.\n\n{{video:Simple operation demonstration.mp4|Run demo}}\n"),
    Page(None, "the-one-app/settings.mdx", "Settings", "Manage account, Definition Spaces, API providers, and desktop runtime.", "Use Settings to manage your account, Definition Spaces, API configuration, desktop runtime status, updates, diagnostics, and backend controls.\n"),
    Page(None, "the-one-app/space-management.mdx", "Space Management", "Create, switch, import, export, and share Definition Spaces.", "You can have any number of Definition Spaces. Spaces are independent and do not contaminate each other. At any moment, only one Space is active for editing or running.\n\nYou can download Spaces from the official sharing platform or upload your own Space:\n\n![Interface screenshot](./assets/image-20260531110342-nmrxz3j.png)\n\nYou can also import and export Spaces through local files:\n\n![Interface screenshot](./assets/image-20260531110227-ieaik90.png)\n", asset_source="The One应用操作/设置/仓储SPACE管理.md"),
    Page(None, "the-one-app/api-configuration.mdx", "API Configuration", "Configure official model service, third-party API keys, OAuth, and OpenAI-compatible providers.", "The One supports multiple connection methods for official model providers, including API keys and subscription-member OAuth flows.\n\nIt also supports custom OpenAI-compatible providers through a base URL.\n\n![Interface screenshot](./assets/image-20260531110505-gbh5a37.png)\n", asset_source="The One应用操作/设置/api配置.md"),
    Page(
        None,
        "start/release-notes/index.mdx",
        "Release Notes",
        "Public release notes for The One Desktop.",
        """This section collects public release notes for The One Desktop.

- [0.2.0](./0-2-0): Provider integration, Definition Spaces, sharing platform, and Graph terminology.
- [0.1.0](./0-1-0): The first desktop release with the repository, editor, runtime, and observation loop.
""",
    ),
    Page("开始/release notes/0.2.0/英文版.md", "start/release-notes/0-2-0.mdx", "The One 0.2.0 Release Notes", "0.2.0 adds provider integration, Definition Spaces, sharing, and Graph terminology."),
    Page("开始/release notes/0.1.0/英文版.md", "start/release-notes/0-1-0.mdx", "The One 0.1.0 Release Notes", "0.1.0 is the first complete desktop release of The One."),
]


def ensure_inside_repo(path: Path) -> None:
    resolved = path.resolve()
    root = ROOT.resolve()
    if root not in (resolved, *resolved.parents):
        raise RuntimeError(f"拒绝操作仓库外路径：{resolved}")


def read_source(relative_path: str) -> str:
    path = SOURCE_ROOT / relative_path
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


def clean_markdown(text: str, page: Page, locale: str) -> str:
    text = text.replace("\ufeff", "").replace("\u200d", "").strip()

    if page.source == "开始/模型与价格.md":
        marker = "# The One 支持的模型渠道与收费方式"
        text = text[text.index(marker) :]

    if page.source and "release notes" in page.source:
        text = re.sub(r"^#\s*(中文版|英文版)\s*", "", text).strip()
        text = re.sub(r"^已基于.*?release notes，不暴露实现细节。\s*", "", text, flags=re.S).strip()

    lines = text.splitlines()
    if lines and lines[0].lstrip().startswith("# "):
        lines = lines[1:]
    text = "\n".join(lines).strip()

    if locale == "zh":
        text = clean_zh_text(text)

    text = replace_video_placeholders(text, locale)
    text = rewrite_image_references(text, locale)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def clean_zh_text(text: str) -> str:
    replacements = {
        "mluti-agent": "Multi-Agent",
        "multi-agent": "Multi-Agent",
        "multi agent": "Multi-Agent",
        "Multi-Agents": "Multi-Agent",
        "agents": "Agent",
        "Agents": "Agent",
        "agent": "Agent",
        "graph": "Graph",
        "llm": "LLM",
        "api": "API",
        "space": "Space",
        "SPACE": "Space",
        "ai Agent": "AI Agent",
        "ai agent": "AI Agent",
        "AI Agent desktop软件": "AI Agent 桌面端应用",
        "AI Agent desktop 软件": "AI Agent 桌面端应用",
        "The One是": "The One 是",
        "在The One": "在 The One",
        "从The One": "从 The One",
        "Agent预设": "Agent 预设",
        "Graph蓝图": "Graph 蓝图",
        "prompt/skill/mcp": "Prompt / Skill / MCP",
        "prompt/skill": "Prompt / Skill",
        "prompt": "Prompt",
        "skill": "Skill",
        "mcp": "MCP",
        "tool": "Tool",
        "链接：下载The One": "前往官网下载 The One 安装包。",
        "如pm": "如 PM",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"(?m)^(\d+)\.(\S)", r"\1. \2", text)
    return add_cjk_latin_spacing(text)


def add_cjk_latin_spacing(text: str) -> str:
    text = re.sub(r"([\u4e00-\u9fff])([A-Za-z0-9])", r"\1 \2", text)
    text = re.sub(r"([A-Za-z0-9])([\u4e00-\u9fff])", r"\1 \2", text)
    return text


def image_replacement(locale: str) -> str:
    alt = "界面截图" if locale == "zh" else "Interface screenshot"
    return rf"![{alt}](/docs-assets/images/\1)"


def rewrite_image_references(text: str, locale: str) -> str:
    text = re.sub(r"!\[image\]\(assets/([^)]+)\)", image_replacement(locale), text)
    text = re.sub(r"!\[([^\]]+)\]\(\./assets/([^)]+)\)", r"![\1](/docs-assets/images/\2)", text)
    return text


def replace_video_placeholders(text: str, locale: str) -> str:
    labels = {
        "zh": {
            "Agent Creation Demonstration.mp4": "Agent 创建演示",
            "Graph Editing Demonstration.mp4": "Graph 编辑演示",
            "Simple operation demonstration.mp4": "运行演示",
            "Warehouse interface display.mp4": "仓储界面演示",
            "Display of the operation interface.mp4": "运行界面演示",
        },
        "en": {
            "Agent Creation Demonstration.mp4": "Agent creation demo",
            "Graph Editing Demonstration.mp4": "Graph editing demo",
            "Simple operation demonstration.mp4": "Run demo",
            "Warehouse interface display.mp4": "Repository interface demo",
            "Display of the operation interface.mp4": "Runtime interface demo",
        },
    }[locale]

    for filename, label in labels.items():
        text = re.sub(rf"此处插入视频\s*{re.escape(filename)}", video_block(filename, label), text)
        text = text.replace(f"{{{{video:{filename}|{label}}}}}", video_block(filename, label))
    return text


def video_block(filename: str, label: str) -> str:
    encoded = filename.replace(" ", "%20")
    return f"""<figure>
  <video controls preload="metadata" aria-label="{label}" style={{{{ width: "100%", borderRadius: 12 }}}}>
    <source src="/docs-assets/videos/{encoded}" type="video/mp4" />
  </video>
  <figcaption>{label}</figcaption>
</figure>"""


def frontmatter(page: Page) -> str:
    return f"---\ntitle: {page.title}\ndescription: {page.description}\n---\n\n"


def output_relative_path(page: Page) -> str:
    return OUTPUT_REMAP.get(page.output, page.output)


def copy_page_assets(source_relative: str, output_path: Path) -> None:
    source_file = SOURCE_ROOT / source_relative
    source_dir = source_file.parent
    raw_text = source_file.read_text(encoding="utf-8")
    asset_names = re.findall(r"!\[image\]\(assets/([^)]+)\)", raw_text)
    if not asset_names:
        return

    PUBLIC_IMAGE_ROOT.mkdir(parents=True, exist_ok=True)
    for asset_name in asset_names:
        src = source_dir / "assets" / asset_name
        if not src.exists():
            raise FileNotFoundError(src)
        shutil.copy2(src, PUBLIC_IMAGE_ROOT / asset_name)


def copy_video_assets() -> None:
    source_root = ROOT / "resources"
    PUBLIC_VIDEO_ROOT.mkdir(parents=True, exist_ok=True)
    for filename in VIDEO_FILES:
        src = source_root / filename
        if not src.exists():
            raise FileNotFoundError(src)
        shutil.copy2(src, PUBLIC_VIDEO_ROOT / filename)


def write_page(locale_root: Path, page: Page, locale: str) -> None:
    output_path = locale_root / output_relative_path(page)
    ensure_inside_repo(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if page.asset_source:
        copy_page_assets(page.asset_source, output_path)

    if page.literal is not None:
        body = rewrite_image_references(replace_video_placeholders(page.literal.strip(), locale), locale) + "\n"
    elif page.source is not None:
        copy_page_assets(page.source, output_path)
        body = clean_markdown(read_source(page.source), page, locale)
    else:
        raise RuntimeError(f"页面缺少内容源：{page.output}")

    output_path.write_text(frontmatter(page) + body, encoding="utf-8", newline="\n")


def write_meta(locale_root: Path, meta_files: dict[str, dict]) -> None:
    for relative_path, data in meta_files.items():
        path = locale_root / relative_path
        ensure_inside_repo(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def replace_content_docs() -> None:
    ensure_inside_repo(CONTENT_ROOT)
    if CONTENT_ROOT.exists():
        shutil.rmtree(CONTENT_ROOT)
    CONTENT_ROOT.mkdir(parents=True, exist_ok=True)


def replace_public_assets() -> None:
    ensure_inside_repo(PUBLIC_ASSET_ROOT)
    if PUBLIC_ASSET_ROOT.exists():
        shutil.rmtree(PUBLIC_ASSET_ROOT)
    PUBLIC_ASSET_ROOT.mkdir(parents=True, exist_ok=True)


def validate_video_resources() -> None:
    resources = ROOT / "resources"
    missing = [name for name in VIDEO_FILES if not (resources / name).exists()]
    if missing:
        raise FileNotFoundError(f"缺少视频资源：{missing}")


def main() -> None:
    validate_video_resources()
    replace_content_docs()
    replace_public_assets()
    copy_video_assets()

    locales = {
        "zh": (CONTENT_ROOT / "zh", ZH_PAGES, ZH_META),
        "en": (CONTENT_ROOT / "en", EN_PAGES, EN_META),
    }

    for locale, (locale_root, pages, meta_files) in locales.items():
        locale_root.mkdir(parents=True, exist_ok=True)
        for page in pages:
            write_page(locale_root, page, locale)
        write_meta(locale_root, meta_files)


if __name__ == "__main__":
    main()
