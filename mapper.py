#!/usr/bin/env python3 
import sys
import csv
import re

def tokenize(text):
    # Tokenization that removes symbols and numbers, keeping only alphabetic words
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())  # Match only alphabetic words
    return words

# Use csv.reader to properly handle commas in the fields
csv_reader = csv.reader(sys.stdin)

for row in csv_reader:
    # Check if there are at least 5 columns
    if len(row) < 5:
        continue  # Skip rows with fewer than 5 columns

    # Select the 10th column (index 9)
    column_10_text = row[9].strip()  # Strip any leading/trailing whitespace from the column

    # Check if the 10th column is empty
    if not column_10_text:
        continue  # Skip if the column is empty

    # Tokenize the 10th column text
    words = tokenize(column_10_text)
    
    # Skip if no words were found
    if not words:
        continue

    # Output each word's individual count
    for word in words: 
        print(f'{word}\t1')
