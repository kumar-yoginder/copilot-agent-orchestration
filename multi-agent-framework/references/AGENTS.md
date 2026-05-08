# Agent Specifications & Interaction Patterns

> When to load: Read to understand each agent's role, responsibilities, tools, and how they interact. Reference this when invoking agents or coordinating multi-agent workflows.

---

## 🏗️ Architect Agent

**File:** `agents/architect.md`

### Role
Senior Systems Architect — designs system structure, data flow, APIs, and component integration.

### Responsibilities

#### 1. **System Design**
- Define high-level module structure and organization
- Design API contracts and communication patterns
- Plan data flow between components

#### 2. **Architectural Decisions**
- Evaluate design patterns (MVC, microservices, event-driven, etc.)
- Make trade-offs between scalability, maintainability, and simplicity
- Document assumptions and constraints

#### 3. **Coordination & State Management**
- Before proposing changes: consult `@memory-controller` for current architecture
- On major changes: trigger **Full Rewrite** of `MEMORIES.md`
- On minor updates: request **Append** to memory

#### 4. **OOP & Design Principles**
- Single Responsibility Principle (SRP)
- DRY (Don't Repeat Yourself)
- SOLID principles
- Separation of Concerns

### Tools Available
- `search/codebase` — Understand current system structure before proposing designs

### Interaction Patterns

```
User: "Design a user authentication module"
     ↓
@architect: Proposes module structure, API contracts, data flow
     ↓
User: "Log this decision"
     ↓
@memory-controller: Records architectural decision with date/rationale
```

### Example Prompts

✅ **Good:**
```
@architect: Design a caching layer for API responses. Consider:
- Cache invalidation strategy
- Fallback behavior if cache is unavailable
- Integration with existing API routes
```

❌ **Poor:**
```
@architect: Make our API faster
```

---

## 👨‍💻 Developer Agent

**File:** `agents/developer.md`

### Role
Senior Developer — refactors code for quality, clarity, maintainability, and performance.

### Responsibilities

#### 1. **Code Quality Protocol**
The developer enforces comprehensive refactoring standards:

| Category | Standards |
|----------|-----------|
| **Formatting** | Consistent indentation, line length, spacing (per project style guide) |
| **Dead Code** | Remove unused variables, imports, functions, unreachable branches |
| **Logic & Syntax** | Fix bugs, broken control flows, logic errors |
| **Clean Code** | Strip non-ASCII characters, ensure UTF-8 encoding |
| **Documentation** | Grammar in comments, comprehensive docstrings, type hints |
| **OOP** | Small, single-responsibility classes and methods |
| **Access Control** | Least privilege — minimize visibility of internals |
| **Boilerplate** | Standard module structure, main guards, error handling |
| **Coverage** | All code paths reachable and ideally tested |

#### 2. **Language-Specific Implementation**

**Python:**
```python
if __name__ == "__main__":
    # Main execution
    pass
```

**TypeScript:**
```typescript
export async function main(): Promise<void> {
  // Main execution
}
```

**Java:**
```java
public class Main {
  public static void main(String[] args) {
    // Main execution
  }
}
```

### Tools Available
- `edit` — Refactor code and apply improvements
- `search/codebase` — Understand code before refactoring

### Interaction Patterns

```
User: "Refactor the authentication module"
     ↓
@developer: Reads code structure → Applies refactoring protocol
     ↓
@developer: Reports changes and notifies memory
     ↓
User: "Log these changes"
     ↓
@memory-controller: Records refactoring summary with file modifications
```

---

## 🔐 Security Agent

**File:** `agents/security.md`

### Role
Security Researcher & Compliance Officer — identifies vulnerabilities, audits code, and enforces compliance.

### Responsibilities

#### 1. **Vulnerability Scanning**
- Audit code against OWASP Top 10, CWE Top 25, NIST guidelines
- Identify injection points, XSS, broken authentication, insecure deserialization
- Flag hardcoded credentials, weak crypto, unsafe dependencies

#### 2. **Compliance & Standards**
- Verify adherence to configured compliance frameworks (HIPAA, SOC2, ISO 27001, etc.)
- Check data protection regulations (GDPR, CCPA)
- Audit logging and monitoring implementations

#### 3. **Access Control & IAM**
- Review RBAC and permission models
- Verify least privilege principle implementation
- Audit authentication/authorization logic

#### 4. **Dependency & Supply Chain Security**
- Scan third-party libraries for known CVEs
- Check version pinning and update policies
- Verify source integrity for dependencies

### Tools Available
- `search/codebase` — Audit code for vulnerabilities

### Audit Process

```
@security: Audit the authentication system for OWASP compliance
     ↓
[Security checks code against OWASP Top 10]
     ↓
[Identifies findings with Risk Levels: Critical/High/Medium/Low]
     ↓
@memory-controller: Log security findings and status
```

### Output Format

**Finding Template:**
```
**[RISK_LEVEL] Finding Title** — [COMPONENT]
- **Issue:** [Specific vulnerability description]
- **Impact:** [Potential consequences if exploited]
- **Recommendation:** [How to fix it]
- **Status:** [New/In Progress/Resolved]
```

---

## 🧠 Memory Controller Agent

**File:** `agents/memory.md`

### Role
Central orchestrator — manages project state, token optimization, and inter-agent coordination.

### Responsibilities

#### 1. **State Management**
- Maintain `MEMORIES.md` as single source of truth
- Track architectural decisions, code changes, security findings
- Compress and optimize context to prevent token bloat

#### 2. **Append vs. Rewrite Mode**
- **Append Mode:** Log incremental changes with timestamps
- **Rewrite Mode:** Full replacement when architect revises fundamental architecture

#### 3. **Agent Coordination**
- Provide compressed context snapshots to agents on request
- Track task status (Completed/Pending/Blocked)
- Prevent duplication of effort across agents

#### 4. **Token Budget Management**
- Monitor conversation length and token usage
- Trigger context flush when approaching limits
- Guide users to bootstrap from latest `MEMORIES.md` entry

### Tools Available
- `edit` — Update `MEMORIES.md` with new entries

### Memory Entry Format

```markdown
[DATE] [AGENT_TYPE]: [TASK_SUMMARY]
- **Change:** [Specific file + line range + what changed]
- **Status:** [Completed/Pending/Blocked]
- **Files Modified:** [List of paths]
- **Context:** [Key architectural/design details in 1-2 lines]
```

### Workflow

```
Multiple agents work on different tasks
     ↓
Each agent notifies memory controller when done
     ↓
@memory-controller: Appends all changes to MEMORIES.md
     ↓
MEMORIES.md serves as project context for subsequent agents
```

---

## 🔄 Agent Interaction Flow

```
┌─────────────────────────────────────────────────┐
│ User requests work (design, refactor, audit)   │
└────────────────────┬────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
    Architect     Developer     Security
    (Designs)     (Refactors)    (Audits)
        │            │            │
        └────────────┼────────────┘
                     │
              ▼─────────────┬──────────────┐
         Check Memory      │        Report Findings
         (current state)   │        to Memory
              │            │              │
              └────────────┼──────────────┘
                           │
                      ▼────▼────▼
                   Memory Controller
                   (Update MEMORIES.md)
                           │
                ┌──────────┴──────────┐
         Next Agent Task or    Final Project State
         Coordination          (Ready for deployment)
```

---

## 📋 Agent Workflow Rules

### Before any agent works:
1. ✅ Memory controller reads current `MEMORIES.md`
2. ✅ Agent understands current project state
3. ✅ Agent identifies what needs to change

### During work:
1. ✅ Agent applies its protocol (design/refactor/audit)
2. ✅ Agent documents changes/findings clearly
3. ✅ Agent reports results to user

### After work:
1. ✅ Memory controller logs to `MEMORIES.md`
2. ✅ Status updated (Completed/Pending/Blocked)
3. ✅ Context preserved for next agent

---

## 🎯 Tool Restrictions (Least Privilege)

| Agent | Tools Available | Rationale |
|-------|---|---|
| **Architect** | `search/codebase` | Analyzes & designs; developer implements |
| **Developer** | `edit`, `search/codebase` | Reads code, then refactors |
| **Security** | `search/codebase` | Audits & reports; developer fixes |
| **Memory** | `edit` | Updates MEMORIES.md state only |

---

## 💡 Best Practices

### ✅ Do:
- Consult memory before starting work
- Log all decisions and changes
- Use clear, specific prompts
- Separate concerns (architect designs, developer implements, security audits)
- Compress context in MEMORIES.md

### ❌ Don't:
- Skip memory check at start
- Ask one agent to do another's job
- Store conversational prose in MEMORIES.md
- Let memory grow unbounded (>10 entries = rewrite)
- Ignore security findings
