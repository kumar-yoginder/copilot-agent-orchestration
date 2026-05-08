# Directory Structure Guide — Framework Organization

> When to load: Read when adding new files, directories, or features. Architect maintains this structure—consult before implementing structural changes.

---

## 📂 Complete Framework Directory Tree

```
multi-agent-framework/
├── SKILL.md                       # Skill entrypoint with frontmatter
├── agents/                        # Agent definitions (4 files)
│   ├── architect.md               # Systems architect agent
│   ├── developer.md               # Code quality & refactoring agent
│   ├── security.md                # Security audit agent
│   └── memory.md                  # State management agent
├── references/                    # Documentation (loaded on demand)
│   ├── SETUP.md                   # Quick start guide
│   ├── CUSTOMIZATION.md           # Domain adaptation guide
│   ├── AGENTS.md                  # Agent specifications & patterns
│   ├── NAMING_CONVENTIONS.md      # Naming standards (AUTHORITY: @architect)
│   ├── DIRECTORY_STRUCTURE.md     # Directory organization (THIS FILE)
│   ├── INDEX.md                   # Complete file reference
│   ├── MEMORIES.md                # Project state log (auto-maintained)
│   ├── MEMORY_TEMPLATE.md         # MEMORIES.md template
│   └── AGENT_TOOLS_UPDATE.md      # Update history & tool changes
├── assets/                        # Static files (HTML, templates, fonts)
│   └── (empty for now)
├── scripts/                       # Executable helpers (Python, Shell)
│   └── (empty for now)
└── templates/                     # Example projects (outside skill)
    ├── python-data-pipeline/
    └── fastapi-web-service/
```

---

## 🏗️ Skill Folder Structure

### `SKILL.md` — Entry Point

**Purpose:** Main skill documentation with YAML frontmatter and triggering phrases.

**Required Fields:**
```yaml
name: multi-agent-framework
description: |
  Use when you need to...
  Triggers: "set up agents", "design system architecture"...
```

---

### `agents/` Directory

**Purpose:** Agent instruction files (one per agent role)

**Files:**
```
agents/
├── architect.md      # System design & directory authority
├── developer.md      # Code quality & refactoring
├── security.md       # Vulnerability & compliance audit
└── memory.md         # State management & coordination
```

**Rules:**
- One agent per file (no combining roles)
- Filenames are lowercase agent names: `.md` (not `.agent.md`)
- Pure instruction format (no code, no prose)
- Each file must have: Role, Inputs, Process, Output format, Guidelines

---

### `references/` Directory

**Purpose:** Reference documentation loaded on demand

**Files:**
- `SETUP.md` — Setup instructions
- `CUSTOMIZATION.md` — Domain adaptation examples
- `AGENTS.md` — Agent specifications & interaction patterns
- `NAMING_CONVENTIONS.md` — Naming standards
- `DIRECTORY_STRUCTURE.md` — This file
- `INDEX.md` — Complete file reference
- `MEMORIES.md` — Project state log (auto-maintained)
- `MEMORY_TEMPLATE.md` — Template for MEMORIES.md
- `AGENT_TOOLS_UPDATE.md` — Change history

**Rules:**
- Each file starts with `> When to load:` callout
- Markdown only (`.md` extension)
- Naming: `UPPERCASE_WITH_UNDERSCORES.md`
- Include table of contents if > 300 lines

---

### `assets/` Directory

**Purpose:** Static files used in output (HTML templates, fonts, etc.)

**Status:** Currently empty (ready for future template files)

**Future Usage:**
- HTML templates for document generation
- Font files (if custom fonts needed)
- PNG/SVG images or diagrams
- Configuration templates

---

### `scripts/` Directory

**Purpose:** Executable helper scripts (Python, Shell, etc.)

**Status:** Currently empty (ready for future automation)

**Future Usage:**
- Python: `run_eval.py`, `package_skill.py`, validation scripts
- Shell: `setup.sh`, `deploy.sh`, deployment automation
- Other: Language-appropriate executables

**Rules:**
- Every script needs `--help` or docstring
- Scripts accept `--output` argument if producing files
- No prose instructions in scripts (those go in SKILL.md or agents/)
- Include `__init__.py` in scripts/ if adding Python files

---

## 📋 Reference Files — When to Load

| File | When to Load | What It Contains |
|------|---|---|
| `SETUP.md` | Initializing the framework for a new project | Step-by-step setup instructions |
| `CUSTOMIZATION.md` | Adapting framework for specific domain | Domain-specific examples & placeholders |
| `AGENTS.md` | Understanding agents and their workflows | Agent roles, tools, interaction patterns |
| `NAMING_CONVENTIONS.md` | Creating new files or code elements | Naming standards for all code/docs |
| `DIRECTORY_STRUCTURE.md` | Adding new files/directories | Folder organization rationale |
| `MEMORY_TEMPLATE.md` | Initializing MEMORIES.md | Template with sections to fill |
| `INDEX.md` | Getting complete file overview | All files and their purposes |
| `AGENT_TOOLS_UPDATE.md` | Reviewing recent agent changes | Tool allocation changes & rationale |

---

## 🎯 Skill Activation

When used as a skill in Copilot Chat:

1. **Trigger phrases** in `SKILL.md` description activate the skill
2. **Agents** in `agents/` folder become available as `@architect`, `@developer`, etc.
3. **References** are loaded on-demand when skill explains them
4. **Templates** show example customizations

---

## ✅ Validation Checklist

**For the restructured skill:**

- [x] `SKILL.md` exists at root with YAML frontmatter
- [x] `agents/` contains 4 files: `architect.md`, `developer.md`, `security.md`, `memory.md`
- [x] `references/` contains all doc files with "When to load" callouts
- [x] Agent files have: Role, Inputs, Process, Output format, Guidelines
- [x] Reference files have "When to load" callouts + table of contents (if >300 lines)
- [x] `assets/` folder exists (empty for now)
- [x] `scripts/` folder exists (empty for now)
- [x] No stray `.md` files at skill root (all in `references/`)
- [x] No code or prose in `agents/` files
- [x] All paths updated from `docs/` to `references/`

---

**Framework Version:** 1.0.0  
**Canonical Layout Version:** 1.0.0  
**Last Updated:** 8 May 2026  
**Authority:** @architect agent
