# Agent Tool Updates — Summary of Changes

> When to load: Read when understanding what tools each agent has access to and why those restrictions exist. Reference when troubleshooting agent capabilities.

**Updated:** 8 May 2026  
**Status:** ✅ Complete

---

## Overview

The agents have been reconfigured with optimized tool restrictions based on their actual responsibilities and workflow. Each agent now has only the tools it truly needs, following the **least privilege principle**.

---

## Tool Assignment Changes

### **Architect Agent**
**Role:** Systems design & architecture  
**Responsibility:** Propose, design, plan (not implement)

| Aspect | Before | After | Rationale |
|--------|--------|-------|-----------|
| Tools | `edit`, `search/codebase` | `search/codebase` | Architect should analyze and design, not edit code. Developer implements. |
| Agent Interaction | `memory-controller` | `memory-controller` | ✓ Unchanged |

**Updated File:** `agents/architect.md`

---

### **Developer Agent**
**Role:** Code refactoring & quality  
**Responsibility:** Understand code, then refactor

| Aspect | Before | After | Rationale |
|--------|--------|-------|-----------|
| Tools | `edit` | `edit`, `search/codebase` | Developer needs to search/understand code structure BEFORE refactoring. |
| Agent Interaction | `memory-controller` | `memory-controller` | ✓ Unchanged |

**Updated File:** `agents/developer.md`

---

### **Security Agent**
**Role:** Vulnerability auditing & compliance  
**Responsibility:** Audit and report (not fix)

| Aspect | Before | After | Rationale |
|--------|--------|-------|-----------|
| Tools | `edit`, `search/codebase` | `search/codebase` | Security agent audits and identifies issues. Developer fixes them. |
| Agent Interaction | `memory-controller` | `memory-controller` | ✓ Unchanged |

**Updated File:** `agents/security.md`

---

### **Memory Controller Agent**
**Role:** State management & coordination  
**Responsibility:** Update MEMORIES.md only

| Aspect | Before | After | Rationale |
|--------|--------|-------|-----------|
| Tools | `edit`, `search/codebase` | `edit` | Memory controller updates MEMORIES.md state. Can rely on agents to provide context. |
| Agents to Coordinate | N/A | N/A | ✓ No agent restrictions (orchestrator) |

**Updated File:** `agents/memory.md`

---

## Updated Files

### **Agent Files** (4 files)
- ✅ `agents/architect.md` — Tools: `search/codebase`
- ✅ `agents/developer.md` — Tools: `edit`, `search/codebase`
- ✅ `agents/security.md` — Tools: `search/codebase`
- ✅ `agents/memory.md` — Tools: `edit`

### **Documentation Files** (3 files)
- ✅ `references/AGENTS.md` — Updated "Tools Available" sections for each agent
- ✅ `references/SETUP.md` — Agent activation instructions
- ✅ `.project-config.yaml` — Updated `tool_restrictions` section with comments

---

## New Agent Tool Allocation Summary

```
ARCHITECT:  search/codebase only
            ↓
            Analyzes current system → Proposes design → Logs via memory

DEVELOPER:  edit + search/codebase
            ↓
            Reads code → Refactors → Notifies memory

SECURITY:   search/codebase only
            ↓
            Audits code → Identifies vulnerabilities → Logs findings via memory

MEMORY:     edit only
            ↓
            Updates MEMORIES.md → Coordinates agents
```

---

## Workflow Impact

### Before:
```
All agents had broad tool access, potential for overlapping responsibilities
```

### After:
```
Architect     → Analyzes & designs (search only)
Developer     → Understands & implements (edit + search)
Security      → Audits & reports (search only)
Memory        → Coordinates & logs (edit only)
```

**Result:** Clear separation of concerns with least privilege principle enforced.

---

## Key Benefits

✅ **Least Privilege** — Each agent has minimal required tools  
✅ **Clear Roles** — No overlapping responsibilities  
✅ **Better Coordination** — All changes flow through memory-controller  
✅ **Improved Security** — Architect can't accidentally edit code  
✅ **Cleaner Workflow** — Developer handles both analysis and implementation  

---

## Configuration Reference

### `.project-config.yaml` Tool Restrictions

```yaml
tool_restrictions:
  architect: ['search/codebase']           # Analyzes & designs, doesn't edit code
  developer: ['edit', 'search/codebase']   # Reads code, then refactors
  security: ['search/codebase']            # Audits code, reports findings (doesn't fix)
  memory: ['edit']                         # Updates MEMORIES.md state only
```

---

**Framework Version:** 1.0.0  
**Last Updated:** 8 May 2026  
**Authority:** @architect agent
