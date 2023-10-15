"""
CP1404/CP5632 Practical 5 - Do-from-scratch exercise 1
Word Occurrences
Estimate: 20 minutes
Actual: 9 minutes  # though current program doesn't account for punctuation, capitalisation etc.
"""

words = input("Text: ").split()
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

width = max((len(word) for word in words))
for word, count in sorted(word_to_count.items()):
    print(f"{word:{width}} : {count}")
