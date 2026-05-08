# Naming Conventions — Framework & Project Standards

> When to load: Read before naming any new files, directories, or code elements. Architect enforces these standards—always check here before creating something new.

---

## 📋 Overview

Consistent naming conventions improve:
- ✅ Code readability and maintainability
- ✅ Team collaboration and communication
- ✅ Automated tool support (linting, formatting)
- ✅ Project organization and navigation

**All files, directories, code, and documentation must follow these conventions.**

---

## 🏗️ Directory & File Naming

### Root Level Files

| Type | Pattern | Example | Purpose |
|------|---------|---------|---------|
| **Main Project Docs** | `UPPERCASE_WITH_UNDERSCORES.md` | `README.md` | Entry point documentation |
| **Main Config** | `lowercase.yaml` or `lowercase.json` | `.project-config.yaml` | Project configuration |
| **Root Hidden Files** | `.filename` | `.gitignore`, `.env.example` | System/environment config |

### Documentation Directory (`references/`)

| Type | Pattern | Example |
|------|---------|---------|
| **Guides** | `UPPERCASE_WITH_UNDERSCORES.md` | `SETUP.md`, `CUSTOMIZATION.md` |
| **Reference** | `UPPERCASE_WITH_UNDERSCORES.md` | `AGENTS.md`, `INDEX.md` |
| **Project State** | `UPPERCASE.md` | `MEMORIES.md` |
| **Templates** | `UPPERCASE_TEMPLATE.md` | `MEMORY_TEMPLATE.md` |
| **Conventions** | `UPPERCASE_CONVENTIONS.md` | `NAMING_CONVENTIONS.md` |

### Agent Directory (`agents/`)

| Type | Pattern | Example |
|------|---------|---------|
| **Agent Files** | `{{agent_name}}.md` | `architect.md`, `developer.md` |

### Source Code Directory (`src/`)

| Type | Pattern | Example |
|------|---------|---------|
| **Python Files** | `snake_case.py` | `data_processor.py`, `auth_service.py` |
| **TypeScript/JavaScript** | `camelCase.ts`, `camelCase.js` | `authService.ts`, `userController.js` |
| **Directories** | `snake_case/` | `src/services/`, `src/models/` |
| **Java Files** | `PascalCase.java` | `AuthService.java`, `UserModel.java` |
| **Go Files** | `snake_case.go` | `auth_service.go`, `user_model.go` |

### Template Directory (`templates/`)

| Type | Pattern | Example |
|------|---------|---------|
| **Template Folders** | `kebab-case/` | `python-data-pipeline/`, `fastapi-web-service/` |
| **Template Config** | `.project-config.yaml` | `.project-config.yaml` |
| **Template Docs** | `README.md` | `README.md` (project-specific) |

---

## 📝 Code Naming Conventions

### Python

```python
# Modules (snake_case)
user_service.py
auth_manager.py

# Classes (PascalCase)
class UserManager:
    pass

class AuthenticationService:
    pass

# Functions/Methods (snake_case)
def get_user_by_id(user_id: int) -> User:
    pass

def authenticate_user(email: str, password: str) -> Token:
    pass

# Constants (UPPERCASE_WITH_UNDERSCORES)
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
API_BASE_URL = "https://api.example.com"

# Private/Internal (leading underscore)
def _validate_input(data: dict) -> bool:
    pass

_internal_cache = {}
```

### TypeScript/JavaScript

```typescript
// Modules (camelCase)
userService.ts
authManager.ts

// Classes (PascalCase)
class UserManager {}
class AuthenticationService {}

// Functions (camelCase)
function getUserById(userId: number): User {}
function authenticateUser(email: string, password: string): Token {}

// Constants (UPPERCASE_WITH_UNDERSCORES)
const MAX_RETRY_ATTEMPTS = 3;
const DEFAULT_TIMEOUT_SECONDS = 30;
const API_BASE_URL = "https://api.example.com";

// Types/Interfaces (PascalCase)
interface UserData {}
type UserStatus = "active" | "inactive";
```

### Java

```java
// Packages (lowercase.separated.by.dots)
package com.example.auth;
package com.example.users.services;

// Classes (PascalCase)
public class UserManager {}
public class AuthenticationService {}

// Methods (camelCase)
public User getUserById(int userId) {}
public Token authenticateUser(String email, String password) {}

// Constants (UPPERCASE_WITH_UNDERSCORES)
public static final int MAX_RETRY_ATTEMPTS = 3;
public static final String API_BASE_URL = "https://api.example.com";

// Variables (camelCase)
private String userName;
private int userId;
```

---

## 📚 Documentation Naming

### Markdown Files

```
# Root Documentation
README.md                    # Main project overview (required at root)

# references/ Directory
references/SETUP.md               # Setup instructions
references/CUSTOMIZATION.md       # Customization guide
references/AGENTS.md              # Agent specifications
references/NAMING_CONVENTIONS.md  # This file
references/DIRECTORY_STRUCTURE.md # Directory organization
references/MEMORIES.md            # Project memory (auto-maintained)
references/MEMORY_TEMPLATE.md     # Memory file template
references/INDEX.md               # Complete file reference
references/AGENT_TOOLS_UPDATE.md  # Update history
```

### Section Headers in Documentation

```markdown
# Main Title (H1 - one per file)
## Section (H2 - use ### for subsections)
### Subsection (H3)
#### Sub-subsection (H4 - rarely needed)
```

---

## ⚠️ Anti-Patterns (Avoid)

❌ **Bad naming:**
```
util.py              # Too vague
helpers.js           # Too generic
stuff.py             # Meaningless
service.ts           # Which service?
module1.py           # Non-descriptive
MY_FUNCTION.py       # Functions aren't UPPERCASE
data/data/data.json  # Redundant nesting
```

✅ **Good naming:**
```
string_utils.py           # Specific
validation_helpers.ts     # Clear purpose
payment_processor.py      # Descriptive
user_service.ts           # Which service (user)
authentication_module.py  # Clear purpose
config.json               # Correct style
```

---

## 🎯 Summary Table

| Context | Pattern | Example | Language |
|---------|---------|---------|----------|
| Python Modules | `snake_case` | `user_service.py` | All |
| Python Classes | `PascalCase` | `UserManager` | Python |
| Python Functions | `snake_case` | `get_user_by_id()` | Python |
| TypeScript Modules | `camelCase` | `userService.ts` | TypeScript |
| TypeScript Classes | `PascalCase` | `UserManager` | TypeScript |
| Java Packages | `lowercase.dot.separated` | `com.example.users` | Java |
| Java Classes | `PascalCase` | `UserManager` | Java |
| Directories | `snake_case` or `kebab-case` | `src/services/` | All |
| Docs (General) | `UPPERCASE_UNDERSCORE` | `SETUP.md` | Markdown |
| Hidden Config | `.filename` | `.env.example` | All |
| Templates | `kebab-case/` | `python-data-pipeline/` | All |

---

**Framework Version:** 1.0.0  
**Last Updated:** 8 May 2026  
**Authority:** @architect agent
