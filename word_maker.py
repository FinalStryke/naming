import random

# Using Scrabble distributions, minus the vowels
consonant = ["t", "t", "t", "t", "t", "t", "r", "r", "r", "r", "r", "r", "n",
        "n", "n", "n", "n", "n", "s", "s", "s", "s", "l", "l", "l", "l", "d",
        "d", "d", "d", "g", "g", "g", "g", "p", "p", "m", "m", "c", "c", "b",
        "b", "y", "y", "w", "w", "v", "v", "h", "h", "f", "f", "k", "j", "x",
        "qu", "z"]

# 50/50 a vowel is used at all
vowel = ["", "", "", "", "", "a", "e", "i", "o", "u"]

word = ""

length = random.randint(3, 8)

while length > 0:
    word += random.choice(consonant)
    word += random.choice(vowel)
    length -= 1

print(word.capitalize())
