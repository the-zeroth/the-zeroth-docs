<div align="center">
  <img src="./app_icon.png" alt="The One app icon" width="96" />

  <h1>The Zeroth Docs</h1>

  <p>
    <strong>The public bilingual documentation repository for The One Desktop.</strong>
  </p>

  <p>
    <strong>English</strong>
    |
    <a href="./README.zh-CN.md">简体中文</a>
  </p>

  <p>
    <a href="https://the-zeroth.com">Website</a>
    |
    <a href="https://github.com/rainyflash/the-zeroth-docs/releases">Releases</a>
  </p>
</div>

---

## Purpose

This repository maintains the public bilingual documentation for The One Desktop on The Zeroth website.

It contains user-facing documentation, release notes, screenshots, and demo videos. It does not contain product source code, private infrastructure, internal implementation details, secrets, or deployment-only configuration.

## Documentation Structure

The canonical documentation lives under `content/docs/en` and `content/docs/zh`. Both languages use the same slugs so the website can switch languages without route drift.

```text
content/docs
+-- en/                            English documentation
|   +-- index.mdx                  Entry page
|   +-- start/                     Quick start, pricing, and release notes
|   |   `-- release-notes/         Release note versions
|   +-- the-one-app/               The One app guide
|   |   +-- definition-space/      Profile, MCP, Agent, and Graph
|   |   +-- run/                   Runtime entry
|   |   `-- settings/              Space and API configuration
|   `-- multi-agent-architecture/  Multi-Agent architecture
|       +-- single-agent/          Model, tools, context, ReAct, action sequence
|       +-- evolution/             From single Agent to Multi-Agent
|       `-- more-possibilities/    Communication, context editing, dynamic Graph
`-- zh/                            Chinese documentation
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

## Drafts and Assets

- `docs_md`: source drafts for new documentation.
- `resources`: video assets referenced by the documentation.
- `public/docs-assets/images`: screenshots used by documentation pages.
- `public/docs-assets/videos`: demo videos used by documentation pages.

## Generation

Documentation is generated from `docs_md` by `scripts/migrate_docs_md.py`:

```powershell
python scripts\migrate_docs_md.py
```

The script removes the old `content/docs` placeholder content, regenerates the `en` / `zh` bilingual documentation trees, copies screenshots and videos into `public/docs-assets`, and rewrites draft image and video placeholders into deployable `/docs-assets/...` references.

## Maintenance Rules

- English and Chinese documents must keep matching slugs so language switching stays stable.
- User-facing content belongs in `content/docs`; raw drafts belong in `docs_md`.
- Screenshots and videos must be served from `public/docs-assets`; pages should not reference local draft paths.
- Do not commit product source code, secrets, internal architecture details, or deployment-only configuration to this repository.

## Scope

The One is a desktop application designed for Multi-Agent architecture. It helps users build, run, observe, and iterate on multi-agent systems.

This repository is only responsible for public documentation. The desktop implementation, backend services, account system, model-call implementation, and internal orchestration logic are outside this repository.
