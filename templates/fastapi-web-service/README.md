# FastAPI Web Service Template

A complete example of the multi-agent framework customized for a **FastAPI REST API project**.

---

## 📋 Project Description

**Name:** AnalyticsAPI  
**Domain:** Web Development  
**Goal:** Build a secure, scalable REST API for real-time analytics with JWT authentication, WebSocket support, and PostgreSQL persistence.

---

## 📂 Directory Structure

```
analytics-api/
├── .project-config.yaml          # Framework configuration
├── MEMORIES.md                   # Project state log
├── README.md                     # Project overview
├── src/
│   ├── __init__.py
│   ├── main.py                   # FastAPI app initialization
│   ├── settings.py               # Pydantic settings/configuration
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── analytics.py  # Analytics endpoints
│   │   │   │   ├── users.py      # User management
│   │   │   │   └── auth.py       # Authentication
│   │   │   └── schemas.py        # Request/response models
│   │   └── v2/                   # API v2 (future)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth.py               # JWT token management
│   │   ├── analytics.py          # Business logic
│   │   └── database.py           # Database operations
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py               # SQLAlchemy User model
│   │   └── analytics.py          # SQLAlchemy Analytics model
│   ├── dependencies.py           # FastAPI dependency injection
│   └── middleware.py             # Logging, error handling
├── tests/
│   ├── __init__.py
│   ├── conftest.py               # Pytest fixtures
│   ├── test_auth.py
│   ├── test_analytics_endpoints.py
│   └── test_integration.py
├── migrations/                   # Alembic database migrations
│   └── env.py
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Container image
├── docker-compose.yml            # Local development with PostgreSQL
├── .env.example                  # Environment variables template
└── pyproject.toml                # Python project config
```

---

## 🔧 Configuration Files

### `.project-config.yaml`

```yaml
project:
  name: "AnalyticsAPI"
  domain: "Web Development"
  description: "Secure REST API for real-time analytics with JWT auth and WebSockets"
  version: "1.2.0"
  created: "2026-05-08"

architect:
  enabled: true
  focus_areas:
    - "RESTful API design with OpenAPI/Swagger documentation"
    - "Async request handling with FastAPI and async database operations"
    - "JWT authentication with refresh token rotation"
    - "Database-agnostic service layer (SQLAlchemy ORM)"
    - "Dependency injection for testability and loose coupling"
  design_principles:
    - "Single Responsibility Principle (one endpoint ≈ one handler)"
    - "Layered architecture (routes → services → models)"
    - "Dependency injection throughout"
    - "Type-safe using Pydantic and SQLAlchemy"

developer:
  enabled: true
  languages:
    - "Python 3.11"
    - "SQL (PostgreSQL)"
  code_style_guide: "PEP 8 + Black (line length 88)"
  standards:
    - "Type hints for all functions (mypy --strict)"
    - "FastAPI conventions (path params, query params, dependencies)"
    - "Pydantic models for request/response validation"
    - "SQLAlchemy ORM for database abstraction"
    - "Async/await for all I/O operations"
    - "Unit tests with >85% coverage"
    - "Docstrings with examples"
  quality_gates:
    - "All endpoints documented with OpenAPI specs"
    - "No global state or side effects in services"
    - "Proper error handling with meaningful HTTP status codes"
    - "Logging at appropriate levels (info, warning, error)"
    - "No N+1 queries in database operations"

security:
  enabled: true
  compliance_frameworks:
    - "OWASP Top 10 (especially A01, A02, A07)"
    - "JWT best practices (RS256 signing)"
    - "CORS properly configured"
  critical_assets:
    - "JWT signing keys (private keys secure, rotated)"
    - "Database credentials and connection strings"
    - "API rate-limiting tokens"
    - "User authentication tokens and refresh tokens"
  threat_model: "Prevent unauthorized API access, token hijacking, SQL injection, XSS in JSON responses, rate-limit bypass attacks"
  mandatory_checks:
    - "All endpoints require authentication (except login/register)"
    - "Pydantic models validate all inputs"
    - "SQL queries use ORM (no raw SQL string concatenation)"
    - "CORS allows only expected origins"
    - "Rate limiting enforced per IP and per user"
    - "Error responses don't leak stack traces or internal details"
    - "Sensitive headers (Authorization) only over HTTPS"
    - "Password hashing uses bcrypt with >12 rounds"

memory:
  enabled: true
  memory_file: "MEMORIES.md"
  append_threshold: 10
  compression_enabled: true

architecture:
  version: "1.2.0"
  last_updated: "2026-05-08"
  components:
    - "FastAPI Application Server (async HTTP)"
    - "PostgreSQL Database (persistence)"
    - "JWT Authentication (stateless tokens)"
    - "Pydantic Models (validation + serialization)"
    - "SQLAlchemy ORM (database abstraction)"
    - "Middleware (logging, error handling, CORS)"
  data_flow: |
    HTTP Request → FastAPI Router → Dependency Injection →
    Handler (business logic) → Service Layer → Database →
    Response (Pydantic model) → JSON HTTP Response
```

---

## 📝 MEMORIES.md (Initial State)

```markdown
# AnalyticsAPI — Project Memory Log

**Framework:** Multi-Agent Orchestration  
**Initialized:** 2026-05-08  
**Architecture Version:** 1.2.0

---

## Active Tasks & Initiatives
- Design RESTful API endpoints for analytics and user management
- Implement JWT authentication with secure token refresh mechanism
- Setup PostgreSQL database with SQLAlchemy ORM
- Comprehensive API documentation (OpenAPI/Swagger)
- Unit and integration testing (>85% coverage target)
- Configure CI/CD pipeline with automated tests

---

## Architectural Decisions

### Decision 1: Layered Architecture (Routes → Services → Models)
- **Date:** 2026-05-08 | **Agent:** Architect
- **Details:** Three-layer design: API layer (FastAPI), business logic (services), data (SQLAlchemy models)
- **Rationale:** Clear separation of concerns; testable; loosely coupled
- **Impact:** Easy to swap implementations (e.g., database); simple unit testing

### Decision 2: Type Safety with Pydantic + SQLAlchemy
- **Date:** 2026-05-08 | **Agent:** Architect
- **Details:** Use Pydantic for request/response validation; SQLAlchemy for database models
- **Rationale:** Runtime type validation; automatic API documentation; migration-safe database changes
- **Impact:** Fewer runtime errors; auto-generated OpenAPI spec; easier API versioning

### Decision 3: JWT Stateless Authentication
- **Date:** 2026-05-08 | **Agent:** Architect
- **Details:** Short-lived access tokens (15 min) + longer-lived refresh tokens (7 days)
- **Rationale:** Scalable across multiple servers; no session storage needed
- **Impact:** No sticky sessions required; easier horizontal scaling

### Decision 4: Async-First Design
- **Date:** 2026-05-08 | **Agent:** Architect
- **Details:** All I/O operations use async/await (FastAPI, SQLAlchemy async driver)
- **Rationale:** Better concurrency for high-traffic API
- **Impact:** Higher throughput; better resource utilization

---

## Code Changes Log

[2026-05-08] [Developer]: Initial FastAPI project structure
- **Change:** Created src/ folder with modular layout (api, services, models)
- **Status:** ✅ Completed
- **Files Modified:** src/main.py, src/settings.py, src/api/v1/endpoints/*.py
- **Context:** Base endpoints created with Pydantic validation; SQLAlchemy models initialized

[2026-05-08] [Security]: Security baseline audit
- **Change:** Reviewed authentication setup and input validation
- **Status:** ✅ Completed
- **Findings:**
  - JWT tokens require HTTPS ✅
  - Pydantic validation on all inputs ✅
  - Password hashing uses bcrypt ✅
  - Rate limiting configured ✅

---

## Security Findings

### ✅ Resolved
- All endpoints require authentication (except /auth/login)
- Pydantic models validate all request bodies
- Error responses sanitized (no stack traces)

### ⏳ Pending
- Implement refresh token rotation (new token on each refresh)
- Add API key management for service-to-service auth
- Enable request signing (HMAC-SHA256) for sensitive operations
- Setup request/response logging without exposing sensitive data

---

## Open Questions
- Q1: Should we support OAuth2/OpenID Connect? (Currently JWT-only)
- Q2: Do we need WebSocket support for real-time analytics? (Planned for v2)
- Q3: What's the rate limit per user? (Currently 100 req/min)

---

## Maintenance Notes
- Last reviewed: 2026-05-08
- Next review: 2026-05-15
```

---

## 🔐 Security Checklist (from security agent)

```markdown
## API Security Audit

### Authentication & Authorization
- [ ] JWT tokens have short expiration (15 min)?
- [ ] Refresh tokens have longer expiration (7 days)?
- [ ] Refresh token rotation implemented (new token on each refresh)?
- [ ] All sensitive endpoints protected with @requires_auth?
- [ ] Admin endpoints protected with @requires_admin role?

### Input Validation
- [ ] All request bodies validated with Pydantic?
- [ ] Path parameters validated (e.g., UUID, positive integers)?
- [ ] Query parameters sanitized and typed?
- [ ] File uploads have size limits?

### Output Security
- [ ] JSON responses don't leak sensitive data?
- [ ] Error messages are generic (don't reveal internals)?
- [ ] Stack traces never sent to clients?
- [ ] Sensitive fields excluded from API responses?

### Database Security
- [ ] All SQL queries use ORM (no raw SQL concatenation)?
- [ ] Database credentials in environment variables only?
- [ ] Connection pooling configured?
- [ ] Prepared statements for any raw SQL?

### Network Security
- [ ] HTTPS enforced (HTTP redirects to HTTPS)?
- [ ] CORS allows only expected origins?
- [ ] Security headers set (HSTS, X-Content-Type-Options, etc.)?
- [ ] Rate limiting prevents abuse?
- [ ] CSRF tokens used for state-changing operations?

### Dependency Security
- [ ] All packages in requirements.txt are pinned to versions?
- [ ] No development dependencies in production?
- [ ] Packages scanned for known CVEs?
```

---

## 💻 Example Code Structure

### `src/main.py`
```python
"""FastAPI application initialization.

This module creates and configures the FastAPI application
with all routes, middleware, and error handlers.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from src.settings import Settings
from src.api.v1 import endpoints
from src.middleware import logging_middleware

settings = Settings()
app = FastAPI(
    title="Analytics API",
    description="Real-time analytics with JWT authentication",
    version="1.2.0"
)

# Security middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.TRUSTED_HOSTS
)

# Custom middleware
app.middleware("http")(logging_middleware)

# Include routers
app.include_router(endpoints.auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(endpoints.analytics.router, prefix="/api/v1/analytics", tags=["analytics"])
app.include_router(endpoints.users.router, prefix="/api/v1/users", tags=["users"])

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### `src/api/v1/endpoints/auth.py`
```python
"""Authentication endpoints.

Handles user login, registration, and token refresh.
All passwords are hashed with bcrypt (12+ rounds).
Tokens use RS256 (RSA) signing for security.
"""

from typing import Annotated
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
import jwt
from passlib.context import CryptContext

from src.services.auth import AuthService
from src.settings import Settings

router = APIRouter()
settings = Settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
auth_service = AuthService()


class LoginRequest(BaseModel):
    """User login credentials."""
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """JWT token response."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest) -> TokenResponse:
    """Authenticate user and return JWT tokens.
    
    Args:
        request: Login credentials (email + password)
        
    Returns:
        TokenResponse with access and refresh tokens
        
    Raises:
        HTTPException: If credentials are invalid
    """
    user = await auth_service.authenticate_user(request.email, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = auth_service.create_access_token(user.id)
    refresh_token = auth_service.create_refresh_token(user.id)
    
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token
    )


@router.post("/refresh")
async def refresh_token(refresh_token: str) -> TokenResponse:
    """Refresh access token using refresh token.
    
    Args:
        refresh_token: Valid refresh token
        
    Returns:
        New TokenResponse with fresh tokens
        
    Raises:
        HTTPException: If refresh token is invalid/expired
    """
    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
        user_id = payload.get("sub")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    access_token = auth_service.create_access_token(user_id)
    new_refresh_token = auth_service.create_refresh_token(user_id)
    
    return TokenResponse(
        access_token=access_token,
        refresh_token=new_refresh_token
    )
```

---

## 🧪 Unit Test Example

### `tests/test_auth.py`
```python
"""Tests for authentication service."""

import pytest
from src.services.auth import AuthService
from src.models.user import User


class TestAuthService:
    """Test JWT token generation and validation."""
    
    @pytest.fixture
    async def auth_service(self):
        """Create auth service instance."""
        return AuthService()
    
    @pytest.mark.asyncio
    async def test_create_access_token(self, auth_service):
        """Test access token generation."""
        token = auth_service.create_access_token(user_id="user123")
        assert token is not None
        assert isinstance(token, str)
    
    @pytest.mark.asyncio
    async def test_token_expiration(self, auth_service):
        """Test that tokens have correct expiration."""
        token = auth_service.create_access_token(user_id="user123")
        # Verify token contains expiration claim
        decoded = auth_service.decode_token(token)
        assert "exp" in decoded
    
    @pytest.mark.asyncio
    async def test_invalid_token_raises_error(self, auth_service):
        """Test that invalid tokens raise error."""
        with pytest.raises(Exception):
            auth_service.decode_token("invalid.token.here")
```

---

## 🚀 Getting Started

1. **Copy template** to your project directory
2. **Customize `.project-config.yaml`** with your project details
3. **Install dependencies:** `pip install -r requirements.txt`
4. **Setup database:** `docker-compose up` (runs PostgreSQL locally)
5. **Run migrations:** `alembic upgrade head`
6. **Start server:** `uvicorn src.main:app --reload`
7. **View API docs:** Visit `http://localhost:8000/docs`

---

## 📖 Related Documentation

- See [CUSTOMIZATION.md](../../docs/CUSTOMIZATION.md) — Adapt for other web frameworks
- See [AGENTS.md](../../docs/AGENTS.md) — Agent interaction patterns
- See [SETUP.md](../../docs/SETUP.md) — Full setup guide

---

**Template Version:** 1.0.0  
**Framework Version:** 1.0.0
