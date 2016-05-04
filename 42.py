import re


def word_value(word):
    return sum(score[c] for c in word)

score = {c: i+1 for (i, c) in enumerate("abcdefghijklmnopqrstuvwxyz")}
triangles = set(n * (n + 1) / 2 for n in xrange(1000))

with open("42_words.txt", "r") as f:
    words = re.findall("\"(.*?)\"", f.read())

words = [word.lower() for word in words]
triangle_words = 0
for word in words:
    if word_value(word) in triangles:
        triangle_words += 1
print triangle_words
