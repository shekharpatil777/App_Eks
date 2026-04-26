import sys
from collections import Counter

def word_frequency():
    # Read all input from stdin and split into words
    # .split() without arguments handles any whitespace (spaces, tabs, newlines)
    input_data = sys.stdin.read().split()
    
    # Count the frequency of each word
    word_counts = Counter(input_data)
    
    # Sort by frequency (descending)
    # word_counts.items() returns (word, count) tuples
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Print the result in the required format: "word frequency"
    for word, count in sorted_counts:
        print(f"{word} {count}")

if __name__ == "__main__":
    word_frequency()