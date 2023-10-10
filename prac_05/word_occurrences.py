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

pairs = sorted(word_to_count.items())
width = max((len(pair[0]) for pair in pairs))

for pair in pairs:
    print(f"{pair[0]:{width}} : {pair[1]}")
