"""
CP1404/CP5632 Practical 5 - Do-from-scratch exercise 1
Word Occurrences
Estimate: 20 minutes
Actual: 9 minutes  # though current program doesn't account for punctuation, capitalisation etc.
"""

words = input("Text: ").split()
word_to_count = {}
width = 0
for word in words:
    if len(word) > width:
        width = len(word)
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

for word, count in sorted(word_to_count.items()):
    print(f"{word:{width}} : {count}")
