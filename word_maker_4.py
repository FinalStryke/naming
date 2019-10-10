import random

letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Using Scrabble distributions, minus the vowels
consonant = ["t", "t", "t", "t", "t", "t", "r", "r", "r", "r", "r", "r", "n",
        "n", "n", "n", "n", "n", "s", "s", "s", "s", "l", "l", "l", "l", "d",
        "d", "d", "d", "g", "g", "g", "g", "p", "p", "m", "m", "c", "c", "b",
        "b", "y", "y", "w", "w", "v", "v", "h", "h", "f", "f", "k", "j", "x",
        "qu", "z"]

# 50/50 a vowel is used at all
vowel = ["", "", "", "", "", "a", "e", "i", "o", "u"]


start = ""
first = random.choice(letter)
if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
    start += first
elif first == "t" or first == "d":
    start += first
    start += random.choice()
elif first == "n" or first == "m":
    start += first
    start += random.choice(["a", "e", "i", "o", "u"])
elif first == "s" or first == "z":
    start += first
    start += random.choice(["a", "e", "i", "o", "u", "r", "l", "w", "k", "t", "p"])
elif first == "k" or first == "c" or first == "g":
    start += first
    start += random.choice(["a", "e", "i", "o", "u", "r", "l", "w"])
elif first == "p" or first == "b":
    start += first
    start += random.choice(["a", "e", "i", "o", "u", "r", "l"])
elif first == "f" or first == "v":
    start += first
    start += random.choice(["a", "e", "i", "o", "u", "r", "l"])
elif first == "h":
    start += first
    start += random.choice(["a", "e", "i", "o", "u"])
elif first == "j":
    start += first
    start += random.choice(["a", "e", "i", "o", "u", "r", "h"])
elif first == "l" or first == "r":
    start += first
    start += random.choice(["a", "e", "i", "o", "u"])
elif first == "q":
    start += first
    start += "u"
    start += random.choice(["a", "e", "i", "o", "u"])
elif first == "w":
    start += first
    start += random.choice(["a", "e", "i", "o", "u", "r"])
elif first == "x":
    start += first
    start += random.choice(["a", "e", "i", "o", "u", "c"])
elif first == "y":
    start += first
    start += random.choice(["a", "e", "i", "o", "u"])


word = start

length = random.randint(2, 5)

while length > 0:
    word += random.choice(consonant)
    word += random.choice(vowel)
    length -= 1

print(word.capitalize())
