import re


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_values = {c: i + 1 for i, c in enumerate(alphabet)}

with open('22_names.txt', 'r') as f:
    names = re.findall('"(.*?)"', f.readline())

names.sort()
total = 0
for i, name in enumerate(names):
    name_score = sum([alphabet_values[c] for c in name])
    total += (i + 1) * name_score

print total
