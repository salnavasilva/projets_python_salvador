import os

folder_path = input("Enter the folder path: ")
old_extension = input("Enter the current file extension (e.g., .txt): ")
new_extension = input("Enter the new file extension (e.g., .md): ")

# Ensure the extensions have the correct format
if not old_extension.startswith('.'):
    old_extension = '.' + old_extension
if not new_extension.startswith('.'):
    new_extension = '.' + new_extension

# Check if the folder exists
if not os.path.isdir(folder_path):
    print(f"The directory {folder_path} does not exist.")
else:
    # Loop through all files in the directory
    for filename in os.listdir(folder_path):
        # Check if the file has the old extension
        if filename.endswith(old_extension):
            # Construct the full file path
            old_file_path = os.path.join(folder_path, filename)
            # Replace the old extension with the new one
            new_filename = filename[:-len(old_extension)] + new_extension
            new_file_path = os.path.join(folder_path, new_filename)
            try:
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {old_file_path} -> {new_file_path}')
            except Exception as e:
                print(f'Failed to rename {old_file_path} -> {new_file_path}: {e}')
