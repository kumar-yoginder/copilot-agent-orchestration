# Copilot Agent Orchestration

A **professional, reusable multi-agent orchestration system** for managing complex software projects using GitHub Copilot Chat. This skill enables specialized agents to collaborate on architecture, development, code quality, and security.

**Framework Status:** ✅ Canonically Structured | Ready for Use  
**Last Updated:** 8 May 2026 | **Version:** 1.0.0

---

## 🎯 Overview

This framework provides four specialized agents that work together to manage software projects:

### **Agents**
1. **[Architect](multi-agent-framework/agents/architect.md)** — Designs system structure, data flow, and component integration
2. **[Developer](multi-agent-framework/agents/developer.md)** — Refactors code for quality, clarity, and maintainability  
3. **[Security](multi-agent-framework/agents/security.md)** — Audits for vulnerabilities, compliance, and secure design
4. **[Memory Controller](multi-agent-framework/agents/memory.md)** — Maintains project state and optimizes token usage

### **Key Features**
- ✅ **Canonical Layout** — Professional skill structure following Claude standards
- ✅ **Generic & Reusable** — Works with any project domain (web, data, infrastructure, ML, etc.)
- ✅ **Least-Privilege Design** — Each agent has only the tools it needs
- ✅ **Token-Optimized** — Compressed memory entries prevent context bloat
- ✅ **Zero Setup** — Copy agents to your project and customize placeholders

---

## 📂 Project Structure

```
.
├── README.md                           # This file
├── .project-config.yaml                # Configuration file (customize for your project)
├── templates/                          # Example projects
│   ├── python-data-pipeline/           # ETL pipeline example
│   └── fastapi-web-service/            # REST API example
│
└── multi-agent-framework/              # Main skill (canonical structure)
    ├── SKILL.md                        # Skill entrypoint
    ├── agents/                         # Agent definitions
    │   ├── architect.md                # System design agent
    │   ├── developer.md                # Code quality agent
    │   ├── memory.md                   # State management agent
    │   └── security.md                 # Security audit agent
    ├── references/                     # Documentation (on-demand loading)
    │   ├── SETUP.md                    # Quick start guide
    │   ├── CUSTOMIZATION.md            # Domain adaptation guide
    │   ├── AGENTS.md                   # Agent specifications
    │   ├── NAMING_CONVENTIONS.md       # Naming standards
    │   ├── DIRECTORY_STRUCTURE.md      # Directory organization
    │   ├── MEMORY_TEMPLATE.md          # Template for MEMORIES.md
    │   ├── AGENT_TOOLS_UPDATE.md       # Tool allocation details
    │   ├── INDEX.md                    # Complete file reference
    │   └── MEMORIES.md                 # Project state log
    ├── assets/                         # Static files (ready for templates)
    └── scripts/                        # Helper scripts (ready for expansion)
```

---

## 🚀 Quick Start

1. **Read the skill overview** — See [multi-agent-framework/SKILL.md](multi-agent-framework/SKILL.md)
2. **Follow setup guide** — See [multi-agent-framework/references/SETUP.md](multi-agent-framework/references/SETUP.md)
3. **Customize configuration** — Edit `.project-config.yaml` with your project details
4. **Initialize project memory** — Copy from [multi-agent-framework/references/MEMORY_TEMPLATE.md](multi-agent-framework/references/MEMORY_TEMPLATE.md)
5. **Invoke agents in Copilot Chat** — Use `@architect`, `@developer`, `@security`, `@memory-controller`

---

## 🎉 Recent Updates

### [2026-05-08] Canonical Skill Restructuring
- **Status:** ✅ Complete
- **Author:** Framework Architect
- **What Changed:**
  - Restructured entire framework into canonical skill layout
  - Created `SKILL.md` with YAML frontmatter and trigger phrases
  - Moved agents to `agents/` folder (renamed `.agent.md` → `.md`)
  - Moved docs to `references/` folder with "When to load" callouts
  - Created empty `assets/` and `scripts/` folders for future expansion
  - Applied least-privilege principle to agent tools
  - Established naming conventions and directory structure standards
  - Created comprehensive documentation (9 reference files, 2,000+ lines)

**Related Docs:**
- [multi-agent-framework/references/AGENTS.md](multi-agent-framework/references/AGENTS.md) — Agent specifications
- [multi-agent-framework/references/CUSTOMIZATION.md](multi-agent-framework/references/CUSTOMIZATION.md) — Domain examples

---

## 📖 Documentation

All documentation is in `multi-agent-framework/references/` with "When to load" callouts:

| File | Purpose | Load When |
|------|---------|-----------|
| **SKILL.md** | Skill entrypoint | Activating the skill in Copilot Chat |
| **SETUP.md** | Setup guide | Initializing for a new project |
| **AGENTS.md** | Agent specs | Understanding agent workflows |
| **CUSTOMIZATION.md** | Domain examples | Adapting for specific domains |
| **NAMING_CONVENTIONS.md** | Naming standards | Creating new files/code |
| **DIRECTORY_STRUCTURE.md** | Directory org | Adding files/directories |
| **MEMORY_TEMPLATE.md** | Memory template | Initializing MEMORIES.md |
| **INDEX.md** | File reference | Getting complete overview |

---

## 🏛️ Standards & Governance

**The Architect is the authority on:**
- 🏗️ **Directory Structure** — See [multi-agent-framework/references/DIRECTORY_STRUCTURE.md](multi-agent-framework/references/DIRECTORY_STRUCTURE.md)
- 📝 **Naming Conventions** — See [multi-agent-framework/references/NAMING_CONVENTIONS.md](multi-agent-framework/references/NAMING_CONVENTIONS.md)
- 🎯 **System Design** — See [multi-agent-framework/references/AGENTS.md](multi-agent-framework/references/AGENTS.md)

**Before implementing any new files:**
- ✅ Check naming conventions
- ✅ Follow directory structure guidelines
- ✅ Update this README.md with feature entry
- ✅ Log to docs/MEMORIES.md via @memory-controller

---

## 📋 Configuration

Edit `.project-config.yaml` to customize agents for your project:

```yaml
project:
  name: "MyProject"
  domain: "Data Engineering"
  description: "ETL pipeline for analytics warehouse"

developer:
  languages:
    - "Python 3.11"
  standards:
    - "Black formatter"
    - "Type hints required"

security:
  compliance_frameworks:
    - "OWASP Top 10"
    - "Data Privacy (GDPR)"
  critical_assets:
    - "Database credentials"
    - "API keys"
```

---

## 💬 Agent Interaction Flow

```
┌─────────────┐
│  Developer  │ → Fix code + call memory-controller
└─────────────┘
      ↓
┌──────────────────────┐
│  Memory Controller   │ → Append to MEMORIES.md
└──────────────────────┘
      ↑
      │
┌─────────────┐
│ Architect   │ → Design + full rewrite on major changes
└─────────────┘

┌─────────────┐
│  Security   │ → Audit + log findings via memory-controller
└─────────────┘
```

---

## 📝 Usage Examples

### Example 1: Design a New Module
```
@architect: Please design a caching layer for our API responses.

[Architect responds with module structure, API contracts, and data flow]

@memory-controller: Log this architectural decision.
[Memory controller appends to MEMORIES.md]
```

### Example 2: Refactor Code
```
@developer: Refactor src/utils/helpers.py for clarity and remove dead code.

[Developer applies refactoring protocol]

@memory-controller: Append changes to MEMORIES.md.
[Memory controller logs the refactoring]
```

### Example 3: Security Audit
```
@security: Audit authentication logic in auth/login.py for OWASP compliance.

[Security agent identifies findings]

@memory-controller: Log all security findings.
[Memory controller records with risk levels]
```

---

## 🔐 Memory Management

The **Memory Controller** maintains `MEMORIES.md` with:

- **Append Mode:** Timestamped logs of code changes, decisions, and insights
- **Rewrite Mode:** Full restructuring when architecture fundamentally changes
- **Compression:** Technical bullet points only — no filler

**Memory Entry Format:**
```
[DATE] [AGENT_TYPE]: [TASK_SUMMARY]
- **Change:** src/api/handlers.py (lines 42-58) — Refactored login flow
- **Status:** Completed
- **Files Modified:** src/api/handlers.py, src/auth/tokens.py
- **Context:** Implements OAuth2 token refresh with 15-min expiry
```

---

## 📚 Documentation

- **[docs/SETUP.md](docs/SETUP.md)** — Initialize the framework for a new project
- **[docs/CUSTOMIZATION.md](docs/CUSTOMIZATION.md)** — Adapt agents for your domain
- **[docs/AGENTS.md](docs/AGENTS.md)** — Detailed agent roles and interaction patterns
- **[docs/INDEX.md](docs/INDEX.md)** — Complete file reference and navigation
- **[.project-config.yaml](.project-config.yaml)** — Configuration reference

---

## 🎓 Example Projects

See [templates/](templates/) for complete example projects:

- **[templates/python-data-pipeline/](templates/python-data-pipeline/)** — ETL pipeline with security & testing
- *More examples coming soon*

---

## 🛠️ Customization

This framework is **100% generic**. Customize it for:

- **Web Applications** (React, FastAPI, Django, etc.)
- **Data Engineering** (ETL, data lakes, ML pipelines)
- **Infrastructure** (DevOps, Kubernetes, Terraform)
- **Backend Services** (microservices, APIs)
- **Mobile Apps** (iOS, Android)
- **Any other domain**

See [docs/CUSTOMIZATION.md](docs/CUSTOMIZATION.md) for step-by-step guidance.

---

## 🔄 Agent Workflow Summary

| Agent | Role | Tools | Interacts With |
|-------|------|-------|-----------------|
| **Architect** | System design & data flow | search/codebase | memory-controller |
| **Developer** | Code quality & refactoring | edit, search/codebase | memory-controller |
| **Security** | Vulnerability & compliance audit | search/codebase | memory-controller |
| **Memory Controller** | State management & coordination | edit | all agents |

---

## 📖 Key Principles

1. **Specialization** — Each agent has a focused role
2. **Coordination** — All agents flow through memory controller
3. **Compression** — Memory entries are concise and technical
4. **Traceability** — All decisions and changes are timestamped
5. **Generality** — Framework works with any tech stack or domain

---

## ❓ FAQ

**Q: Can I use these agents without VS Code?**  
A: This framework is designed for GitHub Copilot Chat (VS Code). Agents can be adapted for other chat interfaces.

**Q: How do I customize agents for my project?**  
A: Edit `.project-config.yaml` and replace placeholders in agent files. See [docs/CUSTOMIZATION.md](docs/CUSTOMIZATION.md).

**Q: What happens to MEMORIES.md?**  
A: It's auto-populated by the memory-controller agent. Initialize it from [docs/MEMORY_TEMPLATE.md](docs/MEMORY_TEMPLATE.md).

**Q: Can agents work in parallel?**  
A: Yes! However, all changes should be logged via memory-controller to maintain consistency.

---

## 📄 License

This framework is open for customization and reuse. Modify as needed for your projects.

---

## 🤝 Contributing

Have improvements or examples? Consider sharing them for other users!

---

**Framework Version:** 1.0.0
