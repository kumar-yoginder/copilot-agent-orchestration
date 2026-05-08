# Release & Copy-Paste Setup Guide

> When to load: Read when downloading a release bundle and integrating this framework into an existing project.

---

## 1) Download the release bundle

1. Open the repository Releases page.
2. Download the latest `copilot-agent-framework-<version>.zip`.
3. Extract it locally.

---

## 2) Copy into your existing project

Copy these files/folders from the extracted bundle into your project root:

- `.project-config.yaml`
- `MEMORIES.md`
- `RELEASE.md`
- `multi-agent-framework/`

Your project should look like:

```text
your-existing-project/
├── .project-config.yaml
├── MEMORIES.md
├── multi-agent-framework/
│   ├── SKILL.md
│   ├── agents/
│   └── references/
└── ...your existing code...
```

---

## 3) Auto-fill placeholders using one startup prompt

Open Copilot Chat in your project and paste this prompt:

```text
Use .project-config.yaml as the single source of truth and replace all {{PLACEHOLDER}} values across:
- multi-agent-framework/SKILL.md
- multi-agent-framework/agents/*.md
- multi-agent-framework/references/*.md (only where placeholders exist)

Rules:
1) Do not change tool lists, role boundaries, or file structure.
2) Keep markdown formatting intact.
3) If a value is missing, ask me once with a short list of missing keys.
4) After replacement, give me a summary table: file, placeholders replaced, placeholders still pending.
```

---

## 4) Start using agents

After placeholders are filled:

```text
@architect: Read MEMORIES.md and design the next feature module.
@developer: Implement/refactor based on the architect output.
@security: Audit the implementation for OWASP risks.
@memory-controller: Append all outcomes to MEMORIES.md.
```

