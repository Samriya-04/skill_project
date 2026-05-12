\---

name: excel-generator

description: Generates Excel files based on user-provided columns and rows. Use whenever the user asks to create or build an Excel file.

\---



\# Excel Generator Skill



\## Instructions



1\. Understand what the user wants:

&#x20;  - File name

&#x20;  - Columns

&#x20;  - Rows



2\. Convert request into JSON:

{

&#x20; "file\_name": "data.xlsx",

&#x20; "columns": \["Name", "Age"],

&#x20; "rows": \[\["Aman", 21], \["Rahul", 22]]

}



3\. Run the script:

python ./scripts/generate\_excel.py '<JSON>'



4\. Share the file path of the created Excel.

