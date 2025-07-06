import os

def add_permalinks(root_dir):
    """
    Adds a permalink to .md files if it doesn't exist, after the 'date:' line.
    The permalink is generated from the file's relative path and excludes the .md extension.
    Reads and writes files using utf-8 encoding.
    """
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                filepath = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(filepath, root_dir)

                # Construct the permalink
                # 1. Replace backslashes with forward slashes for URL consistency on Windows
                # 2. Remove the .md extension
                permalink = "/" + relative_path.replace("\\", "/").replace(".md", "")

                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                except UnicodeDecodeError:
                    print(f"Skipping {filepath}: Could not decode with utf-8. Please check file encoding.")
                    continue

                permalink_exists = False
                date_line_index = -1

                for i, line in enumerate(lines):
                    if line.strip().startswith("permalink:"):
                        permalink_exists = True
                        break
                    if line.strip().startswith("date:"):
                        date_line_index = i

                if not permalink_exists and date_line_index != -1:
                    # Insert the permalink line
                    lines.insert(date_line_index + 1, f"permalink: {permalink}\n")

                    try:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        print(f"Added permalink to: {filepath} -> {permalink}")
                    except Exception as e:
                        print(f"Error writing to {filepath}: {e}")
                elif permalink_exists:
                    print(f"Permalink already exists in: {filepath}")
                else:
                    print(f"Could not find 'date:' line or permalink already exists in: {filepath}")

# --- How to use it ---
# IMPORTANT:
# Replace 'path/to/your/articles/directory' with the actual path to your top-level articles folder.
# This should be the directory from which you want the relative paths to be calculated.
#
# Example:
# If your project structure is:
# my_project/
# └── content/
#     ├── 2025/
#     │   └── 03/
#     │       └── 06/
#     │           └── using-poetry.md
#     └── another-post.md
#
# And you want permalinks like /2025/03/06/using-poetry
# Then your `root_directory` should be 'my_project/content'

root_directory = "content/blog"
add_permalinks(root_directory)
