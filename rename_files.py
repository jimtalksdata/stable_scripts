# Given directory (absolute path) containing files to be processed
# Renames files containing SRC with DEST recursively

import os

# Absolute path to directory containing files to be processed
PATH = "F:/Projects/stable_diffusion/images/path/to/images"

SRC = "by d&d"
DEST = " , by d&d"

# Get list of files in directory
files = os.listdir(PATH)
for file in files:
    # Get file name without extension
    filename = os.path.splitext(file)[0]
    # Get file extension
    ext = os.path.splitext(file)[1]
    # Replace non alphanumeric characters with spaces
    # filename = "".join([char if char.isalnum() else " " for char in filename])
    # Trim spaces at end of filename
    filename = filename.strip()
    # Replace SRC with DEST
    filename = filename.replace(SRC, DEST)
    # Remove extra spaces
    filename = " ".join(filename.split())
    # print new filename
    print(filename)
    # Rename file
    os.rename(os.path.join(PATH, file), os.path.join(PATH, filename + ext))
