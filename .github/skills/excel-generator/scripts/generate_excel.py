import pandas as pd
import json
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("❌ No input provided")
        return

    data = json.loads(sys.argv[1])

    file_name = data.get("file_name", "output.xlsx")
    columns = data.get("columns", [])
    rows = data.get("rows", [])

    df = pd.DataFrame(rows, columns=columns)
    output_path = os.path.join(os.getcwd(), file_name)
    df.to_excel(output_path, index=False)

    print(f"✅ Excel file created: {output_path}")

if __name__ == "__main__":
    main()