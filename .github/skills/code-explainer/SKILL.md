---
name: code-explainer
description: Explains any given code snippet (Python, C++, Java, JS, Go, etc.) in both layman and technical depth and produces a Microsoft-style PDF report. Use whenever the user asks to explain, understand, analyze, study, break down, walk through, or document code.
---

# Code Explainer Skill (Pro – PDF Output)

## Purpose
Generate a deep, well-structured explanation of any code snippet, with both layman analogy and technical breakdown, saved as a Microsoft-style PDF.

## Behavior

When the user provides code:

1. Detect the language
2. Understand the code
3. Generate the following JSON and save as code_input.json:

{
  "title": "Short descriptive name of the code",
  "language": "Python | C++ | JavaScript | Java | Go | ...",
  "author": "Aman Samriya",
  "original_code": "the original code as string",
  "summary_layman": "Simple explanation for non-engineers",
  "step_by_step": [
    "Step 1 explanation",
    "Step 2 explanation",
    "Step 3 explanation"
  ],
  "analogy": "Real-world analogy that makes the code intuitive",
  "inputs_outputs": [
    { "input": "example input", "output": "example output" }
  ],
  "what_it_delivers": "What this code achieves in real-world terms",
  "edge_cases": ["..."],
  "strengths": ["..."],
  "weaknesses": ["..."],
  "improvements": ["..."],
  "summary_final": "1-2 sentence wrap-up of the code's purpose and quality"
}

4. Run script:

python .github/skills/code-explainer/scripts/explain_code.py code_input.json

The script will:
- Create CodeExplainers/ folder
- Generate Microsoft-style PDF
- Auto-open it

## Style Rules
- Use clear, friendly language
- Avoid jargon unless explained
- Layman first, technical second
- Always include analogy
- Always include strengths and weaknesses
- Always include improvements
- Keep tone like an experienced engineer mentoring a junior