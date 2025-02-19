import json
import os
import subprocess

# Get the MODULEPATH environment variable
modulepath = os.environ.get("MODULEPATH")

if not modulepath:
    print("Error: MODULEPATH environment variable is not set.")
    exit(1)

# Run the 'spider' command and capture its JSON output
try:
    cmd = f"/hpc/modules/lmod/lmod/libexec/spider -o jsonSoftwarePage {modulepath}"
    result = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=True)
    json_data = result.stdout.strip()

    # Debug: Print raw output before parsing
    if not json_data:
        print("Error: No JSON output received from spider command.")
        exit(1)

    software_list = json.loads(json_data)

except subprocess.CalledProcessError as e:
    print(f"Error running spider command: {e}")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error parsing JSON output: {e}")
    exit(1)

# Generate Markdown output
md_output = "# Available Software Modules\n\n"

for software in software_list:
    package_name = software.get("package", "Unknown Package")
    description = software.get("description", "No description available.")

    # Keep section headers as requested
    md_output += f"## {package_name}\n"
    md_output += f"**Description:** {description}\n\n"

    # Start the table for module file paths
    md_output += "| **Module File Path** |\n"
    md_output += "|----------------------|\n"

    # Populate the table with paths
    for version in software.get("versions", []):
        path = version.get("path", "Unknown path")
        md_output += f"| `{path}` |\n"

    md_output += "\n---\n"

# Save to a Markdown file
with open("software_modules.md", "w") as f:
    f.write(md_output)

print("Markdown documentation generated: software_modules.md")
