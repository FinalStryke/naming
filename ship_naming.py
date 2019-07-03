import random

prefix = []

weapons = ["Sword", "Spear", "Pike", "Lance", "Bow", "Arrow",
           "Halberd", "Scimitar", "Shield", "Scythe", "Dagger",
           "Gladius", "Javelin", "Morningstar"]

music = ["Dirge", "March", "Waltz", "Sonata", "Hymn", "Chant",
         "Symphony", "Concerto"]

emotions = ["Rage", "Sorrow", "Joy", "Vengeance", "Longing"]

supernatural = ["Ghost", "Banshee", "Spectre", "Ghoul", "Demon",
                "Angel", "Orc", "Imp", "Geist"]

nobility = ["Noble", "Lord", "King", "Queen", "Duke", "Duchess",
            "Prince", "Princess", "Baron", "Baronet", "Daimyo",
            "Nobility"]

p_nouns = ["Pillar", "Leaf", "Flame", "Crystal", "Bolt", "Jet", "Gem",
           "Stone", "Lay", "Wind", "Ice", "Fire", "Storm", "Fang",
           "Tail", "Claw", "Shiver", "Chill", "Heat", "Scorch",
           "Garden", "Key", "Lock", "Fountain", "Statue", "Book",
           "Tome", "Scroll", "Last Word", "Thorn", "Shawl", "Cloak",
           "Helm", "Shadow", "Light", "Fastness", "Bulwark", "Titan",
           "Hydra", "Crown", "Sceptre", "Throne", "Dust", "Void",
           "Hand", "Leap"]


suffix = []

seasons = ["Spring", "Summer", "Autumn", "Winter"]

day = ["Day", "Night", "Dawn", "Morning", "Noon", "Afternoon", "Sunset",
       "Midnight"]

heroes = ["Gilgamesh", "Beowulf", "Arthur", "Enkidu", "Hercles",
          "Leonidas", "Altria", "Jason", "Cu Chulainn", "Odysseus",
          "Achilles", "Hector", "Aeneas", "Duryodhana", "Vainamoinen"]

gods = ["Odin", "Thor", "Hermes", "Titan", "Zeus", "Saturn"]

legendary_weapons = ["Excalibur", "Masamune", "Murasame", "Caesura"]

cities = ["Damascus", "Instanbul", "Constantinople", "Nairobi",
          "Cairo", "Insomnia", "Midgard", "Lindblum","Alexandria"]

s_nouns = ["Flame", "Stone", "Ice", "Fire", "Storms", "Dust", "Light",
           "Shadow"]

prefix.extend(weapons)
prefix.extend(music)
prefix.extend(emotions)
prefix.extend(supernatural)
prefix.extend(p_nouns)

suffix.extend(seasons)
suffix.extend(day)
suffix.extend(heroes)
suffix.extend(gods)
suffix.extend(legendary_weapons)
suffix.extend(cities)
suffix.extend(s_nouns)

def build_ship(begin, end):
    """Return the name of a ship."""
    ship_name = ["The " + begin + " of " + end]
    return ship_name

first = random.choice(prefix)
last = random.choice(suffix)

name = build_ship(first, last)
print(name)
