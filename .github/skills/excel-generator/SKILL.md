---
name: excel-generator
description: Generates Excel files based on user-provided columns and rows. Use whenever the user asks to create or build an Excel file.
---

# Excel Generator Skill

## Instructions

1. Understand what the user wants:
   - File name
   - Columns
   - Rows

2. Convert request into JSON:

   {
     "file_name": "data.xlsx",
     "columns": ["Name", "Age"],
     "rows": [["Aman", 21], ["Rahul", 22]]
   }

3. Run the script:

   python ./scripts/generate_excel.py input.json

4. Share the file path of the created Excel.
