---
name: multi-agent-framework
description: |
  Use when you need to establish a multi-agent system for software projects.
  
  **Trigger phrases:** "Set up multi-agent framework", "Create coding agents", "Design system architecture", "Establish naming conventions", "Manage project state", "Refactor code for quality", "Audit security vulnerabilities", "coordinate agents for my project"
  
  **What it does:** Provides 4 specialized agents (Architect, Developer, Security, Memory) that collaborate on code design, quality, security, and state management. Each agent has clear responsibilities and tool access following least-privilege principle.
  
  **Output:** Agents available in Copilot Chat (@architect, @developer, @security, @memory-controller) ready to work on your project. Framework setup guide and customization examples for any domain (web, data, infrastructure, ML, etc.).
---

# Multi-Agent Framework for Copilot Chat

A **professional, reusable multi-agent orchestration system** for managing complex software projects using GitHub Copilot Chat. This skill enables specialized agents to collaborate on architecture, development, code quality, and security.

---

## 🎯 What This Skill Provides

### **4 Specialized Agents**

1. **@architect** — Systems design, directory structure, naming authority
   - Designs system components and data flow
   - Establishes naming conventions and directory standards
   - Proposes architectural decisions with full documentation
   
2. **@developer** — Code quality and refactoring
   - Enforces comprehensive refactoring protocol (9 categories)
   - Applies language-specific best practices
   - Logs all code changes for audit trail
   
3. **@security** — Vulnerability detection and compliance
   - Audits code against OWASP Top 10, CWE, and compliance frameworks
   - Identifies security risks and data protection issues
   - Classifies findings by risk level (Critical/High/Medium/Low)
   
4. **@memory-controller** — State management and coordination
   - Maintains project state in `MEMORIES.md`
   - Coordinates all agents and their outputs
   - Optimizes context to prevent token bloat

---

## 🚀 Quick Start

### **Step 1: Activate Framework**
Invoke the skill in Copilot Chat:
```
@architect: Design a user authentication module for our API
```

### **Step 2: Read Setup Guide**
See `references/SETUP.md` for:
- Prerequisites and file copying
- Configuration (`.project-config.yaml`)
- Agent customization for your domain
- Agent activation and usage
- Startup prompt for automatic placeholder replacement
- Best practices and typical workflows

### **Step 3: Invoke Agents**
Work with agents in Copilot Chat:
```
@architect:         Design system structure
@developer:         Refactor code for quality
@security:          Audit for vulnerabilities
@memory-controller: Log all changes
```

### **Step 4: Consult References**
Each reference file has a "When to load" callout:
- **SETUP.md** — Setting up the framework
- **RELEASE.md** — Downloading and installing release bundle into existing projects
- **CUSTOMIZATION.md** — Adapting for your domain
- **AGENTS.md** — Understanding agent workflows
- **NAMING_CONVENTIONS.md** — Naming files and code
- **DIRECTORY_STRUCTURE.md** — Organizing folders
- **And more...**

---

## 🌟 Key Features

### ✅ **Generic & Reusable**
- Works with **any project domain** (web, data, infrastructure, ML, etc.)
- Works with **any programming language** (Python, TypeScript, Java, Go, etc.)
- Zero setup — copy agents and customize placeholders

### ✅ **Least-Privilege Design**
- Each agent has **minimal required tools**
- Architect: analyzes & designs (read-only)
- Developer: understands & implements (read + write)
- Security: audits & reports (read-only)
- Memory: manages state (write to MEMORIES.md only)

### ✅ **Clear Role Boundaries**
- No overlapping responsibilities
- Each agent is authority in its domain (e.g., Architect owns naming conventions)
- Coordinated workflows prevent conflicts

### ✅ **Token-Optimized**
- Memory controller compresses context
- Prevent token bloat with "Append vs. Rewrite" mode
- Bootstrap from latest state in MEMORIES.md

### ✅ **Professional Structure**
- Canonical skill layout (SKILL.md, agents/, references/, assets/, scripts/)
- Comprehensive documentation with "When to load" callouts
- Ready for distribution and reuse

---

## 📂 Skill Structure

```
multi-agent-framework/
├── SKILL.md                       # This entrypoint
├── agents/                        # 4 agent definitions
│   ├── architect.md               # System design authority
│   ├── developer.md               # Code quality authority
│   ├── security.md                # Security audit authority
│   └── memory.md                  # State management authority
├── references/                    # On-demand documentation
│   ├── SETUP.md                   # Quick start guide
│   ├── CUSTOMIZATION.md           # Domain adaptation (4 examples)
│   ├── AGENTS.md                  # Agent specifications
│   ├── NAMING_CONVENTIONS.md      # Naming standards
│   ├── DIRECTORY_STRUCTURE.md     # Directory organization
│   ├── MEMORY_TEMPLATE.md         # MEMORIES.md template
│   ├── AGENT_TOOLS_UPDATE.md      # Tool allocation
│   ├── INDEX.md                   # File reference
│   └── MEMORIES.md                # Framework state
├── assets/                        # Static files (templates, fonts)
└── scripts/                       # Helper scripts (Python, Shell)
```

---

## 🏗️ Agent Roles & Responsibilities

### **@architect** — Senior Systems Architect

**Role:** Design system structure, data flow, API contracts

**Responsibilities:**
- Define high-level module structure and organization
- Design API contracts and communication patterns
- Plan data flow between components
- **Authority:** Naming conventions and directory structure
- Evaluate design patterns (MVC, microservices, event-driven, etc.)
- Make trade-offs between scalability, maintainability, simplicity

**Tools Available:** `search/codebase` (analyzes, doesn't edit)

**Output:** Design proposals, API contracts, data flow diagrams, architectural decisions

---

### **@developer** — Senior Developer

**Role:** Code quality, refactoring, maintainability

**Responsibilities:**
- Apply comprehensive refactoring protocol (formatting, dead code, logic, clarity, OOP, access control, documentation, coverage)
- Enforce language-specific boilerplate (Python, TypeScript, Java, Go, etc.)
- Ensure all code paths are reachable and tested
- Log all changes via memory controller

**Tools Available:** `edit`, `search/codebase` (understand code, then refactor)

**Output:** Refactored code, quality improvements, change documentation

---

### **@security** — Security Researcher

**Role:** Vulnerability detection, compliance, secure design

**Responsibilities:**
- Audit code against **OWASP Top 10**, CWE Top 25, NIST, compliance frameworks
- Identify injection points, XSS, broken authentication, insecure deserialization
- Flag hardcoded credentials, weak crypto, unsafe dependencies
- Review access control (RBAC), authentication/authorization
- Audit data validation and encryption
- Check supply chain security (dependencies, versions)

**Tools Available:** `search/codebase` (audits & reports, doesn't fix)

**Output:** Security findings, compliance reports, risk classifications, audit checklists

---

### **@memory-controller** — Memory & State Controller

**Role:** State management, inter-agent coordination, token optimization

**Responsibilities:**
- Maintain `MEMORIES.md` as single source of truth
- Manage Append vs. Rewrite modes for memory updates
- Compress context to prevent token bloat
- Track architectural decisions, code changes, security findings
- Provide context snapshots to agents on request
- Enable seamless agent handoffs

**Tools Available:** `edit` (updates MEMORIES.md state only)

**Output:** Updated project state, compressed context, agent coordination

---

## 🔄 Typical Workflow

```
1. User asks @architect to design a feature
   ↓
   Architect: Consults memory for current state
   ↓
   Architect: Proposes system design with APIs and data flow
   ↓
   User: "Log this decision"
   
2. User asks @developer to implement
   ↓
   Developer: Searches code to understand structure
   ↓
   Developer: Implements & refactors per protocol
   ↓
   Developer: Reports changes
   
3. @memory-controller: Appends to MEMORIES.md
   ↓
   Timestamps + file changes + status
   
4. User asks @security to audit
   ↓
   Security: Audits against OWASP/compliance
   ↓
   Security: Reports findings with risk levels
   
5. @memory-controller: Logs security findings
   ↓
   Cycle continues: architect → developer → security → memory
```

---

## 📚 Reference Files (On-Demand)

Each reference file includes a "When to load" callout. Read only what you need:

| File | When to Load | Key Content |
|------|---|---|
| **SETUP.md** | Initializing framework for new project | 6-step setup, configuration, activation |
| **RELEASE.md** | Installing from downloadable release | Copy/paste steps + startup prompt for placeholder replacement |
| **CUSTOMIZATION.md** | Adapting for specific domain | 4 detailed examples (Python ETL, FastAPI, K8s, ML), placeholders |
| **AGENTS.md** | Understanding agents & workflows | Roles, tools, interaction patterns, best practices |
| **NAMING_CONVENTIONS.md** | Naming new files/code | Directory patterns, language-specific rules, anti-patterns |
| **DIRECTORY_STRUCTURE.md** | Adding files/directories | Folder organization, responsibility, authority checklist |
| **MEMORY_TEMPLATE.md** | Initializing MEMORIES.md | Sections for tasks, decisions, changes, security, snapshots |
| **AGENT_TOOLS_UPDATE.md** | Understanding tool allocation | Least-privilege rationale, tool restrictions |
| **INDEX.md** | Getting complete overview | All files, purposes, navigation guide |
| **MEMORIES.md** | Starting session | Framework state, decisions, inventory |

---

## 💡 Key Principles

### 🏛️ **Authority & Governance**
- **@architect** owns: Naming conventions, directory structure, system design
- **@developer** owns: Code quality, refactoring protocol, implementation
- **@security** owns: Vulnerability audit, compliance checks, risk classification
- **@memory-controller** owns: Project state, coordination, context management

### 🔐 **Least Privilege**
- Each agent has **only the tools it needs**
- Architect designs (read-only); Developer implements (read + write)
- Security audits (read-only); Memory updates state (write-only)
- **Result:** No overlapping responsibilities, cleaner workflows

### 📝 **State Management**
- Single source of truth: `MEMORIES.md`
- Append mode for incremental changes
- Rewrite mode for architectural pivots
- Compressed entries prevent token bloat

### 🤝 **Coordination**
- Agents always consult memory before working
- All changes logged for audit trail
- Handoffs between agents are seamless
- Context preserved for next agent

---

## 🎯 Use Cases

### ✅ **New Project Setup**
- `@architect`: Design initial system structure
- `@memory-controller`: Log architectural decisions
- `@developer`: Set up boilerplate code
- Result: Well-structured project ready for development

### ✅ **Code Quality Initiative**
- `@developer`: Refactor entire codebase per protocol
- `@memory-controller`: Log all improvements
- Result: Higher code quality, better maintainability

### ✅ **Security Audit**
- `@security`: Audit against OWASP/compliance
- `@memory-controller`: Log all findings
- `@developer`: Fix security issues
- Result: More secure codebase

### ✅ **Architecture Review**
- `@architect`: Review current design against best practices
- `@memory-controller`: Log architectural improvements
- `@developer`: Refactor to new design
- Result: Improved, scalable architecture

### ✅ **Domain Adaptation**
- Read `references/CUSTOMIZATION.md` for your domain
- Customize `.project-config.yaml` with domain-specific settings
- Invoke agents with domain context
- Result: Framework optimized for your project type

---

## 🚀 Getting Started

1. **Read** `references/SETUP.md` — Step-by-step initialization
2. **Copy** agent files to your project (or use from this skill)
3. **Customize** `.project-config.yaml` for your domain
4. **Initialize** `MEMORIES.md` from `references/MEMORY_TEMPLATE.md`
5. **Invoke** agents in Copilot Chat:
   ```
   @architect: Design...
   @developer: Refactor...
   @security: Audit...
   @memory-controller: Log changes
   ```

---

## 📖 Read Next

- **New to this skill?** → `references/SETUP.md`
- **Need domain examples?** → `references/CUSTOMIZATION.md`
- **Understand agents?** → `references/AGENTS.md`
- **Complete reference?** → `references/INDEX.md`
- **Check framework state?** → `references/MEMORIES.md`

---

## ✅ Skill Validation

- ✅ Canonical layout (SKILL.md, agents/, references/, assets/, scripts/)
- ✅ 4 specialized agents with clear role boundaries
- ✅ Comprehensive documentation with "When to load" callouts
- ✅ Least-privilege tool allocation per agent
- ✅ Professional structure ready for distribution
- ✅ Example projects and domain customization guides
- ✅ Backup created before restructuring

---

**Skill Version:** 1.0.0  
**Canonical Layout:** ✅ Compliant  
**Status:** 🚀 Ready for Use  
**Last Updated:** 8 May 2026
