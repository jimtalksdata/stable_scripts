# Processes files in specified directory (absolute path) and renames
# Adds prefix PREFIX to file name
# Adds suffix SUFFIX to file name
# Searches filename for TOKENS (non case sensitive); if found, moves TOKEN to end of filename
# Replaces all non alphanumeric characters with spaces

import os

PREFIX = "a picture of "
SUFFIX = ", by d&d"
TOKENS = ["3e", "4e", "5e"]
TOKENS_TO_REMOVE = ["token"]

# Absolute path to directory containing files to be processed
PATH = "F:/Projects/stable_diffusion/images/path/to/images"

# Get list of files in directory
files = os.listdir(PATH)
for file in files:
    # Get file name without extension
    filename = os.path.splitext(file)[0]
    # Get file extension
    ext = os.path.splitext(file)[1]
    # Replace non alphanumeric characters with spaces
    filename = "".join([char if char.isalnum() else " " for char in filename])
    # Trim spaces at end of filename
    filename = filename.strip()
    # Add prefix
    filename = PREFIX + filename
    # Add suffix
    filename = filename + SUFFIX
    # Remove tokens
    for token in TOKENS_TO_REMOVE:
        if token in filename.lower():
            filename = filename.replace(token, "").strip()
    # Search for tokens
    for token in TOKENS:
        if token in filename.lower():
            # Move token to end of filename
            filename = filename.replace(token, "").strip() + " " + token
    # Remove extra spaces
    filename = " ".join(filename.split())
    # print new filename
    print(filename)
    # Rename file
    os.rename(os.path.join(PATH, file), os.path.join(PATH, filename + ext))

