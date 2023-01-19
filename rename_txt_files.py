# Renames txt files with extra extensions (e.g. .jpg.txt) to just .txt
import os

# Absolute path to directory containing files to be processed
PATH = "F:/Projects/stable_diffusion/images/path/to/images"

files = os.listdir(PATH)
countfiles = 0
for file in files:
    if os.path.splitext(file)[1] == ".txt":
        # Get file name without extension
        filename = os.path.splitext(file)[0]
        # Get file extension
        ext = os.path.splitext(file)[1]
        # Removes .png, .jpg, etc. from filename
        filename = os.path.splitext(filename)[0]
        # Trim spaces at end of filename
        filename = filename.strip()
        # print (filename + ext)
        # Rename file
        try:
            os.rename(os.path.join(PATH, file), os.path.join(PATH, filename + ext))
            countfiles += 1
        except:
            print("Error renaming file: " + file)
print("Renamed " + str(countfiles) + " files.")
