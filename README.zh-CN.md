<div align="center">
  <img src="./app_icon.png" alt="The One 应用图标" width="96" />

  <h1>The Zeroth Docs</h1>

  <p>
    <strong>The One Desktop 的公开双语文档仓库。</strong>
  </p>

  <p>
    <a href="./README.md">English</a>
    |
    <strong>简体中文</strong>
  </p>

  <p>
    <a href="https://the-zeroth.com">官网</a>
    |
    <a href="https://github.com/rainyflash/the-zeroth-docs/releases">发布记录</a>
  </p>
</div>

---

## 仓库作用

这个仓库用于维护 The Zeroth 官网使用的 The One Desktop 公开双语文档。

这里存放的是面向用户的文档内容、发布记录、截图和演示视频资源，不存放产品源码、私有基础设施、内部实现细节、密钥或部署专用配置。

## 文档结构

正式文档位于 `content/docs/zh` 和 `content/docs/en`。两种语言使用相同 slug，站点可以基于同一路由结构做语言切换。

```text
content/docs
+-- zh/                            中文文档
|   +-- index.mdx                  入口页
|   +-- start/                     快速入门、模型价格与发布记录
|   |   `-- release-notes/         版本发布记录
|   +-- the-one-app/               The One 应用操作
|   |   +-- definition-space/      Profile、MCP、Agent 与 Graph
|   |   +-- run/                   运行入口
|   |   `-- settings/              Space 与 API 配置
|   `-- multi-agent-architecture/  Multi-Agent 工程思想
|       +-- single-agent/          模型、工具、上下文、ReAct、行动链
|       +-- evolution/             从单一 Agent 到 Multi-Agent
|       `-- more-possibilities/    通讯、上下文编辑、Dynamic Graph
`-- en/                            English documentation
    +-- index.mdx                  Entry page
    +-- start/                     Quick start, pricing, and release notes
    |   `-- release-notes/         Release note versions
    +-- the-one-app/               The One app guide
    |   +-- definition-space/      Profile, MCP, Agent, and Graph
    |   +-- run/                   Runtime entry
    |   `-- settings/              Space and API configuration
    `-- multi-agent-architecture/  Multi-Agent architecture
        +-- single-agent/          Model, tools, context, ReAct, action sequence
        +-- evolution/             From single Agent to Multi-Agent
        `-- more-possibilities/    Communication, context editing, dynamic Graph
```

## 草稿与资源

- `docs_md`：新文档草稿来源。
- `resources`：文档中引用的视频资源。
- `public/docs-assets/images`：文档页面使用的截图资源。
- `public/docs-assets/videos`：文档页面使用的演示视频资源。

## 生成方式

文档由 `scripts/migrate_docs_md.py` 从 `docs_md` 迁移生成：

```powershell
python scripts\migrate_docs_md.py
```

脚本会删除旧的 `content/docs` 占位内容，重新生成 `zh` / `en` 双语文档树，复制截图和视频到 `public/docs-assets`，并把草稿中的图片与视频占位替换为可部署访问的 `/docs-assets/...` 引用。

## 维护原则

- 中英文文档必须保持相同 slug，避免语言切换时路由漂移。
- 面向用户的表达放进 `content/docs`，原始草稿放进 `docs_md`。
- 截图和视频必须走 `public/docs-assets`，不要在页面里引用本地草稿路径。
- 不要在这个仓库提交产品源码、密钥、内部架构细节或部署专用配置。

## 内容边界

The One 是一款为 Multi-Agent 架构设计的桌面应用，用来搭建、运行、观察和迭代多智能体系统。

这个仓库只负责公开文档表达。真正的桌面端实现、后端服务、账号系统、模型调用实现和内部编排逻辑都不在这里。
