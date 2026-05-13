---
name: weekly-status-report
description: Generates a Microsoft-style weekly status report as a PDF from user notes and automatically opens it. Use whenever the user asks to create, draft, summarize, or write a weekly update, status report, EOW update, weekly summary, weekly progress report, or end-of-week report.
---

# Weekly Status Report Skill (PDF Version)

## Purpose
Generate a clean, Microsoft-style weekly status report as a professional PDF.

## Behavior

Convert user notes into JSON with these sections:

{
  "title": "Weekly Status Report",
  "author": "Aman Samriya",
  "highlights": ["..."],
  "progress": ["..."],
  "blockers": ["..."],
  "next_week": ["..."],
  "asks": ["..."]
}

Save it to report_input.json, then run:

python .github/skills/weekly-status-report/scripts/generate_report.py report_input.json

The script will:
- Create a Microsoft-style PDF
- Save with today's date in filename
- Auto-open the PDF

## Formatting Rules
- Use bullet points
- Concise and professional
- Highlights at the top
- Use exec-friendly language