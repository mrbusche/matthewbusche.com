import os
import shutil
import re

def organize_blog_posts(source_directory, destination_directory):
    """
    Organizes blog post files from a flat directory into a YYYY/MM/DD structure
    and renames them to post-title.md.

    Args:
        source_directory (str): The path to the directory containing the original files.
        destination_directory (str): The base path for the new organized structure.
    """
    # Ensure the destination directory exists
    os.makedirs(destination_directory, exist_ok=True)

    # Regex to match the filename pattern: YYYY-MM-DD-post-title.md
    # It captures year, month, day, and the rest of the title part.
    filename_pattern = re.compile(r'^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$')

    print(f"Starting file organization from '{source_directory}' to '{destination_directory}'...")

    processed_count = 0
    skipped_count = 0

    for filename in os.listdir(source_directory):
        # Construct the full path to the current file
        old_file_path = os.path.join(source_directory, filename)

        # Skip directories, process only files
        if os.path.isdir(old_file_path):
            continue

        match = filename_pattern.match(filename)
        if match:
            year, month, day, post_title_slug = match.groups()

            # Construct the new directory path: destination_directory/YYYY/MM/DD
            new_sub_directory = os.path.join(destination_directory, year, month, day)
            # Construct the new filename: post-title.md
            new_filename = f"{post_title_slug}.md"
            # Construct the full new file path
            new_file_path = os.path.join(new_sub_directory, new_filename)

            try:
                # Create the target directory if it doesn't exist
                os.makedirs(new_sub_directory, exist_ok=True)

                # Move and rename the file
                shutil.move(old_file_path, new_file_path)
                print(f"Moved and renamed: '{filename}' -> '{new_sub_directory}/{new_filename}'")
                processed_count += 1
            except Exception as e:
                print(f"Error processing '{filename}': {e}")
                skipped_count += 1
        else:
            print(f"Skipped '{filename}': Does not match the expected 'YYYY-MM-DD-post-title.md' pattern.")
            skipped_count += 1

    print("\n--- Summary ---")
    print(f"Successfully processed files: {processed_count}")
    print(f"Skipped files (due to pattern mismatch or errors): {skipped_count}")
    print("Organization complete!")

# --- How to use the script ---
# IMPORTANT:
# 1. Replace 'your_source_folder_path' with the actual path to your folder
#    containing the .md files.
# 2. Replace 'your_destination_folder_path' with the path where you want
#    the new YYYY/MM/DD structure to be created.
#    (e.g., 'organized_posts' in the same directory as the script).

# Example Usage:
# Assuming your script is in a folder and your markdown files are in a subfolder named 'posts'
# and you want the output in a subfolder named 'organized_posts'
# current_script_directory = os.path.dirname(os.path.abspath(__file__))
# source_folder = os.path.join(current_script_directory, 'posts')
# destination_folder = os.path.join(current_script_directory, 'organized_posts')

# For direct paths:
source_folder = 'content/blog' # e.g., 'C:\\Users\\YourUser\\Documents\\MyBlogPosts' or '/home/youruser/blog/posts'
destination_folder = 'content/blog2' # e.g., 'C:\\Users\\YourUser\\Documents\\OrganizedBlogPosts' or '/home/youruser/blog/organized'

# Uncomment the line below to run the script
organize_blog_posts(source_folder, destination_folder)

# Example of how to run it if you save this as a file, e.g., `organizer.py`:
# 1. Create a folder named 'my_blog_files' and put your example files inside it.
# 2. Create an empty folder named 'organized_blog_files' for the output.
# 3. Modify `source_folder` to `'./my_blog_files'`
# 4. Modify `destination_folder` to `'./organized_blog_files'`
# 5. Uncomment the `organize_blog_posts` call.
# 6. Run from your terminal: `python organizer.py`
