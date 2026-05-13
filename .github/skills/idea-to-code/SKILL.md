---
name: idea-to-code
description: Converts a high-level idea into a working project scaffold with code skeleton, folder structure, README, dependencies, and architecture suggestions. Use whenever the user asks to build, scaffold, generate, prototype, draft, design, or create a new code project, tool, script, or app.
---

# Idea-to-Code Skill

## Purpose
Turn a rough product or technical idea into a clean, ready-to-run Python project scaffold.

## Behavior

When the user gives an idea:

1. Understand the idea — its goal, functionality, and constraints.
2. Suggest:
   - A short architecture
   - Required libraries
   - File structure
3. Generate the following JSON:

{
  "project_name": "folder-name",
  "description": "Short description of the project",
  "language": "python",
  "dependencies": ["package1", "package2"],
  "files": {
    "main.py": "code content here",
    "utils.py": "code content here",
    "README.md": "Project description and run instructions",
    "requirements.txt": "package1\npackage2"
  }
}

4. Save as project_input.json
5. Run script:

python .github/skills/idea-to-code/scripts/scaffold_project.py project_input.json

6. The script will:
   - Create folder
   - Create files
   - Add boilerplate
   - Auto-open in VS Code

## Code Quality Rules
- Always include comments
- Add TODOs for engineering work
- Use functions/classes (no spaghetti code)
- Modular structure
- Include basic error handling
- Include a sample test in tests/ folder when relevant

## Output Style
- Professional
- Beginner-friendly
- Production-leaning
- Clear naming