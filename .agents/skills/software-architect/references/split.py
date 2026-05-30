import os

file_path = r"e:\Escritorio\Agentic Workspace\.agents\skills\software-architect\references\design-patterns.md"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

header_lines = []
creational_lines = []
structural_lines = []
behavioral_lines = []

current_section = "header"

for line in lines:
    if line.startswith("## Creational Patterns"):
        current_section = "creational"
    elif line.startswith("## Structural Patterns"):
        current_section = "structural"
    elif line.startswith("## Behavioral Patterns"):
        current_section = "behavioral"
    
    if current_section == "header":
        header_lines.append(line)
    elif current_section == "creational":
        creational_lines.append(line)
    elif current_section == "structural":
        structural_lines.append(line)
    elif current_section == "behavioral":
        behavioral_lines.append(line)

dir_path = os.path.dirname(file_path)

def write_file(name, content_lines):
    if not content_lines: return
    # Add header to sections if it doesn't have one
    content = "".join(header_lines) + "".join(content_lines)
    with open(os.path.join(dir_path, name), "w", encoding="utf-8") as f:
        f.write(content)

write_file("patterns-creational.md", creational_lines)
write_file("patterns-structural.md", structural_lines)
write_file("patterns-behavioral.md", behavioral_lines)

print("Files created successfully.")

# Delete original file
os.remove(file_path)
print("Original file deleted.")
