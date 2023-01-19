# Find and replace script for multiple files
# Gets a list of files from a recursively directory and replaces a word in each file
# If one parameter is selected "word_to_replace" then it will return lines containing matches of the word, and the filename
# If two parameters are selected "word_to_replace" and "replacement_word" then it will replace the word
# If "replacement_word" contains a (d), replace with the name of the dir containing the file (d2 for dir 2 levels up, etc)
# If "replacement_word" contains a (f), replace with the name of the file

from glob import glob
import os
import sys
import re

def find_replace_words_in_files(path, word_to_replace, replacement_word):
    files = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.txt'))]
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            filename = os.path.basename(file)
            last_dir = os.path.basename(os.path.dirname(file))
            dir_2_up = os.path.basename(os.path.dirname(os.path.dirname(file)))
            dir_3_up = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(file))))
            for line in lines:
                if replacement_word and '(d)' in replacement_word:
                    replacement_word = replacement_word.replace('(d)', last_dir)
                if replacement_word and '(d2)' in replacement_word:
                    replacement_word = replacement_word.replace('(d2)', dir_2_up)
                if replacement_word and '(d3)' in replacement_word:
                    replacement_word = replacement_word.replace('(d3)', dir_3_up)
                if replacement_word and '(f)' in replacement_word:
                    replacement_word = replacement_word.replace('(f)', filename)
                if word_to_replace in line:
                    print(file + ":" + line)
                    if replacement_word:
                        new_line = re.sub(word_to_replace, replacement_word, line)
                        print(new_line)
                        with open(file, 'w') as f:
                            f.seek(0)
                            f.write(new_line)

if __name__ == '__main__':
    path = sys.argv[1]
    word_to_replace = sys.argv[2]
    if len(sys.argv) == 4:
        replacement_word = sys.argv[3]
    else:
        replacement_word = None
    find_replace_words_in_files(path, word_to_replace, replacement_word)