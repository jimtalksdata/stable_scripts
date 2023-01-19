# Creates a list of ngrams from all text files in the given path (recursive)
import os
from glob import glob
import re

PATH = "F:/Projects/stable_diffusion/images/path/to/images"
NGRAMS = 1
MIN_LENGTH = 3

def generate_ngrams(s, n):
    # Convert to lowercases
    s = s.lower()
    
    # Replace all none alphanumeric characters with spaces
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    
    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]
    
    # Discard tokens that are too short
    tokens = [token for token in tokens if len(token) >= MIN_LENGTH]
    
    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]

"""Given a list of ngrams, return a dictionary of ngram counts
"""
def ngrams(generated_ngrams_list):
    ngram_counts = {}
    for ngram in generated_ngrams_list:
        if ngram in ngram_counts:
            ngram_counts[ngram] += 1
        else:
            ngram_counts[ngram] = 1
    return ngram_counts
    

files = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.txt'))]
ngram_full_dict = {}
countfiles = 0
maxtokens = 0
filename_of_maxtokens = ""
for file in files:
    countfiles += 1
    with open(file, 'r') as f:
        text = f.read()
        maxtokens = max(maxtokens, len(text.split()))
        filename_of_maxtokens = file if len(text.split()) == maxtokens else filename_of_maxtokens
        ngram_dict = ngrams(generate_ngrams(text, NGRAMS))
        # merge dictionaries and increment counts
        ngram_full_dict = {k: ngram_full_dict.get(k, 0) + ngram_dict.get(k, 0) for k in set(ngram_full_dict) | set(ngram_dict)}
        
ngram_full_dict = {k: v for k, v in sorted(ngram_full_dict.items(), key=lambda item: item[1], reverse=True)}
# write to file
FILE_TO_WRITE = PATH + "/ngrams.txt"
with open(FILE_TO_WRITE, "w") as f:
    for k, v in ngram_full_dict.items():
        f.write(k + ": " + str(v) + "\n")
        
print("Processed " + str(countfiles) + " files and found " + str(len(ngram_full_dict)) + " unique ngrams.")
print("Max tokens in a file: " + str(maxtokens) + " in file " + filename_of_maxtokens)