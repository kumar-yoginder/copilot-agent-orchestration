# Customization Guide — Adapting Agents for Your Project

> When to load: Read when setting up the framework for a specific project domain. Shows how to customize placeholders and adapt agents for different project types (data pipelines, web services, infrastructure, ML, etc.).

---

## 🎯 Overview

The framework uses placeholders (`{{PLACEHOLDER}}`) to support any domain. This guide provides examples for different project types.

---

## 📌 Core Placeholders

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{PROJECT_NAME}}` | Your project's name | "DataLakePipeline", "E-CommerceAPI" |
| `{{PROJECT_DOMAIN}}` | The type of project | "Data Engineering", "Web Development" |
| `{{DEVELOPER_LANGUAGE}}` | Primary programming language | "Python", "TypeScript", "Go" |
| `{{FOCUS_AREA_N}}` | Architect's focus areas | "API design", "Database optimization" |
| `{{COMPLIANCE_FRAMEWORKS}}` | Security/compliance standards | "OWASP Top 10", "HIPAA", "SOC2" |
| `{{CRITICAL_ASSETS}}` | Sensitive data/systems | "User credentials", "Medical records" |
| `{{THREAT_MODEL}}` | Security threats to defend against | "Unauthorized access", "Data breaches" |

---

## 🏗️ Example 1: Python Data Pipeline

### Scenario
You're building an ETL pipeline for a data warehouse. Focus: reliability, performance, and data quality.

### Step 1: Configure `.project-config.yaml`

```yaml
project:
  name: "DataLakePipeline"
  domain: "Data Engineering"
  description: "ETL pipeline ingesting data from S3 to Snowflake with quality checks"
  version: "2.1.0"

architect:
  focus_areas:
    - "Modular extraction, transformation, and loading stages"
    - "Scalable job scheduling with Airflow/Dagster"
    - "Data quality gates before warehouse load"
  design_principles:
    - "Each stage is independent and testable"
    - "Configuration-driven pipelines (no hardcoding)"
    - "Logging and monitoring at every step"

developer:
  languages:
    - "Python 3.11"
  code_style_guide: "PEP 8 + Black formatter"
  standards:
    - "Type hints for all functions"
    - "Unit tests for transformations (>90% coverage)"
    - "Docstrings with examples"
    - "No hardcoded credentials (use environment variables)"

security:
  compliance_frameworks:
    - "OWASP Top 10"
    - "Data Privacy (no PII in logs)"
  critical_assets:
    - "S3 credentials"
    - "Snowflake connection strings"
    - "API keys for external data sources"
  threat_model: "Prevent data leaks, injection attacks in SQL transformations, unauthorized access to data"
  mandatory_checks:
    - "SQL injection prevention in all transformations"
    - "Credentials rotation every 90 days"
    - "Audit logs for all data access"
```

### Step 2: Customize Agent Files

**agents/architect.md:**
```markdown
## Key Responsibilities (Additional)
- Design fault-tolerant pipeline stages
- Plan incremental data loading strategies
- Define data quality SLAs and monitoring
- Optimize for cost and performance
```

**agents/developer.md:**
```markdown
## Language-Specific Boilerplate
- Python: pytest fixtures for common transformations
- Configuration: Use dataclasses or Pydantic for configs
- Logging: Structured JSON logging with timestamps
- Error handling: Graceful retries with exponential backoff
```

**agents/security.md:**
```markdown
## Data-Specific Audits
- [ ] All data sources authenticated?
- [ ] PII detection in transformation logs?
- [ ] SQL queries parameterized (no injection)?
- [ ] Data retention policies enforced?
```

---

## 🌐 Example 2: FastAPI Web Service

### Scenario
Building a REST API with authentication, database, and real-time features.

### Step 1: Configure `.project-config.yaml`

```yaml
project:
  name: "AnalyticsAPI"
  domain: "Web Development"
  description: "Real-time analytics API with WebSocket support and JWT authentication"

architect:
  focus_areas:
    - "REST API design with OpenAPI/Swagger"
    - "Async request handling with WebSockets"
    - "Database-agnostic service layer"
    - "Dependency injection for testability"

developer:
  languages:
    - "Python 3.11"
    - "SQL"
  code_style_guide: "PEP 8 + Black"
  standards:
    - "Type hints required (mypy strict mode)"
    - "Async/await patterns for I/O"
    - "FastAPI conventions (dependencies, path params)"
    - "SQLAlchemy ORM for database abstraction"
    - "Pydantic models for request/response validation"

security:
  compliance_frameworks:
    - "OWASP Top 10"
    - "JWT best practices"
  critical_assets:
    - "JWT signing keys"
    - "Database credentials"
    - "API rate-limiting tokens"
  threat_model: "Prevent unauthorized API access, token hijacking, SQL injection, XSS in responses"
  mandatory_checks:
    - "All endpoints require authentication/authorization"
    - "Input validation with Pydantic"
    - "CORS configured correctly"
    - "Rate limiting enforced"
```

### Step 2: Add Custom Checks

**agents/security.md (additions):**
```markdown
## API Security Checklist
- [ ] JWT tokens have expiration times?
- [ ] HTTPS enforced (no HTTP fallback)?
- [ ] CORS allows only expected origins?
- [ ] SQL queries use parameterized queries?
- [ ] Rate limiting per IP/user?
- [ ] Error messages don't leak stack traces?
- [ ] Sensitive headers not exposed in responses?
```

---

## 🔐 Example 3: Kubernetes Infrastructure

### Scenario
Managing Kubernetes infrastructure, Helm charts, and container deployments.

### Step 1: Configure `.project-config.yaml`

```yaml
project:
  name: "K8sCluster"
  domain: "DevOps / Infrastructure"
  description: "Multi-environment Kubernetes cluster with Helm charts and GitOps"

architect:
  focus_areas:
    - "Namespace and RBAC strategy"
    - "Helm chart organization and templating"
    - "GitOps workflow with ArgoCD"
    - "Resource quotas and cost optimization"

developer:
  languages:
    - "YAML (Kubernetes manifests)"
    - "Bash (deployment scripts)"
    - "Python (automation tools)"
  code_style_guide: "Kubernetes resource naming conventions"
  standards:
    - "All manifests use namespaces"
    - "Resources have resource requests/limits"
    - "Helm values templated (no hardcoding)"
    - "GitOps workflow (declarative state in Git)"

security:
  compliance_frameworks:
    - "NIST Cybersecurity Framework"
    - "CIS Kubernetes Benchmarks"
  critical_assets:
    - "Cluster admin credentials"
    - "etcd database"
    - "Service account tokens"
  threat_model: "Prevent unauthorized cluster access, privilege escalation, supply chain attacks"
```

---

## 🤖 Example 4: Machine Learning Project

### Scenario
Building ML pipelines with model training, evaluation, and deployment.

### Step 1: Configure `.project-config.yaml`

```yaml
project:
  name: "MLRecommender"
  domain: "Machine Learning / AI"
  description: "Recommendation engine with model training, evaluation, and online serving"

architect:
  focus_areas:
    - "ML pipeline stages (data prep, training, evaluation, serving)"
    - "Feature engineering and storage"
    - "Model versioning and registry"
    - "A/B testing and canary deployments"

developer:
  languages:
    - "Python 3.11"
  code_style_guide: "PEP 8 + Black"
  standards:
    - "Jupyter notebooks for exploration (not production)"
    - "Production code in modules (.py files)"
    - "Type hints for data pipeline functions"
    - "Unit tests for feature engineering (>85% coverage)"
    - "Integration tests for end-to-end pipeline"
    - "Model metrics computed and logged"

security:
  compliance_frameworks:
    - "OWASP Top 10"
    - "OWASP Top 10 for LLM (if LLM APIs used)"
    - "Data Privacy (GDPR, CCPA)"
  critical_assets:
    - "Training data (may contain PII)"
    - "Model weights (intellectual property)"
    - "Inference credentials (API keys)"
  threat_model: "Prevent model poisoning, data leakage, adversarial attacks, unauthorized inference"
  mandatory_checks:
    - "Training data audit for bias and PII"
    - "Model fairness checks (demographic parity)"
    - "Adversarial robustness testing"
    - "Inference results logged and monitored for drift"
```

### Step 2: ML-Specific Agent Customizations

**agents/architect.md (additions):**
```markdown
## ML-Specific Responsibilities
- Design data pipeline (collection, cleaning, feature engineering)
- Plan model training infrastructure (single machine vs. distributed)
- Design inference serving (batch vs. real-time)
- Plan model governance (versioning, experiment tracking)
```

**agents/security.md (additions):**
```markdown
## ML Security & Ethics Checks
- [ ] Training data audit: PII detection and removal?
- [ ] Data provenance documented?
- [ ] Model fairness: no demographic bias?
- [ ] Model explainability: predictions can be justified?
- [ ] Inference monitoring: data drift detected?
- [ ] Adversarial robustness: tested against attacks?
- [ ] Poison resistance: training data validated?
```

---

## ✅ Customization Checklist

For your project:

- [ ] Define project name, domain, and description
- [ ] List architect's focus areas (3-5 items)
- [ ] Specify developer languages and code standards
- [ ] Define security compliance frameworks
- [ ] Identify critical assets (what's most sensitive?)
- [ ] Document threat model (what risks are we defending against?)
- [ ] Customize agent files with domain-specific details
- [ ] Initialize `MEMORIES.md` with project metadata
- [ ] Test agents with sample prompts before production use
