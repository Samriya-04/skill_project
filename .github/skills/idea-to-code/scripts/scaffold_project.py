import os, sys, json, subprocess

def main():
    if len(sys.argv) < 2:
        print("❌ Provide JSON input file")
        return

    arg = sys.argv[1]
    try:
        with open(arg, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = json.loads(arg)

    project_name = data.get("project_name", "new_project")
    files = data.get("files", {})
    dependencies = data.get("dependencies", [])
    description = data.get("description", "")
    language = data.get("language", "python")

    base_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(base_path, exist_ok=True)

    # Create files
    for filename, content in files.items():
        file_path = os.path.join(base_path, filename)
        # Make parent folder if needed
        os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(filename) else None
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Created: {file_path}")

    # Ensure requirements.txt
    req_path = os.path.join(base_path, "requirements.txt")
    if dependencies and not os.path.exists(req_path):
        with open(req_path, "w", encoding="utf-8") as f:
            f.write("\n".join(dependencies))
        print(f"✅ Created: {req_path}")

    # Ensure README
    readme_path = os.path.join(base_path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {project_name}\n\n{description}\n\n## Setup\n\n```\npip install -r requirements.txt\npython main.py\n```\n")
        print(f"✅ Created: {readme_path}")

    print(f"\n🎉 Project scaffold created at: {base_path}")

    # Auto-open in VS Code
    try:
        subprocess.Popen(["code", base_path], shell=True)
    except Exception as e:
        print(f"⚠️ Could not auto-open in VS Code: {e}")

if __name__ == "__main__":
    main()