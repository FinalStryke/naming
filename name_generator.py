import random

phonemes = ["am", "an", "and", "ash", "ba", "bal", "bar", "be", "bel",
            "ber", "el", "en", "il", "ish", "ki", "kir", "ni", "nin",
            "om", "or", "rah", "sal", "sar", "ta", "tal", "tan", "tau",
            "te", "tev", "tem", "to", "tok", "tol", "ton", "va", "vae",
            "val", "vam", "van" "var"]

name = ""

length = random.randint(2, 6)

while length > 0:
    name += random.choice(phonemes)
    length -= 1

print(name.capitalize())
