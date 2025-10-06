# Jira Service Management Automation

> End-to-end pattern for Slack → Jira ticket intake, auto‑triage, SLA routing, and self‑service knowledge with Confluence + ChatGPT.

## 🧰 Overview
This repo demonstrates how to reduce repetitive tickets and speed up IT responses by connecting Slack forms, Jira Automation rules, and a searchable KB.

## ⚙️ Implementation Highlights
- **Slack forms** (or /slash commands) call a webhook → create Jira issues
- **Jira Automation** sets priority, assigns groups, and posts status messages
- **SLA policies** by request type, with operational dashboards
- **Confluence KB** articles recommended by category (optionally ChatGPT‑assisted)

## 🏗️ Structure
```
/scripts/
  slack_to_jira_webhook.py   # receives Slack payloads → Jira REST
  kb_recommend.py            # suggests KB based on labels
/docs/
  workflows/*.png            # diagrams
  automation/*.json          # export of JSM rules
/examples/
  slack_payload.json
  jira_issue_example.json
```

## 🚀 Quick Start
```bash
python ./scripts/slack_to_jira_webhook.py --port 8080 --dry-run
# Test with: curl -X POST http://localhost:8080/hook -d @examples/slack_payload.json -H "Content-Type: application/json"
```

## 📈 Results (typical)
- ~40% reduction in repetitive “how do I” tickets
- Faster SLA response + clearer communication in Slack
- Better reporting for weekly ops reviews

## 🔐 Notes
- Store secrets (Jira token, Slack signing secret) in env vars or a secret manager
- Redact PII before sharing payload examples

## 🛣️ Roadmap
- [ ] MS Teams intake option
- [ ] Form validation + adaptive cards
- [ ] JSM Assets integration for device requests

## 🧠 Skills & Tools
`Jira Service Management` `Slack API` `Automation` `Confluence` `ChatGPT`

## 📝 License
MIT — see `LICENSE`.
