---
name: deep-analysis
description: Performs deep technical and product analysis of code, systems, workflows, or documents, identifying issues, risks, scalability limits, and improvement opportunities. Outputs a Microsoft-style PDF report. Use whenever the user asks to analyze, critique, evaluate, or deeply understand a system, code, or process.
---

# Deep Analysis Skill

## Purpose
Provide structured, senior-level analysis of any input (code, system, workflow, design).

## Behavior

When given input:

1. Generate structured JSON:

{
  "title": "Analysis title",
  "author": "Aman Samriya",
  "what_it_does": "Explanation of system/code purpose",
  "why_it_exists": "Problem it solves",
  "strengths": ["..."],
  "weaknesses": ["..."],
  "hidden_issues": ["..."],
  "risks": ["..."],
  "scalability": "How it behaves at scale",
  "edge_cases": ["..."],
  "improvements": ["..."],
  "pm_insights": ["..."],
  "summary": "Final evaluation"
}

2. Save as analysis_input.json

3. Run:

python .github/skills/deep-analysis/scripts/analyze.py analysis_input.json

## Style
- Think like senior engineer + PM
- Be critical, not just descriptive
- Highlight risks and trade-offs
- Suggest real improvements