import random

prefix = ["archaeo", "arachno", "ferro", "klepto", "draco", "bio"]

suffix = ["mancer", "ologist", "mania", "phobia"]

first = random.choice(prefix)

last = random.choice(suffix)

if first[-1] == last[0]:
    last = last[1:]

word = first + last

print(word.capitalize())
