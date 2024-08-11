#!/usr/bin/env python3
from collections import defaultdict
import sys

word_counts = defaultdict(int)  # Stores words and counts

for line in sys.stdin:
    try:
        # Remove leading/trailing whitespaces and split the line by tab
        line = line.strip()
        word, count = line.split('\t', 1)  # Use '\t' as delimiter and split only once

        # Convert count to integer
        count = int(count)
    except ValueError:
        continue  # Skip the line if it does not meet the expected format

    # Add the count for each word
    word_counts[word] += count

# Sort the word counts by count in descending order and retrieve the top 50
top_50_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:50]

# Output the top 50 words with their counts
for word, count in top_50_words:
    print(f'{word}\t{count}')
