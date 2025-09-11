# AI Project-198 Commission:
Commissioners:
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


# Governance YAML: Cross-Referencing, Style, and Next Steps

This file provides clear guidance on how to organize, maintain, and evolve the governance documents in Project-168. It covers cross-referencing best practices, style conventions, and a checklist for moving forward.

## Governance Documents

  - committee_docket.yaml

  - 
  - session_agenda.yaml
  - resubmission_protocol.yaml

---

## Cross-Referencing

**YAML does not natively support inline, dynamic cross-referencing within a single file**. Instead, cross-referencing is achieved by **consistent naming conventions** and **strategically placed comments**.

### How to Reference

- **Use the same `item_id`** in `committee_docket.yaml` and `session_agenda.yaml` files to link agenda items to their docket entries.
- **Reference directive filenames** (e.g., `Project-168-Committee.yaml`) as attachments in the docket and as pre-reads in the agenda.
- **Document cross-references in the `README.md` and in comments** for human clarity.
- **Maintain a table in the `README.md`** (see below for an example) tracking which docket items map to which agenda slots and protocol updates.

#### Example Table

| Docket `item_id`         | Agenda Slot(s)             | Protocol Reference(s)        | Pre-Read(s)                  |
|--------------------------|---------------------------|-----------------------------|------------------------------|
| P168-verify-664-496-168  | 00:10–00:35 (session-2025-09-12) | -                           | Project-168-Committee.yaml   |
| protocol-refresh         | 00:35–00:55 (session-2025-09-12) | resubmission_protocol.yaml  | Project-168-Committee.yaml   |

**Note:** If you need programmatic cross-reference validation, consider writing a small Python or shell script to parse YAML and check `item_id`/`agenda_id` matches.

---

## Style Conventions

Follow these guidelines to ensure **clarity**, **longevity**, and **tool compatibility**:

- **Use `%YAML 1.2` directive** at the top of every file.
- **Consistent indentation** (2 spaces per level, no tabs).
- **Quote ambiguous scalars** (e.g., `"yes"`, `"true"`, `"2025-09-10T12:48:00Z"`) to prevent YAML casting issues.
- **Explicit booleans**: Use `true/false` (never `yes/no/on/off`).
- **Descriptive, consistent key names** (e.g., `item_id`, `pre_reads`, `decision_gate`).
- **Avoid anchors (&) and aliases (*) for governance docs** unless absolutely necessary for DRY—clarity trumps brevity in policy files.
- **Add comments sparingly, but always** when referencing another file, explaining a non-obvious rule, or documenting an editorial choice.

