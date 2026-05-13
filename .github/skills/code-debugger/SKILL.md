---
name: code-debugger
description: Performs structured root cause analysis on code errors and produces a Microsoft-style PDF debug report with symptom, root cause, fix, tests, and prevention tips. Use whenever the user asks to debug, fix, analyze, investigate, troubleshoot, or RCA a piece of code or error.
---

# Code Debugger Skill (Pro – PDF Output)

## Purpose
Generate a professional, structured debug report for any code issue, with engineering-grade reasoning.

## Behavior

When the user provides:
- Code snippet
- Error message or unexpected behavior
- Expected behavior (optional)

Generate a JSON file like below and save it as debug_input.json:

{
  "title": "Short bug title",
  "author": "Aman Samriya",
  "symptom": "What is happening",
  "root_cause": "Why it is happening",
  "reasoning": [
    "Step 1 observation",
    "Step 2 observation",
    "Step 3 observation"
  ],
  "code_before": "original buggy code",
  "code_after": "fixed code",
  "tests": "unit test code as a string",
  "prevention": [
    "Tip 1",
    "Tip 2",
    "Tip 3"
  ],
  "severity": "Low | Medium | High",
  "impact": "What the bug causes",
  "fix_complexity": "Low | Medium | High",
  "priority": "Low | Medium | High",
  "summary": "Final summary of the issue and fix"
}

Then run:

python .github/skills/code-debugger/scripts/debug_report.py debug_input.json

The script will:
- Create a Microsoft-style PDF
- Auto-open it
- Save under DebugReports/

## Style Rules
- Use clear, technical language
- Use bullet points where possible
- Maintain professional engineering tone
- Always include tests
- Always include prevention tips