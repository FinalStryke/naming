import random

male_name = []

female_name = []

misc_name = []

jpop = ["Ayumi", "Hikaru", "Mao", "Atsuko", "Yuuko", "Lisa",
        "Hitomi", "Regina", "Kia", "Kanna", "An"]

kpop_f = ["Lisa", "Jeannie", "Rose", "Taeyeon", "Eunjung", "Hyomin", "Bom", "CL", "Dara", "Minzy"]

kpop_m = ["G-Dragon", "T.O.P.", "Taeyang", "Daesung", "Jin", "Suga", "J-Hope", "RM", "Jimin", "V", "Jungkook"]

characters_m = ["Dwayne", "Perrin Murksorrow",
                        "Raphrok Lunthiel", "Eli Tram", "Thud",
                        "Sargent Ulthane", "Venn Tasarm", "Perch",
                        "Blythe", "Alko Riverfellow", "Dura Ruutag",
                        "Vark Fulton", "Tugon the Cursed",
                        "Alexander Rootish", "Erndok Bottlebuster",
                        "Dogrim", "Alok", "Tanith", "Harmon Strongnet",
                        "Tawn Thundercave", "Rayne Vale", "Lambug",
                        "Mahka"]

characters_f = ["Tira", "Cora", "Allin", "Maki", "Lura Ruutag",
                       "Patricia Rootish", "Eivie Pettysprite",
                       "Floehilda Bottlebuster", "Dana Oakbow", "Leela",
                       "Braide Barrenblossom", "Augustine Feldspar"]

bands = ["Insomnium", "Amon Amarth", "Soilwork", "In Flames",
         "Tranquility", "Opeth", "Be'lakor", "Ensiferum", "Eluveitie"]

family_town = ["X-14D3", "Rootish", "Murksorrow", "Lunthiel", "Tram",
               "Ulthane", "Tasarm", "Riverfellow", "Ruutag", "Fulton",
               "Bottlebuster", "Strongnet", "Thundercave", "Vale",
               "Von Dongen", "Fischer", "Peters", "Smith" "Weaver",
               "Hart", "Parker", "Tanith", "Balhaut", "Sloka", "Vitria",
               "Blackshard", "Monthax", "Hyrka", "Voltemand", "Ketzok",
               "Volpone", "Ramilies", "Slamabadden", "Roane", "Voltis",
               "Kaylen", "Trynai", "Fadayhin", "Verghast", "Cociaminus",
               "Animus", "Grimoyr", "Narmenia", "Hagia", "Urdesh",
               "Gigar", "Aondrift", "Novaanaximander", "Aximander",
               "Mirridon", "Tanzia", "Ariadne", "Rydol", "Phantine",
               "Veyveyr", "Heritor", "Banefail", "Commodus",
               "Sol Invictus", "Invictus", "The Eternal", "Engram",
               "Garsedd", "Nilt", "Shis'urna", "Revall", "Trivall",
               "Trefall", "Alefir", "Hrafsir", "Erilar", "Hridmogir",
               "Thrymjaris", "Savitar", "Savotaur"]

misc_m = ["Fukumaru", "Maron", "Bruiser", "Lucky", "Pookoo", "Abaddon",
          "Torgaddon", "Loken", "Aximand", "Cayde", "Halo", "Bender",
          "Fry", "Zoidberg", "Hermes", "Chikatilo", "Chicken Joe",
          "Pootie", "Juju", "Bojangles",
          "Michael McDonald", "Angelo", "Alexander",
          "Alessandro", "Garrick", "Saladin", "Samael", "Raum",
          "Rand", "Matrim", "Tesh", "Archer", "Cyril", "Sterling",
          "Krieger", "Jager", "Ricky Astley", "Marcus", "Phoenix",
          "Fenix", "Dominic", "Gotrek", "Felix", "Baldur", "Aldebert",
          "Ozymandias", "Arsenal", "Arrow", "Lunthiel", "Ulthane",
          "Cygnus", "Vermillion", "Mage", "Source", "Tribe", "Cadmus",
          "Geist", "Gestalt", "Ron Van Dongen", "Stanley Fischer",
          "Tom Peters", "Adam Smith", "Harold H. Hart",
          "Robert M. Parker Jr.", "Deus", "Grimoire",
          "Heritor Asphodel", "Asphodel", "Rygnar", "Rampshel",
          "Esarhaddon", "Commodus Voke", "Voke", "Ishabel Roban",
          "Ishabel", "Roban", "Phant mastik", "Ezra", "Hyuse", "Askept",
          "Calderon", "Estrapabo", "Eskvar", "Issainu", "Vahnitr",
          "Mullenkedheim", "resis", "Issaid"]

misc_f = ["Luna", "Momiji", "Teru", "Maron", "Lin", "Pookie", "Ely",
          "Ying Tze", "Akari", "Juyeon", "Viviana", "Vivian",
          "Absidy", "Miri", "Leela", "Raven", "Egwene", "Moiraine",
          "Lana", "Pam", "Cheryl", "Carol", "Malorie", "Mana",
          "Phoenix", "Miyabi", "Vivi", "Biancha", "Beatrix", "Cynthia",
          "Kaylen", "Rosie"]

barelyhare_m = ["Lydan", "Syrin", "Ptorik", "Joz", "Varog", "Gethrod",
                "Hezra", "Feron", "Ophni", "Colborn", "Fintis",
                "Gatlin", "Jinto", "Hagalbar", "Krinn", "Lenox",
                "Revvyn", "Hodus", "Dimian", "Paskel", "Kontas",
                "Weston", "Azamarr", "Jather", "Tekren", "Jareth",
                "Adon", "Zaden", "Eune", "Graff", "Tez", "Jessop",
                "Gunnar", "Pike", "Domnhar", "Baske", "Jerrick",
                "Mavrek", "Riordan", "Wulfe", "Straus", "Tyvrik",
                "Henndar", "Favroe", "Whit", "Jaris", "Renham",
                "Kagran", "Lassrin", "Vadim", "Arlo", "Quintis", "Vale",
                "Caelan", "Yorjan", "Khron", "Ishmael", "Jakrin",
                "Fangar", "Roux", "Baxar", "Hawke", "Gatlen", "Barak",
                "Nazim", "Kadric", "Paquin", "Kent", "Moki", "Rankar",
                "Lothe", "Ryven", "Clawsen", "Pakker", "Embre",
                "Cassian", "Verssek", "Dagfinn", "Ebraheim", "Nesso",
                "Eldermar", "Rivik", "Rourke", "Barton", "Hemm",
                "Sarkin", "Blaiz", "Talon", "Agro", "Zagaroth",
                "Turrek", "Esdel", "Lustros", "Zenner", "Baashar",
                "Dagrod", "Gentar", "Feston"]

barelyhare_f = ["Syrana", "Resha", "Varin", "Wren", "Yuni", "Talis",
                "Kessa", "Magaltie", "Aeris", "Desmina", "Krynna",
                "Asralyn", "Herra", "Pret", "Kory", "Afia", "Tessel",
                "Rhiannon", "Zara", "Jesi", "Belen", "Rei", "Ciscra",
                "Temy", "Renalee", "Estyn", "Maarika", "Lynorr", "Tiv",
                "Annihya", "Semet", "Tamrin", "Antia", "Reslyn",
                "Basak", "Vixra", "Pekka", "Xavia", "Beatha", "Yarri",
                "Liris", "Sonali", "Razra", "Soko", "Maeve", "Everen",
                "Yelina", "Morwena", "Hagar", "Palra", "Elysa", "Sage",
                "Ketra", "Lynx", "Agama", "Thesra", "Tezani", "Ralia",
                "Esmee", "Heron", "Naima", "Rydna", "Sparrow",
                "Baakshi", "Ibera", "Phlox", "Dessa", "Braithe",
                "Taewen", "Larke", "Silene", "Phressa", "Esther",
                "Anika", "Rasy", "Harper", "Indie", "Vita", "Drusila",
                "Minha", "Surane", "Lassona", "Merula", "Kye", "Jonna",
                "Lyla", "Zet", "Orett", "Naphtalia", "Turi", "Rhays",
                "Shike", "Hartie", "Beela", "Leska", "Vemery", "Lunex",
                "Fidess", "Tisette", "Partha"]

disgaea_f = ["Adieu", "Agora", "Ahya", "Aisha", "Alllietta", "Alice",
             "Amia", "Amnelis", "Alumina", "Alquen", "Allocen", "Amy",
             "Amulet", "Anabell", "Anastasia", "Anita", "Anna",
             "Annerose", "Annis", "Angeline", "Aphrodite", "Aria",
             "Ariel", "Arina", "Athena", "Aura", "Aurelia", "Auslese",
             "Baghi", "Barbara", "Beatrice", "Beauchette", "Becky",
             "Bellatrix", "Belle", "Betty", "Bianca", "Bonita",
             "Boo", "Bouquet", "Brenda", "Brigit", "Buelle", "Cameron",
             "Carol", "Carrie", "Cathy", "Cecila", "Charlotte",
             "Chiangley", "Chicori", "Celcia", "Christine", "Ciel",
             "Cinderella", "Claris", "Clarion", "Codeine", "",
             "Connie", "Coral", "Coronet", "Couturiere", "Crescentia",
             "Cynthia", "Daphne", "Delia", "Diana", "Dora", "Dandelion",
             "Eclair", "Ecole", "Eida", "Elaine", "Eleanor", "Elena",
             "Elfir", "Elisa", "Elise", "Elizabeth", "Elphin", "Elsa",
             "Ema", "Emma", "Emmy", "Empress", "Erica", "Esmerelda",
             "Estel", "Ethel", "Eve", "Exocet", "Fabrizia", "Faith",
             "Falfie", "Falquenne", "Fatima", "Faustina", "Fay",
             "Felicia", "Fenella", "Ferri", "Fiona","Fleur", "Flora",
             "Florence", "Francine", "Freda", "Frederica", "Freya",
             "Fubuki", "Garnet", "Gawein", "Gillian", "Ginger",
             "Gloria", "Goldie", "Grace", "Grammy", "Grune",
             "Harlequin", "Hannah", "Hazuki", "Helen", "Hermina",
             "Idea", "Idola", "Ilumina", "Ingrid", "Ippril", "Iris",
             "Irma", "Isabel", "Ishtar", "Isolde", "Hilde", "Jaccard",
             "Jane", "Jasmine", "Jeanne", "Jessica", "Jill", "Joanna",
             "Joclyn", "Judith", "Julie", "Julienne", "Julietta",
             "Justice", "Kanna", "Karen", "Karin", "Karla", "Karrey",
             "Kary", "Kasumi", "Kate", "Katerine", "Katrina", "Kit",
             "Klara", "Klimina", "Komugi", "Kosmos", "Kriemhild",
             "Kyrielich", "Laelia", "Lafeene", "Lana", "Lancia",
             "Laura", "Lauren", "Laverna", "Leia", "Lena", "Leticia",
             "Liberty", "Liese", "Ligia", "Lily", "Linda", "Lisa",
             "Lita", "Lorelei", "Love", "Lucille", "Lucretia", "Luna",
             "Lunista", "Luphina", "Lynn", "Madonna", "Magdalena",
             "Magenta", "Maggie", "Maggiore", "Magnolia", "Margarita",
             "Mariah", "Marin", "Marissa", "Mary", "Matilda", "May",
             "Maya", "Medea", "Meena", "Megan", "Melissa", "Melody",
             "Menuette", "Memory", "Mercia", "Merium", "Merle", "Meryl",
             "Michelle", "Minerva", "Ming-Sia", "Mint", "Moira",
             "Mirage", "Nadia", "Natalie", "Nebula", "Nirva", "Noelle",
             "Noin", "Noir", "Non", "Nyah", "Octavia", "Odessia",
             "Olga", "Olive", "Olympia", "Oracle", "Orivea", "Pamela",
             "Pamille", "Penelope", "Perfume", "Petite", "Phyllis",
             "Pia", "Pierina", "Poette", "Polly", "Pollyanna",
             "Pratima", "Primula", "Pris", "Pritny", "Pucelle", "Quess",
             "Quinine", "Rachel", "Raelene", "Rana", "Ram", "Rem",
             "Rena", "Rhea", "Ripley", "Robin", "Robyn", "Rocielle",
             "Ronica", "Rose", "Rosetta", "Rouge", "Roxanne",
             "Rubashka", "Sabrina", "Sabrosa", "Sakura", "Salvia",
             "Sarafan", "Sarah", "Saratoga", "Saria", "Sarome", "Sasha",
             "Scarlet", "Schia", "Seila", "Selene", "Sepia", "Sharon",
             "Shelby", "Sherry", "Sialon", "Sibyl", "Silica", "Silver",
             "Silvia", "Siren", "Soleil", "Solis", "Sonata", "Sonette",
             "Sophia", "Strawberry", "Sunday", "Suzanna", "Suzie",
             "Suzu", "Svana", "Sweet", "Tamarin", "Tamia", "Tanya",
             "Teresa", "Terrine", "Tesse", "Tiffany", "Tigre", "Tina",
             "Tranza", "Trianna", "Trinity", "Undine", "Vanessa",
             "Vediva", "Venus", "Vera", "Vicky", "Victoria", "Vilma",
             "Vine", "Violette", "Wendy", "Windy", "Winney", "Xandria",
             "Yanyan", "Yuki", "Yvette", "Yvonne", "Zenia", "Ziska"]

disgaea_m = ["Abigor", "Ace", "Achilles", "Acid", "Adrian", "Aegis",
             "Agaliarept", "Agares", "Agrippa", "Ajikage", "Akey",
             "Akiblo", "Akira", "Al", "Alan", "Albert", "Aldis", "Alex",
             "Alexander", "Alfred", "Algoreo", "Allen", "Alpha", "Alsace",
             "Alto", "Alucard", "Amdusias", "Amon", "Andras", "Andre",
             "Andrealphus", "Andrew", "Andromalius", "Animus", "Ansbach",
             "Antaios", "Antonio", "Apollo", "Appleton", "Aqua", "Aragorn",
             "Arbaux", "Archie", "Arias", "Arion", "Ark", "Armaros",
             "Artemis", "Arthur", "Asbestos", "Ash", "Astarte",
             "Athetosis", "Athos", "August", "Avan", "Axis", "Azazel",
             "Baggins", "Bakala", "Balalaika", "Baldr", "Baldwin", "Balin",
             "Ballad", "Baltis", "Barak", "Barsom", "Beaufort", "Belinus",
             "Belphegor", "Benten", "Beowulf", "Bereth", "Bertrand",
             "Bifrons", "Billy", "Birru", "Bismarck", "Blair", "Bob",
             "Bonaparte", "Boss", "Bossanova", "Bravo", "Brocken", "Bruce",
             "Byung", "Cadmus", "Cagliostro", "Cameo", "Cameron", "Canard",
             "Caradoc", "Carbide", "Carl", "Carlos", "Carlton",
             "Carmalide", "Caulang", "Cecil", "Chapeau", "Charles",
             "Charmant", "Chen", "Chlordane", "Choux", "Christoph",
             "Chuck", "Cinzano", "Clefford", "Clipton", "Clive", "Cloak",
             "Clove", "Clown", "Clutch", "Cognac", "Comet", "Cornerius",
             "Cornet", "Corriedale", "Corsage", "Cotton", "Croissant",
             "Crouton", "Cymbal", "Damian", "Dan", "Dandy", "Darby",
             "Debonair", "Delta", "Devon", "Dietrich", "Dilan", "Djinn",
             "Dog", "Dogma", "Dolce", "Domitus", "Don Juan", "Donnie",
             "Dorro", "Douglas", "Drew", "Dschingis", "Duke", "Dustin",
             "Dynamo", "Ebonite", "Ed", "Edgar", "Eigendorf", "Eiji",
             "Eisbein", "Eisenach", "Eisenerz", "Elfriede", "Eligor",
             "Elsheimer", "Emilio", "Engarde", "Enigma", "Epsilon",
             "Erg", "Ernst", "Escargo", "Esparanto", "Esprit", "Ethos",
             "Etranger", "Etwas", "Falco", "Falus", "Faust", "Faustus",
             "Fei-Hung", "Ferne", "Fiador", "Fixer", "Flauros", "Flea",
             "Fondue", "Foon", "Frank", "Friedrich", "Fuke", "Fyz",
             "Gabbot", "Gainer", "Gair", "Gairu", "Galaxy", "Gallant",
             "Gambit", "Gandalf", "Gansel", "Garcon", "Gareth", "Garon",
             "Garosh", "Gash", "Gaston", "Gaufres", "Gaws", "Gazette",
             "Geese", "Geist", "Gemeiner", "General", "George",
             "Geraint", "Geralt", "Gerhard", "Geronimo", "Gesellschaft",
             "Gestalt", "Gewalt", "Giko", "Gimlet", "Gin", "Gingham",
             "Gnocchi", "Goblet", "Goemon", "Gray", "Great", "Gremory",
             "Griffon", "Guenever", "Gustav", "Guy", "Haken", "Halver",
             "Hanzo", "Harrison", "Harry", "Hartwin", "Haydn", "Hector",
             "Hedwig", "Heinrich", "Heinz", "Hellicios", "Hickory",
             "Homeros", "Horchata", "Hrothgar", "Hulloc", "Hun", "Husky",
             "Ipos", "Ivan", "Jack", "Jackal", "Jam", "James", "Jarble",
             "Jet", "Jeyal", "Jim", "Joe", "Johann", "Johanson", "John",
             "Johnson", "Joker", "Jordan", "Jruu", "Jubei", "Judas",
             "Julius", "Kain", "Kaiser", "Kasekuchen", "Kasuba",
             "Keeseling", "Keim", "Keith", "Kennel", "Kessler", "Khmer",
             "Kinkan", "Kiwi", "Klomn", "Kocher", "Konga", "Krajicek",
             "Kurt", "Kyle", "Lachesis", "Lambda", "Lancelot", "Lao",
             "Lapiz", "Larugo", "Laslo", "Laudigan", "Launceor",
             "Leighton", "Lemon", "Lenn", "Leon", "Limbo", "Lime",
             "Linker", "Lionel", "Logan", "Lone Wolf", "Lowell",
             "Ludwig", "Luke", "Lundi", "Lutius", "Lynn", "Macky",
             "Magnus", "Malcolm", "Malthus", "Mao", "Marchocias",
             "Marco", "Mariell", "Marius", "Mark", "Marl", "Marlone",
             "Mars", "Martin", "Matthias", "Maximillian", "Maximus",
             "Mayden", "Mazurka", "Meimu", "Meindorf", "Melchior",
             "Memory", "Mephisto", "Metiee", "Meyer", "Mihail", "Mike",
             "Milan", "Millia", "Mint", "Mirage", "Misha", "Mocchus",
             "Mocci", "Modero", "Mohawk", "Moloch", "Monar", "Mordred",
             "Morpheus", "Mort", "Mourvin", "Muireann", "Musashi",
             "Mustafa", "Muzari", "Myrddin", "Napoleon", "Neidhardt",
             "Neige", "Neirin", "Nel", "Nero", "Nessler", "Nicholas",
             "Nitro", "Noir", "Oath", "Oce", "Octavius", "Oidepus",
             "Olias", "Olivier", "Omega", "Orson", "Oscar", "Otto",
             "Ouzo", "Ozmyere", "Palmiro", "Pancho", "Pastel", "Patrick",
             "Paulman", "Peetan", "Percival", "Perrin", "Peter",
             "Phobos", "Phoenix", "Pizzicato", "Pock", "Praxis",
             "Quilt","Qwerty", "Ralph", "Ran", "Rangue", "Rastel", "Ray",
             "Rayrord", "Razz", "Reckendorf", "Red", "Remiel", "Remy",
             "Rhett", "Riali", "Ribbon", "Ricardo", "Rich", "Richard",
             "Robert", "Robinson", "Rockwell", "Roderick", "Roger",
             "Rolan", "Romeo", "Rosewood", "Ruger", "Russell", "Ryan",
             "Saladin", "Salmun", "Salsburg", "Samchay", "Samson",
             "Samuel", "Sasuke", "Savarin", "Scherzo", "Scotch",
             "Sebastian", "Sector", "Seimei", "Seito", "Shade", "Shadow",
             "Shamrock", "Sherbert", "Shidoshi", "Shredder", "Si",
             "Sigma", "Sigurd", "Siniud", "Sirius", "Skald", "Skinner",
             "Sludge", "Snob", "Solaris", "Soliton", "Sombart", "Sonic",
             "Souffle", "Spade", "Spartan", "Spiral", "Staden", "Star",
             "Steilhang", "Stigma", "Stinger", "Stout", "Sushi",
             "Tamiel", "Tandoori", "Tanpopo", "Tao", "Tarte", "Theo",
             "Theta", "Thomas", "Tinker", "Titan", "Torquay", "Tristan",
             "Tristram", "Turbo", "Ulrich", "Uranus", "Uriel", "Va",
             "Valencia", "Valerius", "Valgus", "Vasquez",
             "Vega", "Veritace", "Verne", "Verrier", "Vladimir", "Vodka",
             "Volac", "Waffle", "Walter", "Warren", "Wasabi", "Werner",
             "Wesker", "Wilhelm", "Willaby", "William", "Willock",
             "Wing", "Wolf", "X-14D3", "Xabia", "Xe", "Xenon", "Xig",
             "Ygerne", "York", "Z", "Zanac", "Zebra", "Zeeman", "Zeke",
             "Zeolite", "Zero", "Zeus", "Zeveck", "Zisakuzien", "Zodiac"]

male_name.extend(characters_m)
male_name.extend(misc_m)
male_name.extend(barelyhare_m)
male_name.extend(disgaea_m)
male_name.extend(kpop_m)

female_name.extend(character_f)
female_name.extend(misc_m)
female_name.extend(barelyhare_f)
female_name.extend(disgaea_f)
female_name.extend(jpop)
female_name.extend(kpop_f)

misc_name.extend(bands)
misc_name.extend(family_town)

def removeDuplicates_m(name_list):
    uniqueList = []
    for elem in name_list:
        if elem not in uniqueList:
            uniqueList.append(elem)
    return uniqueList

male_unique = removeDuplicates_m(male_name)

female_unique = removeDuplicates_m(female_name)

other_unique = removeDuplicates_m(misc_name)

prompt = "Choose: Male(m), Female(f), or Other(o): " \
         "\nPress quit(q) to quit, or help(h) for help, at any time."

while True:
    choice = input(prompt)

    if choice.lower() == "quit" or choice.lower() == "q":
        break
    elif choice.lower() == "male" or choice.lower() == "m":
        print(random.choice(male_unique))
        continue
    elif choice.lower() == "female" or choice.lower() == "f":
        print(random.choice(female_unique))
        continue
    elif choice.lower() == "miscellaneous" or choice.lower() == "o" or choice.lower() == "misc" or choice.lower() == "other":
        print(random.choice(other_unique))
        continue
    elif choice.lower() == "help" or choice.lower() == "h":
        print("Typing 'male' or 'm' generates a male name"
              "\nTyping 'female' or 'f' generates a female name"
              "\nTyping 'other' or 'o' generates a miscellaneous name"
              "\nMiscellaneous names work better as family names, or the names of places")
        continue
    else:
        print("Invalid input, please try again")
