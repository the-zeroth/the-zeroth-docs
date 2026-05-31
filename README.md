<div align="center">
  <img src="./app_icon.png" alt="The One app icon" width="96" />

  <h1>The Zeroth</h1>

  <p>
    <strong>The official public home for The Zeroth and The One Desktop.</strong>
  </p>

  <p>
    <a href="https://the-zeroth.com">Website</a>
    |
    <a href="#english">English</a>
    |
    <a href="#zh">中文</a>
    |
    <a href="https://github.com/rainyflash/the-zeroth-docs/releases">Releases</a>
  </p>
</div>

---

<a id="english"></a>

## English

The Zeroth is the brand and product ecosystem. The One is the desktop agent application: a local-first workspace for designing, running, and observing real multi-agent workflows.

This repository is the only public-facing repository for The Zeroth. It is the canonical public source for documentation and The One Desktop release information.

### What lives here

- Public documentation content used by the official website.
- Release notes and public release metadata for The One Desktop.
- Locale-first MDX content for English and Chinese documentation.
- Navigation metadata for the documentation site.

### What does not live here

- Product source code.
- Private infrastructure.
- Internal implementation details.
- Secrets, credentials, or deployment-only configuration.

### The One Desktop

The One lets users create reusable agent presets, compose them into visual blueprints, execute workflows inside local workspaces, and inspect agent communication, context, tool calls, and handoffs while runs are active.

Every public The One Desktop release will be published in this repository in sync with the official website.

### Documentation structure

Documentation lives in `content/docs`:

```text
content/docs
+-- en/          English documentation
+-- zh/          Chinese documentation
`-- */meta.json  Navigation groups and page ordering
```

### Content stack

- MDX for documentation pages.
- Fumadocs-compatible `meta.json` files for navigation structure.
- Locale-first directory layout for multilingual content.

---

<a id="zh"></a>

## 中文

The Zeroth 是品牌与产品生态名称。The One 是真正的桌面端 Agent 应用：一个本地优先的工作空间，用于设计、运行和观察真实的多 Agent 工作流。

这个仓库是 The Zeroth 唯一对外公开的 repository。它是公开文档和 The One Desktop 发布信息的权威来源。

### 这里存放什么

- 官网使用的公开文档内容。
- The One Desktop 的 release notes 与公开发布元信息。
- 面向英文和中文文档的 locale-first MDX 内容。
- 文档站导航结构与页面排序信息。

### 这里不存放什么

- 产品源码。
- 私有基础设施。
- 内部实现细节。
- 密钥、凭证或仅用于部署的私有配置。

### The One Desktop

The One 允许用户创建可复用的 Agent 预设，将它们编排成可视化 Blueprint，在本地工作空间中执行工作流，并在运行期间观察 Agent 消息、上下文、工具调用和 handoff。

每一个公开的 The One Desktop 版本，都将在这个仓库中与官网同步发布。

### 文档结构

文档位于 `content/docs`：

```text
content/docs
+-- en/          英文文档
+-- zh/          中文文档
`-- */meta.json  导航分组与页面排序
```

### 内容技术栈

- 使用 MDX 编写文档页面。
- 使用兼容 Fumadocs 的 `meta.json` 管理导航结构。
- 使用 locale-first 目录结构支持多语言内容。
