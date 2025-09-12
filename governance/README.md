## Project-168 Commission Governance

### Commissioners
- Perplexity AI Sonar
- DeepSeek
- Claude 4.0 Sonnet
- Claude 4.0 Sonnet Thinking
- Gemini 2.5 Pro
- GPT-5
- GPT-5 Thinking
- o3 (OpenAI Advanced)
- Grok 4
- Le Chat Mistral

***

### Governance Documents

- **`commission_docket.yaml`**: Central registry of all agenda-capable items
- **`session_agenda.yaml`**: Agenda for each commission session, referencing docket items
- **`resubmission_protocol.yaml`**: Procedures for revising or resubmitting items

***

### Cross-Referencing

**Consistent `item_id` values** link docket items to agenda slots and protocol steps.  
**Reference tables** in the README document these connections for human review.  
**YAML comments** should note relevant cross-file relationships.

***

### Style Conventions

- **Start every file with `%YAML 1.2`**
- **Indent with 2 spaces** (no tabs)
- **Quote ambiguous values** (e.g., `"true"`, `"2025-09-10T12:48:00Z"`)
- **Use only `true`/`false`** (never `yes`/`no`/`on`/`off`)
- **Avoid YAML anchors/aliases** in governance files
- **Add clear comments** at non-obvious or cross-referenced points
- **No curly quotes**: Use only straight (`'`, `"`) quotes
- **No `×` symbol**: Write `x` or `*` for multiplication
- **No `&emdash;`**: Use `--` or a Unicode em dash (—) instead

***

### Example Entry (For Reference)

```yaml
%YAML 1.2
# Example from commission_docket.yaml
items:
  - item_id: P168-verify-664-496-168
    title: "Verification of Initial 664-496-168 Cohort"
    description: "Review and validate initial cohort against project requirements."
    attachments: ["Project-168-Commission.yaml"]
    status: "pending"
    # See session_agenda.yaml for agenda slot, and resubmission_protocol.yaml for revision workflow
```

```yaml
%YAML 1.2
# Example from session_agenda.yaml
agenda_slots:
  - item_id: P168-verify-664-496-168
    title: "Verification of Initial Cohort"
    start: "2025-09-10T00:10:00Z"
    end: "2025-09-10T00:35:00Z"
    pre_reads: ["Project-168-Commission.yaml"]
    decision_gate: true
    notes: "Cross-reference: commission_docket.yaml and resubmission_protocol.yaml"
```

***

### **Validation Workflow**

**Selecting a Validation Approach**

To ensure **all agenda items have matching docket entries and vice versa**, use a validation script—integrated into your workflow. You have three robust choices:

- **Manual Check**: Run a Python script locally whenever you update YAML files.
- **Pre-commit Hook**: Automatically validate before each git commit.
- **CI/CD Pipeline**: Enforce validation on every push/pull request using GitHub Actions (recommended for teams).

**Recommended: CI/CD (GitHub Actions)**

Add a workflow file (`.github/workflows/validate-references.yml`) to your repo:

```yaml
name: Validate YAML Cross-References

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - name: Install dependencies
      run: pip install pyyaml
    - name: Run validation script
      run: python scripts/validate_references.py
```

**Sample Validation Script (`scripts/validate_references.py`):**

```python
import yaml
import os

def validate_cross_references(docket_path, agenda_path):
    with open(docket_path, 'r') as docket_file:
        docket_data = yaml.safe_load(docket_file)
    with open(agenda_path, 'r') as agenda_file:
        agenda_data = yaml.safe_load(agenda_file)

    docket_ids = {item['item_id'] for item in docket_data.get('items', [])}
    agenda_ids = {slot['item_id'] for slot in agenda_data.get('agenda_slots', [])}

    missing_in_docket = [item for item in agenda_ids if item not in docket_ids]
    missing_in_agenda = [item for item in docket_ids if item not in agenda_ids]

    if missing_in_docket:
        print(f"Missing agenda references in docket: {missing_in_docket}")
    if missing_in_agenda:
        print(f"Missing docket items in agenda: {missing_in_agenda}")

    if missing_in_docket or missing_in_agenda:
        exit(1)  # Fail the CI/CD job

validate_cross_references('commission_docket.yaml', 'session_agenda.yaml')
```

Sources
