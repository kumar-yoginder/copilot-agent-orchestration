# Multi-Agent Framework — Project State

> When to load: Read at the start of every session to understand framework state, recent changes, and next steps. Updated by @memory-controller.

---

## 📋 Framework Status

**Status:** ✅ Ready for Use  
**Version:** 1.0.0 (Canonical Layout)  
**Last Updated:** 8 May 2026

---

## 🎯 Completed Milestones

### ✅ Framework Structure Canonicalized
- **Date:** 8 May 2026
- **Changes:** Restructured entire framework into canonical skill layout
  - Created `SKILL.md` with YAML frontmatter and triggering phrases
  - Moved agents to `agents/` folder (architect.md, developer.md, security.md, memory.md)
  - Moved docs to `references/` folder with "When to load" callouts
  - Created empty `assets/` and `scripts/` folders for future expansion
- **Status:** ✅ Complete
- **Files Modified:** 13 files restructured
- **Files Created:** 9 new reference files

### ✅ Agent Tool Allocation Optimized
- **Date:** 8 May 2026
- **Changes:** Applied least-privilege principle to agent tools
  - Architect: `search/codebase` only (analyzes, proposes designs)
  - Developer: `edit`, `search/codebase` (understands, then refactors)
  - Security: `search/codebase` only (audits, reports findings)
  - Memory: `edit` only (maintains MEMORIES.md state)
- **Impact:** Clear role separation, reduced unintended side effects
- **Status:** ✅ Complete

### ✅ Naming Conventions Established
- **Date:** 8 May 2026
- **Authority:** @architect agent
- **Contents:** 
  - File naming (UPPERCASE_WITH_UNDERSCORES for docs, snake_case for code)
  - Code naming per language (Python, TypeScript, Java, Go)
  - Directory naming (snake_case or kebab-case)
  - Anti-patterns and examples
- **File:** `references/NAMING_CONVENTIONS.md` (~400 lines)
- **Status:** ✅ Complete

### ✅ Directory Structure Formalized
- **Date:** 8 May 2026
- **Authority:** @architect agent
- **Contents:**
  - Complete directory tree
  - Responsibility per directory
  - Language-specific organization
  - Rules for adding features
  - Authority checklist
- **File:** `references/DIRECTORY_STRUCTURE.md` (~400 lines)
- **Status:** ✅ Complete

---

## 📁 Current Folder Structure

```
multi-agent-framework/
├── SKILL.md                 # Entrypoint with frontmatter ✅
├── agents/                  # 4 agent files ✅
│   ├── architect.md
│   ├── developer.md
│   ├── security.md
│   └── memory.md
├── references/              # 9 reference files ✅
│   ├── SETUP.md
│   ├── CUSTOMIZATION.md
│   ├── AGENTS.md
│   ├── NAMING_CONVENTIONS.md
│   ├── DIRECTORY_STRUCTURE.md
│   ├── MEMORY_TEMPLATE.md
│   ├── AGENT_TOOLS_UPDATE.md
│   ├── INDEX.md
│   └── MEMORIES.md (this file)
├── assets/                  # Empty (ready for future) ✅
├── scripts/                 # Empty (ready for future) ✅
└── templates/               # Example projects (outside skill)
    ├── python-data-pipeline/
    └── fastapi-web-service/
```

---

## 🏗️ Architectural Decisions

### [8 May 2026] Canonical Skill Layout Adopted
- **Decision:** Restructure framework as canonical skill (SKILL.md, agents/, references/, assets/, scripts/)
- **Rationale:** Follows Claude skills system conventions; clear separation of concerns; scalable structure
- **Implementation:**
  - SKILL.md: Entrypoint with triggering phrases
  - agents/: Agent instruction files (one per role)
  - references/: Documentation (on-demand loading with "When to load" callouts)
  - assets/: Static files (HTML templates, fonts) — ready for expansion
  - scripts/: Helper scripts (Python, Shell) — ready for expansion
- **Impact:** Professional skill structure; compliant with best practices; ready for distribution
- **Status:** ✅ Implemented

### [8 May 2026] Separation of Concerns in References
- **Decision:** Each reference file addresses one concern with "When to load" callout
- **Rationale:** Users load only what they need; clearer navigation; better token usage
- **Files:**
  - SETUP.md — For initial setup
  - CUSTOMIZATION.md — For domain adaptation
  - AGENTS.md — For understanding agents
  - NAMING_CONVENTIONS.md — For naming files/code
  - DIRECTORY_STRUCTURE.md — For organizing folders
  - MEMORY_TEMPLATE.md — For initializing MEMORIES.md
  - AGENT_TOOLS_UPDATE.md — For understanding tool allocation
  - INDEX.md — For overview
  - MEMORIES.md — For framework state
- **Status:** ✅ Implemented

---

## 📝 Framework Inventory

### Agent Files (4)
- ✅ `agents/architect.md` — Systems architect (design, naming authority, directory authority)
- ✅ `agents/developer.md` — Code quality (refactoring protocol, language-specific rules)
- ✅ `agents/security.md` — Security researcher (vulnerability scanning, compliance)
- ✅ `agents/memory.md` — Memory controller (state management, coordination)

### Reference Files (9)
- ✅ `references/SETUP.md` — Quick start guide (6 setup steps + best practices)
- ✅ `references/CUSTOMIZATION.md` — Domain adaptation (4 detailed examples: Python ETL, FastAPI, K8s, ML)
- ✅ `references/AGENTS.md` — Agent specifications (roles, tools, workflows, best practices)
- ✅ `references/NAMING_CONVENTIONS.md` — Naming standards (directories, code, anti-patterns)
- ✅ `references/DIRECTORY_STRUCTURE.md` — Directory organization (rules, authority, checklist)
- ✅ `references/MEMORY_TEMPLATE.md` — MEMORIES.md template (sections for tasks, decisions, etc.)
- ✅ `references/AGENT_TOOLS_UPDATE.md` — Tool allocation history (least-privilege rationale)
- ✅ `references/INDEX.md` — Complete file reference (navigation, quick lookup)
- ✅ `references/MEMORIES.md` — Framework state (this file)

### Skill Root Files (1)
- ✅ `SKILL.md` — Entrypoint (YAML frontmatter, triggering phrases, agent overview)

### Empty Folders (Ready for Expansion)
- ✅ `assets/` — For HTML templates, fonts, images (when needed)
- ✅ `scripts/` — For Python, Shell, automation helpers (when needed)

---

## 🎯 Triggering Phrases (in SKILL.md)

Framework activates on phrases like:
- "Set up multi-agent framework"
- "Create coding agents"
- "Design system architecture"
- "Establish naming conventions"
- "Refactor code for quality"
- "Audit for security vulnerabilities"
- etc.

---

## ✅ Quality Assurance Checks

**Skill Structure:**
- [x] SKILL.md exists with YAML frontmatter (name, description)
- [x] Description includes specific triggering phrases
- [x] Description mentions output format
- [x] SKILL.md body < 500 lines (under limit)

**Agent Files:**
- [x] 4 agents in agents/ folder (architect, developer, security, memory)
- [x] Each file has Role section
- [x] Each file has Inputs/Responsibilities section
- [x] Each file has Process section
- [x] Each file has Output format section
- [x] Each file lists Tools available
- [x] No code in agent files (pure instruction)

**Reference Files:**
- [x] 9 reference files in references/ folder
- [x] Each has "When to load" callout at top
- [x] No duplicate content between files
- [x] All > 300 lines include table of contents
- [x] Naming: UPPERCASE_WITH_UNDERSCORES.md

**Folder Structure:**
- [x] assets/ folder exists (ready for templates)
- [x] scripts/ folder exists (ready for helpers)
- [x] No stray .md, .py, .html files at skill root
- [x] All paths use references/ (not docs/)

---

## 🚀 Next Steps

### For Users:
1. ✅ Copy skill folder to your VS Code extensions
2. ✅ Read `references/SETUP.md` for initialization
3. ✅ Customize `.project-config.yaml` for your domain
4. ✅ Invoke `@architect`, `@developer`, `@security`, `@memory-controller` in Copilot Chat
5. ✅ Reference docs as needed (each has "When to load" callout)

### For Future Enhancement:
- ⏳ Add HTML templates to `assets/` (when needed for report generation)
- ⏳ Add Python scripts to `scripts/` (when automation helpers needed)
- ⏳ Create additional domain-specific templates in `templates/`
- ⏳ Expand examples in `references/CUSTOMIZATION.md` as new domains tested

---

## 📊 Framework Statistics

| Aspect | Value | Notes |
|--------|-------|-------|
| **Agents** | 4 | Architect, Developer, Security, Memory |
| **Reference Docs** | 9 | All with "When to load" callouts |
| **Skill Folders** | 5 | agents/, references/, assets/, scripts/, templates/ |
| **Total Skill Files** | 14 | SKILL.md + 4 agents + 9 references |
| **Example Projects** | 2 | Python ETL, FastAPI API |
| **Canonical Layout** | ✅ Yes | Fully compliant with Claude skills system |

---

## 📞 Framework Status Summary

✅ **Restructuring:** COMPLETE (8 May 2026)  
✅ **Canonical Layout:** ACHIEVED  
✅ **Documentation:** COMPREHENSIVE  
✅ **Agent Configuration:** OPTIMIZED (least privilege)  
✅ **Standards:** ESTABLISHED (naming, directory structure)  
✅ **Validation:** PASSED (all checklist items)  

**Status:** 🚀 **READY FOR USE**

---

**Framework Version:** 1.0.0  
**Layout Version:** Canonical 1.0.0  
**Last Updated:** 8 May 2026  
**Maintained By:** @memory-controller
