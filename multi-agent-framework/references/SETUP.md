# Setup Guide — Multi-Agent Framework

> When to load: Read when initializing the framework for a new project. Follow step-by-step instructions to copy, configure, and activate agents.

---

## 📋 Prerequisites

- GitHub Copilot Chat (VS Code)
- A project directory (new or existing)
- Familiarity with your project's tech stack

---

## ✅ Step 1: Copy Framework Files

Copy all files from this framework to your project root:

```
your-project/
├── .project-config.yaml
├── MEMORIES.md
├── README.md
├── agents/
│   ├── architect.md
│   ├── developer.md
│   ├── memory.md
│   └── security.md
└── your-existing-code/
```

---

## ⚙️ Step 2: Customize `.project-config.yaml`

Replace all `{{PLACEHOLDER}}` values with your project details:

```yaml
project:
  name: "MyAwesomeProject"                  # Your project name
  domain: "Web Development"                  # Your domain (e.g., DevOps, Data Engineering)
  description: "Fast API framework for real-time analytics"
  version: "1.0.0"
  created: "2026-05-08"

architect:
  focus_areas:
    - "API design and REST conventions"
    - "Database schema and ORM patterns"
    - "Async/await patterns for real-time data"

developer:
  languages:
    - "Python 3.11"
  code_style_guide: "PEP 8 + Black"
  standards:
    - "Type hints required"
    - "Docstrings for all functions"
    - "Unit tests for new code"

security:
  compliance_frameworks:
    - "OWASP Top 10"
  critical_assets:
    - "API authentication tokens"
    - "Database credentials"
  threat_model: "Prevent unauthorized API access and data leaks"
```

---

## 📝 Step 3: Initialize `MEMORIES.md`

Copy `references/MEMORY_TEMPLATE.md` to `MEMORIES.md` and customize:

```markdown
# MyAwesomeProject — Project Memory Log

**Framework:** Multi-Agent Orchestration  
**Initialized:** 2026-05-08  
**Architecture Version:** 1.0.0

## Active Tasks & Initiatives
- Build REST API for analytics dashboard
- Set up PostgreSQL database with ORM
- Implement JWT authentication

## Architectural Decisions
- Decision 1: Use FastAPI for async HTTP handling
- Decision 2: Use SQLAlchemy ORM for database abstraction
```

---

## 🎯 Step 4: Customize Agent Files (Optional)

Agent files work with placeholders. Replace `{{PLACEHOLDER}}` values:

### In `agents/architect.md`:
```markdown
## Domain Context
- **Project:** MyAwesomeProject
- **Domain:** Web Development
- **Key Focus Areas:** API design, database schema, security
```

### In `agents/developer.md`:
```markdown
## Domain Context
- **Project:** MyAwesomeProject
- **Primary Languages:** Python 3.11, SQL
- **Code Standards:** PEP 8, Black formatter, Type hints
```

### In `agents/security.md`:
```markdown
## Domain Context
- **Project:** MyAwesomeProject
- **Compliance Frameworks:** OWASP Top 10, NIST Cybersecurity
- **Critical Assets:** API tokens, user credentials, database
```

---

## 🚀 Step 5: Activate Agents in Copilot Chat

In VS Code Copilot Chat, agents are available via `@agent-name`:

```
@architect: Design a user authentication module for our API.

[Architect responds with structure and recommendations]

@developer: Refactor the payment processing code for clarity.

[Developer applies refactoring protocol and reports changes]

@security: Audit the authentication logic for OWASP compliance.

[Security agent identifies findings and risk levels]

@memory-controller: Log all changes to MEMORIES.md.

[Memory controller timestamps and records in project memory]
```

---

## 💾 Step 6: Maintain Project Memory

The memory controller automatically updates `MEMORIES.md`. To manually add entries:

```markdown
## Code Changes Log

[2026-05-08] [Developer]: Refactored user authentication module
- **Change:** src/auth/login.py (lines 1-80) — Implemented OAuth2 flow
- **Status:** Completed
- **Files Modified:** src/auth/login.py, src/auth/tokens.py
- **Context:** 15-minute JWT expiry, refresh token rotation enabled

[2026-05-08] [Architect]: Designed API versioning strategy
- **Change:** API routes use /v1/, /v2/ prefixes
- **Status:** Completed
- **Context:** Backward compatibility for 2 major versions
```

---

## 🎓 Step 7: Best Practices

### ✅ Do:
- **Consult memory before changes** — Always ask memory controller for current state
- **Log everything** — Keep MEMORIES.md updated with changes and decisions
- **Use append mode** — Log incremental changes; avoid large rewrites
- **Compress context** — Use technical bullet points, not conversational prose
- **Coordinate via memory** — All agents should check memory first

### ❌ Don't:
- **Overwrite memory manually** — Let agents manage it
- **Store conversational notes** — Keep memory technical and concise
- **Skip timestamps** — Always date-stamp entries
- **Ignore architectural decisions** — Log decisions for future reference
- **Let memory grow unbounded** — Trigger rewrites after ~10 appends

---

## 🔄 Typical Workflow

1. **Ask Architect** — "Design a new feature module"
2. **Architect responds** — Provides structure, APIs, and data flow
3. **Ask Memory Controller** — "Log this architectural decision"
4. **Memory appends** — Records decision with date and details
5. **Ask Developer** — "Implement the module and refactor for quality"
6. **Developer refactors** — Applies code quality protocol
7. **Ask Memory Controller** — "Append the implementation details"
8. **Memory logs** — Records files modified and status
9. **Ask Security** — "Audit for vulnerabilities"
10. **Security reports** — Identifies issues and risk levels
11. **Continue cycle** — Refactor, test, audit, repeat
