"""This file is used to auto generate software list into page called
software_modules.md which is then displayed in documentation. Just 
run this script and it will generate the markdown file then copy the 
generated markdown to its desired location
"""
import json
import subprocess
import os
modulepath = os.environ.get("MODULEPATH")

# Run the 'spider' command and capture its JSON output
try:
    cmd = f"/hpc/modules/lmod/lmod/libexec/spider -o jsonSoftwarePage {modulepath}"
    result = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=True)
    json_data = result.stdout  # Capture the command output
    print(json_data)
except subprocess.CalledProcessError as e:
    print(f"Error running spider command: {e}")
    exit(1)

# Parse JSON output
try:
    software_list = json.loads(json_data)
except json.JSONDecodeError as e:
    print(f"Error parsing JSON output: {e}")
    exit(1)

# software_list = json.loads(json_data)
# Generate Markdown output
md_output = "# Available Software Modules\n\n"

for software in software_list:
    package_name = software.get("package", "Unknown Package")
    description = software.get("description", "No description available.")

    md_output += f"## {package_name}\n"
    md_output += f"**Description:** {description}\n\n"
    
    for version in software.get("versions", []):
        path = version.get("path", "Unknown path")
        md_output += f"- **Module File Path:** `{path}`\n"
    
    md_output += "\n---\n"

# Save to a Markdown file
with open("software_modules.md", "w") as f:
    f.write(md_output)

print("Markdown documentation generated: software_modules.md")
