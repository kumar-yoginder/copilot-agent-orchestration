# Multi-Agent Framework — Complete File Index

> When to load: Read to get a complete overview of all framework files and their purposes. Use for navigation and understanding the skill structure.

---

## 📋 Skill File Structure

```
multi-agent-framework/
│
├── SKILL.md                       # Skill entrypoint with triggering phrases
│
├── agents/                        # Agent definitions (one per file)
│   ├── architect.md               # Systems architect agent
│   ├── developer.md               # Senior developer agent
│   ├── security.md                # Security researcher agent
│   └── memory.md                  # Memory controller agent
│
├── references/                    # Reference documentation (on-demand loading)
│   ├── SETUP.md                   # Quick start guide
│   ├── RELEASE.md                 # Release download + copy/paste integration
│   ├── CUSTOMIZATION.md           # Domain adaptation guide
│   ├── AGENTS.md                  # Agent specifications & interaction patterns
│   ├── NAMING_CONVENTIONS.md      # Naming standards (authority: @architect)
│   ├── DIRECTORY_STRUCTURE.md     # Directory organization (authority: @architect)
│   ├── MEMORY_TEMPLATE.md         # Template for MEMORIES.md
│   ├── AGENT_TOOLS_UPDATE.md      # Tool allocation & changes
│   ├── INDEX.md                   # This file (complete reference)
│   └── MEMORIES.md                # Framework state log
│
├── assets/                        # Static files (for future use)
│   └── (empty for now)
│
└── templates/                     # Example projects (outside skill)
    ├── python-data-pipeline/      # ETL/Data Engineering example
    └── fastapi-web-service/       # REST API example
```

---

## 🎯 Skill Entrypoint

### **SKILL.md** — Main Skill File
- **Purpose:** Skill trigger phrases and main documentation
- **Contains:** YAML frontmatter with `name` and `description`, overview of agents and workflow
- **Usage:** This is what Copilot Chat reads to activate the skill
- **Key Content:**
  - Trigger phrases for skill activation
  - Overview of 4 agents and their roles
  - Key features and use cases
  - Pointers to reference files

---

## 🤖 Agent Files (4 total)

All agent files are in the `agents/` directory with detailed role descriptions, responsibilities, tools, and workflows.

### 1. **agents/architect.md** — Systems Architect
- **Role:** System design, data flow, structural decisions
- **Responsibilities:** Directory structure, API design, architectural decisions, naming authority
- **Tools:** `search/codebase` (analyze, don't edit)
- **Coordinates:** With memory-controller
- **Output:** Design proposals, structure diagrams, architectural decisions

### 2. **agents/developer.md** — Senior Developer
- **Role:** Code quality, refactoring, maintainability
- **Responsibilities:** Applies refactoring protocol (9 categories), enforces standards, language-specific boilerplate
- **Tools:** `edit`, `search/codebase` (understand code, then refactor)
- **Coordinates:** With memory-controller
- **Output:** Refactored code, quality improvements, change logs

### 3. **agents/security.md** — Security Researcher
- **Role:** Vulnerability detection, compliance, secure design
- **Responsibilities:** Access control audits, vulnerability scanning, data integrity checks, dependency security
- **Tools:** `search/codebase` (audit, don't edit)
- **Coordinates:** With memory-controller
- **Output:** Security findings, compliance reports, risk levels

### 4. **agents/memory.md** — Memory Controller
- **Role:** State management, inter-agent coordination, token optimization
- **Responsibilities:** Maintain MEMORIES.md, manage append/rewrite modes, compress context, coordinate agents
- **Tools:** `edit` (update MEMORIES.md only)
- **Coordinates:** All agents (orchestrator)
- **Output:** Updated project state, compressed context snapshots

---

## 📚 Reference Files (10 total)

All reference files are in the `references/` directory and include "When to load" callouts.

### Core Setup & Customization

| File | Purpose | Load When | Content |
|------|---------|-----------|---------|
| **SETUP.md** | Quick start guide | Setting up framework for new project | Prerequisites, file copying, configuration steps, agent activation, best practices |
| **RELEASE.md** | Release installation guide | Installing from downloadable release zip | Release download steps, copy/paste setup, startup placeholder prompt |
| **CUSTOMIZATION.md** | Domain adaptation guide | Adapting framework for specific domain | Placeholder reference, 4 examples (Python ETL, FastAPI, K8s, ML), customization checklist |

### Agent & Workflow Documentation

| File | Purpose | Load When | Content |
|------|---------|-----------|---------|
| **AGENTS.md** | Agent specifications | Understanding agents & workflows | Agent roles, responsibilities, tools, interaction patterns, workflow rules, best practices |
| **AGENT_TOOLS_UPDATE.md** | Tool allocation history | Reviewing agent capabilities | Tool changes, rationale, least-privilege principle, workflow impact |

### Standards & Organization

| File | Purpose | Load When | Content |
|------|---------|-----------|---------|
| **NAMING_CONVENTIONS.md** | Naming standards | Naming new files/code | Directory patterns, code conventions per language, anti-patterns, summary table |
| **DIRECTORY_STRUCTURE.md** | Directory organization | Adding files/features | Folder structure, responsibility per directory, rules, authority checklist |

### State & Templates

| File | Purpose | Load When | Content |
|------|---------|-----------|---------|
| **MEMORY_TEMPLATE.md** | MEMORIES.md template | Initializing project memory | Sections for tasks, decisions, changes, security, snapshots, questions |
| **MEMORIES.md** | Framework state log | Starting session | Current framework state, architectural decisions, documentation inventory |

### Reference & Navigation

| File | Purpose | Load When | Content |
|------|---------|-----------|---------|
| **INDEX.md** | Complete file reference | Getting overview of all files | File structure, descriptions, cross-references, reading order, quick reference |

---

## 🔄 How to Use This Skill

### **Step 1: Activate the Skill**
Trigger phrases in `SKILL.md` activate the skill:
- "Set up multi-agent framework"
- "Design system architecture with agents"
- "Create coding agents for my project"
- etc.

### **Step 2: Access Agents**
Once activated, agents are available:
- `@architect` — Design system structure
- `@developer` — Refactor code
- `@security` — Audit for vulnerabilities
- `@memory-controller` — Manage project state

### **Step 3: Reference Documentation**
As needed, read reference files:
- New to skill? → **SETUP.md** + **AGENTS.md**
- Adapting for domain? → **CUSTOMIZATION.md** + **NAMING_CONVENTIONS.md**
- Understanding structure? → **DIRECTORY_STRUCTURE.md** + **INDEX.md**
- Checking state? → **MEMORIES.md**

### **Step 4: Work with Agents**
Invoke agents in Copilot Chat:
```
@architect: Design a user authentication module

@developer: Refactor the payment processing code

@security: Audit for OWASP compliance

@memory-controller: Log all changes
```

---

## 📖 Recommended Reading Order

### **First Time Users:**
1. Read `SKILL.md` — Understand skill purpose
2. Skim `AGENTS.md` — Learn agent roles
3. Review `SETUP.md` — Follow setup steps
4. Check `CUSTOMIZATION.md` — Adapt for your domain

### **For Implementation:**
1. Read `AGENTS.md` — Full agent capabilities
2. Reference `NAMING_CONVENTIONS.md` — Check naming standards
3. Reference `DIRECTORY_STRUCTURE.md` — Plan directory layout
4. Keep `MEMORIES.md` updated — Log all decisions

### **For Troubleshooting:**
1. Check `AGENT_TOOLS_UPDATE.md` — Verify agent capabilities
2. Review `AGENTS.md` interaction section — Understand workflow
3. Check `MEMORIES.md` — See current state

---

## 🎯 Quick Reference Table

| Need | Reference | Section |
|------|-----------|---------|
| Set up framework | SETUP.md | All |
| Understand agents | AGENTS.md | All |
| Name new files | NAMING_CONVENTIONS.md | Code/File naming |
| Add directories | DIRECTORY_STRUCTURE.md | Directory rules |
| Adapt for domain | CUSTOMIZATION.md | Domain examples |
| Check current state | MEMORIES.md | All |
| Learn tool access | AGENT_TOOLS_UPDATE.md | Tool allocation |
| Initialize project | MEMORY_TEMPLATE.md | All |

---

## 📊 Framework Statistics

| Aspect | Count | Notes |
|--------|-------|-------|
| **Agents** | 4 | Architect, Developer, Security, Memory |
| **Agent Files** | 4 | One per agent in `agents/` |
| **Reference Files** | 10 | All in `references/` with "When to load" callouts |
| **Example Projects** | 2 | Python ETL, FastAPI |
| **Folders** | 5 | agents/, references/, assets/, scripts/, templates/ |
| **Total Files** | 15+ | Skill core files + templates |

---

## ✅ Skill Validation Checklist

- [x] `SKILL.md` exists at skill root with YAML frontmatter
- [x] 4 agent files in `agents/` folder (architect, developer, security, memory)
- [x] 10 reference files in `references/` folder with "When to load" callouts
- [x] Agent files have: Role, Responsibilities, Tools, Output format
- [x] Reference files organized by purpose (setup, agents, standards, state)
- [x] `assets/` folder exists (empty, ready for templates)
- [ ] `scripts/` folder exists (empty, ready for helpers)
- [x] All internal paths use `references/` (not `docs/`)
- [x] Clear separation: agents (pure instruction) vs. references (on-demand docs)
- [x] Canonical skill layout fully implemented

---

**Skill Version:** 1.0.0  
**Canonical Layout:** ✅ Canonical  
**Last Updated:** 8 May 2026  
**Status:** ✅ Ready for Use
