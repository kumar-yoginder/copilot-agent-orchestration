# Python Data Pipeline Template

A complete example of the multi-agent framework customized for a **Python ETL/data pipeline project**.

---

## 📋 Project Description

**Name:** DataLakePipeline  
**Domain:** Data Engineering  
**Goal:** Build a reliable, scalable ETL pipeline that ingests data from multiple sources (APIs, CSV files, databases) into a centralized data warehouse with quality checks and monitoring.

---

## 📂 Directory Structure

```
data-lake-pipeline/
├── .project-config.yaml          # Framework configuration
├── MEMORIES.md                   # Project state log
├── README.md                     # Project overview
├── src/
│   ├── __init__.py
│   ├── config.py                # Configuration management
│   ├── extraction/
│   │   ├── __init__.py
│   │   ├── api_source.py         # Extract from REST APIs
│   │   ├── csv_source.py         # Extract from CSV files
│   │   └── database_source.py    # Extract from databases
│   ├── transformation/
│   │   ├── __init__.py
│   │   ├── cleaner.py            # Data validation and cleaning
│   │   ├── aggregator.py         # Aggregation logic
│   │   └── enricher.py           # Data enrichment
│   ├── loading/
│   │   ├── __init__.py
│   │   └── warehouse.py          # Load to Snowflake/BigQuery
│   ├── quality/
│   │   ├── __init__.py
│   │   └── checks.py             # Data quality validations
│   └── pipeline.py               # Main orchestration
├── tests/
│   ├── __init__.py
│   ├── test_extraction.py
│   ├── test_transformation.py
│   ├── test_loading.py
│   └── test_quality.py
├── config/
│   ├── dev.yaml                  # Development config
│   ├── staging.yaml              # Staging config
│   └── prod.yaml                 # Production config
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Container image
├── docker-compose.yml            # Local development
└── .env.example                  # Environment variables template
```

---

## 🔧 Configuration Files

### `.project-config.yaml`

```yaml
project:
  name: "DataLakePipeline"
  domain: "Data Engineering"
  description: "ETL pipeline ingesting data from S3 to Snowflake with quality checks"
  version: "2.1.0"
  created: "2026-05-08"

architect:
  enabled: true
  focus_areas:
    - "Modular extraction, transformation, and loading stages"
    - "Scalable job scheduling with Airflow/Dagster"
    - "Data quality gates before warehouse load"
    - "Cost optimization for cloud storage and compute"
  design_principles:
    - "Each stage is independent and unit testable"
    - "Configuration-driven pipelines (no hardcoding)"
    - "Graceful error handling with retries"
    - "Comprehensive logging at every step"

developer:
  enabled: true
  languages:
    - "Python 3.11"
    - "SQL"
  code_style_guide: "PEP 8 + Black formatter"
  standards:
    - "Type hints for all functions (mypy strict mode)"
    - "Unit tests for transformations (>90% coverage)"
    - "Docstrings with examples for all public functions"
    - "No hardcoded values (use environment variables or config files)"
    - "Async patterns for I/O operations"
  quality_gates:
    - "No unused imports or variables"
    - "All methods documented with Args, Returns, Raises"
    - "Test coverage: >90% for transformation logic"
    - "Linting: pylint score >9.0"
    - "Type checking: mypy strict mode passes"

security:
  enabled: true
  compliance_frameworks:
    - "OWASP Top 10"
    - "Data Privacy (no PII in logs)"
    - "Credential rotation every 90 days"
  critical_assets:
    - "S3 credentials and bucket access"
    - "Snowflake connection strings"
    - "API keys for external data sources"
    - "Database passwords"
  threat_model: "Prevent data leaks, SQL injection in transformations, unauthorized access to sensitive data"
  mandatory_checks:
    - "SQL injection prevention (parameterized queries)"
    - "Secrets not hardcoded (use environment variables)"
    - "Credentials rotation policy enforced"
    - "Audit logs for all data access"
    - "No PII in debug logs or error messages"

memory:
  enabled: true
  memory_file: "MEMORIES.md"
  append_threshold: 10
  compression_enabled: true

architecture:
  version: "2.1.0"
  last_updated: "2026-05-08"
  components:
    - "Extraction Layer (S3, APIs, Databases)"
    - "Transformation Layer (Cleaning, Enrichment, Validation)"
    - "Loading Layer (Snowflake/BigQuery)"
    - "Quality Layer (Data validation, monitoring)"
  data_flow: "Extract → Validate → Transform → Enrich → Validate → Load"
```

---

## 📝 MEMORIES.md (Initial State)

```markdown
# DataLakePipeline — Project Memory Log

**Framework:** Multi-Agent Orchestration  
**Initialized:** 2026-05-08  
**Architecture Version:** 2.1.0

---

## Active Tasks & Initiatives
- Build modular extraction layer for S3, APIs, and databases
- Implement data quality checks before warehouse load
- Set up monitoring and alerting for pipeline failures
- Optimize Snowflake costs with incremental loads

---

## Architectural Decisions
- **Decision 1:** Modular ETL design (separate extraction, transformation, loading)
  - Date: 2026-05-08, Agent: Architect
  - Rationale: Enables independent testing, scaling, and maintenance
  - Impact: Each layer can be deployed/scaled independently

- **Decision 2:** Configuration-driven pipelines (YAML configs per environment)
  - Date: 2026-05-08, Agent: Architect
  - Rationale: No hardcoding; easy environment switching (dev/staging/prod)
  - Impact: Reduced secrets in code, consistent deployment

- **Decision 3:** Async Python with asyncio for I/O operations
  - Date: 2026-05-08, Agent: Architect
  - Rationale: Improve throughput for API calls and database queries
  - Impact: Better performance for network-bound operations

---

## Code Changes Log

[2026-05-08] [Developer]: Initial project structure and base classes
- **Change:** Created src/ folder with extraction, transformation, loading, quality modules
- **Status:** Completed
- **Files Modified:** src/__init__.py, src/config.py, src/pipeline.py
- **Context:** Base classes defined for SourceConnector, Transformer, QualityCheck; all typed

[2026-05-08] [Security]: Initial security audit
- **Change:** Reviewed config management and credential handling
- **Status:** Completed
- **Findings:** 
  - All credentials use environment variables ✅
  - SQL queries use parameterized statements ✅
  - Logging does not expose PII ✅

---

## Security Findings

### Completed
- [2026-05-08] Verified no hardcoded credentials in codebase — RESOLVED

### Pending
- Implement credential rotation policy for Snowflake service account
- Add audit logging for all data access events
- Review data retention policies for non-production environments

---

## Context Snapshots

### Snapshot 1: Initial Architecture (2026-05-08)
- **Current state:** Base project structure created; three main layers defined
- **Key blockers:** None identified yet
- **Next steps:** 
  1. Implement extraction sources (S3, API connectors)
  2. Build transformation pipeline (validators, cleaners)
  3. Set up unit tests (target >90% coverage)
  4. Configure CI/CD pipeline

---

## Open Questions
- Q1: Should we use Airflow or Dagster for orchestration? (Under evaluation)
- Q2: What's the SLA for data freshness? (Need to confirm with stakeholders)
- Q3: Do we need real-time streaming or batch is sufficient? (Currently batch-only)

---

## Maintenance Notes
- Last reviewed: 2026-05-08
- Next review: 2026-05-15
- Contacts: [DevOps Team], [Data Team]
```

---

## 🔐 Security Checklist (from security agent)

```markdown
## Data Pipeline Security Audit

### Access Control
- [ ] S3 bucket policies use least privilege (specific roles/users)
- [ ] Snowflake RBAC configured (separate roles for read/write)
- [ ] Service accounts have time-limited credentials
- [ ] API keys rotated every 90 days

### Data Integrity
- [ ] SQL queries use parameterized statements (no string concatenation)
- [ ] Data validation catches injection attempts
- [ ] Checksums verify data integrity in transit
- [ ] Audit logs track all data modifications

### Data Privacy
- [ ] PII detection in transformation layer
- [ ] Sensitive fields encrypted in Snowflake
- [ ] No sensitive data in logs or error messages
- [ ] Data retention policies enforced (delete old data)

### Dependency Security
- [ ] All Python packages scanned for CVEs
- [ ] requirements.txt pinned to specific versions
- [ ] No development dependencies in production

### Infrastructure
- [ ] Secrets not stored in Git (use .env files)
- [ ] Environment variables validated at startup
- [ ] Docker images scanned for vulnerabilities
- [ ] Network access restricted (VPC, security groups)
```

---

## 💻 Example Code Structure

### `src/extraction/api_source.py`
```python
"""Module for extracting data from REST APIs.

This module provides connectors for various API endpoints with
error handling, retries, and type safety.
"""

from typing import Any, Dict, List, Optional
import asyncio
import httpx
from abc import ABC, abstractmethod


class SourceConnector(ABC):
    """Abstract base class for data sources."""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize connector with configuration.
        
        Args:
            config: Configuration dictionary (from environment/YAML)
            
        Raises:
            ValueError: If required config keys are missing
        """
        self.config = config
        self._validate_config()
    
    @abstractmethod
    def extract(self) -> List[Dict[str, Any]]:
        """Extract data from source.
        
        Returns:
            List of dictionaries representing records
            
        Raises:
            ConnectionError: If source is unreachable
            ValueError: If data format is invalid
        """
        pass
    
    def _validate_config(self) -> None:
        """Validate required configuration keys."""
        required_keys = {"api_url", "timeout"}
        missing = required_keys - set(self.config.keys())
        if missing:
            raise ValueError(f"Missing config keys: {missing}")


class APIConnector(SourceConnector):
    """Connect to REST API endpoints."""
    
    async def extract_async(self) -> List[Dict[str, Any]]:
        """Asynchronously extract data from API.
        
        Returns:
            List of records from API response
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.config["api_url"],
                timeout=self.config.get("timeout", 30)
            )
            response.raise_for_status()
            return response.json()
    
    def extract(self) -> List[Dict[str, Any]]:
        """Extract data from API (sync wrapper)."""
        return asyncio.run(self.extract_async())
```

### `src/transformation/cleaner.py`
```python
"""Data cleaning and validation module."""

from typing import Any, Dict, List
import logging

logger = logging.getLogger(__name__)


class DataCleaner:
    """Validates and cleans data records."""
    
    def __init__(self, schema: Dict[str, type]):
        """Initialize cleaner with schema.
        
        Args:
            schema: Dictionary mapping field names to expected types
        """
        self.schema = schema
    
    def validate(self, record: Dict[str, Any]) -> bool:
        """Validate record against schema.
        
        Args:
            record: Data record to validate
            
        Returns:
            True if valid, False otherwise
        """
        for field, expected_type in self.schema.items():
            if field not in record:
                logger.warning(f"Missing field: {field}")
                return False
            if not isinstance(record[field], expected_type):
                logger.warning(f"Invalid type for {field}: expected {expected_type}")
                return False
        return True
    
    def clean_batch(self, records: List[Dict[str, Any]]) -> tuple:
        """Clean a batch of records.
        
        Args:
            records: List of data records
            
        Returns:
            Tuple of (valid_records, invalid_count)
        """
        valid = [r for r in records if self.validate(r)]
        invalid_count = len(records) - len(valid)
        logger.info(f"Cleaned batch: {len(valid)} valid, {invalid_count} invalid")
        return valid, invalid_count
```

---

## 🧪 Unit Test Example

### `tests/test_transformation.py`
```python
"""Tests for transformation layer."""

import pytest
from src.transformation.cleaner import DataCleaner


class TestDataCleaner:
    """Test data cleaning functionality."""
    
    @pytest.fixture
    def cleaner(self):
        """Create cleaner instance with test schema."""
        schema = {
            "id": int,
            "name": str,
            "email": str,
            "age": int
        }
        return DataCleaner(schema)
    
    def test_validate_valid_record(self, cleaner):
        """Test validation of valid record."""
        record = {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com",
            "age": 30
        }
        assert cleaner.validate(record) is True
    
    def test_validate_missing_field(self, cleaner):
        """Test validation with missing field."""
        record = {
            "id": 1,
            "name": "John Doe",
            "age": 30
        }
        assert cleaner.validate(record) is False
    
    def test_validate_invalid_type(self, cleaner):
        """Test validation with invalid type."""
        record = {
            "id": "not-an-int",  # Should be int
            "name": "John Doe",
            "email": "john@example.com",
            "age": 30
        }
        assert cleaner.validate(record) is False
    
    def test_clean_batch(self, cleaner):
        """Test batch cleaning."""
        records = [
            {"id": 1, "name": "John", "email": "john@example.com", "age": 30},
            {"id": 2, "name": "Jane", "email": "jane@example.com"},  # Missing age
            {"id": 3, "name": "Bob", "email": "bob@example.com", "age": 25}
        ]
        valid, invalid_count = cleaner.clean_batch(records)
        assert len(valid) == 2
        assert invalid_count == 1
```

---

## 📚 Next Steps for This Template

1. **Extend extraction layer** — Add CSV and database connectors
2. **Build transformation pipeline** — Implement aggregations and enrichment
3. **Implement loading layer** — Connect to Snowflake/BigQuery
4. **Add quality checks** — Data validation gates before loading
5. **Setup CI/CD** — GitHub Actions for testing and deployment
6. **Configure monitoring** — Logs, metrics, alerts
7. **Document runbooks** — Emergency procedures for pipeline failures

---

## 📖 Related Documentation

- See [CUSTOMIZATION.md](../../docs/CUSTOMIZATION.md) — Adapt this template for other domains
- See [AGENTS.md](../../docs/AGENTS.md) — Agent interaction patterns
- See [SETUP.md](../../docs/SETUP.md) — Full setup guide

---

**Template Version:** 1.0.0  
**Framework Version:** 1.0.0
