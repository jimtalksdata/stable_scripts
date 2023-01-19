# Processes files in specified directory (absolute path) with accompanying .txt files
# Adds prefix PREFIX to beggining of .txt file
# Adds suffix SUFFIX to end of .txt file
# Searches .txt file for TOKENS (non case sensitive); if found, moves TOKEN to end of filename
# Converts all newlines in .txt file to commas
# Replaces all non alphanumeric characters with spaces

import os

PREFIX = "a picture of "
SUFFIX = ", by d&d"
TOKENS = ["3e", "4e", "5e"]
TOKENS_TO_REMOVE = ["token"]

TXT_TOKENS_TO_REMOVE = ["filename:","series:","title:","creator:","rating:","species:","character:","name:"]

# Absolute path to directory containing files to be processed
PATH = "F:/Projects/stable_diffusion/images/path/to/images"

# Get list of files in directory
countfiles = 0
files = os.listdir(PATH)
for file in files:
    # if file is an image
    if os.path.splitext(file)[1] != ".txt":
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
        # Open corresponding .txt file
        txt_file_name = os.path.splitext(file)[0] + ext + ".txt"
        txt_file_name_new_name = os.path.splitext(file)[0] + ".txt"
        with open(os.path.join(PATH, txt_file_name),'r+') as f:
            # Read .txt file
            txt = f.read()
            # Replace newlines with commas
            txt = txt.replace("\n", ", ")
            # Replace TXT_TOKENS_TO_REMOVE with ""
            for token in TXT_TOKENS_TO_REMOVE:
                txt = txt.replace(token, "")
            # prepend filename to .txt file
            txt = filename + ", " + txt
            print(txt)
            # Replace existing .txt file
            f.seek(0, 0)
            f.write(txt)
            countfiles += 1
        # Rename .txt file removing ext
        try:
            os.rename(os.path.join(PATH, txt_file_name), os.path.join(PATH, txt_file_name_new_name))
        except:
            print("Error renaming file: " + txt_file_name)
print("Processed " + str(countfiles) + " files.")
