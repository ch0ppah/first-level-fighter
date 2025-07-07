import random
from sys import exit

# 1: Read from the template file
# 2: Replace each [token] spot with the corresponding info from user input
# 3: Save the file to a location on the PC, probably the documents folder?

#Things needed to generate:
# Stat spread, species, name
# spread is independent, name is species dependent

def generate():
    # This should read the files into a 2D-arrays that I can then index using
    # pseudo-random numbers
    species, name = generate_name()
    stats = generate_stats()
    classes = show_classes()
    chosen_class = pick_class(classes)
    equipment = get_equipment(chosen_class)
    prompt_for_asi()
    allocate_asi(stats)

# Generates a species and name to use
# returns both in a tuple
def generate_name():
    with open('../content/names.csv') as file:
        names = list(map(lambda line: line.strip().split(','), file))

    # Rolls number for species
    species_index = random.randrange(0, 8)
    # Rolls number for name
    name_index = random.randrange(1,11)

    species = names[species_index]
    name = names[species_index][name_index]

    print(f"You are {name}, the {species}.")
    print()
    return species, name

# roll stats using '4d6 drop lowest', store results in order as a list
# returns a list of integers
def generate_stats():
    stats = [roll_stat(), roll_stat(), roll_stat(), roll_stat(), roll_stat(), roll_stat()]
    strr, dex, con, intt, wis, cha = stats[0], stats[1], stats[2], stats[3], stats[4], stats[5]

    print(f"You rolled the following stats:")
    print(f"Strength     (STR): {strr}")
    print(f"Dexterity    (DEX): {dex}")
    print(f"Constitution (CON): {con}")
    print(f"Intelligence (INT): {intt}")
    print(f"Wisdom       (WIS): {wis}")
    print(f"Charisma     (CHA): {cha}")
    print()
    return stats

# helper function to 'roll' for a stat
def roll_stat():
    die_1 = random.randrange(1, 6)
    die_2 = random.randrange(1, 6)
    die_3 = random.randrange(1, 6)
    die_4 = random.randrange(1, 6)

    # Puts all die rolls into a list
    dice = [die_1, die_2, die_3, die_4]
    # Sorts list, placing lowest roll in the first index
    dice = sorted(dice)
    # Slices the lowest (first index) roll out of the list, 'dropping' it
    dice = dice[1:]
    return dice[1] + dice[2] + dice[3]

# Helper function for calculating stat modifiers
# takes a stat (int) and returns its mod (string
def statmod(stat):
    return (stat - 10) // 2

# create list of class equipment to fill sheet with
# returns class-relevant equipment in a list
def get_equipment(chosen_class):
    with open('../content/equipment.csv') as file:
        equipment = list(map(lambda line: line.strip().split(','), file))
    
    return next((row for row in equipment if row[0].startswith(chosen_class)), None)[1:]

# poll user for what class to use
# Inform user of what the valid classes are
# If an invalid string is given, inform user of mistake and poll again
# returns a string
def pick_class(classes):
    chosen_class = input("Please select a class by typing in the class you would like to use for your stat spread.")
    if chosen_class == 'QUIT':
        print("First Level Fighter terminated")
        exit()
    elif chosen_class.lower().capitalize in classes:
        return chosen_class
    else:
        print("Invalid class")
        pick_class()

def show_classes():
    with open('../content/abilities.csv') as file:
        classes = list(map(lambda line: line.strip().split(',')[0], file))
    print("Here are the classes you can select:")
    for clas in classes:
        print(f"{clas}")

    return classes

# Prompts user for what stats they would like to boost
# input should be formatted like 'str dex', first stat gets +2, second gets +1.
# alternatively can give three stats for +1 in each.
# stats is a list of the current stat spread
def allocate_asi(stats):
    asi = input()
    if asi == 'QUIT':
        exit()
    asi = asi.split()
    if len(asi) == 2:
        match asi[0].lower():
            case "str":
                stats[0] += 2
            case "dex":
                stats[1] += 2
            case "con":
                stats[2] += 2
            case "int":
                stats[3] += 2
            case "wis":
                stats[4] += 2
            case "cha":
                stats[5] += 2
            case _:
                raise ValueError(f"invalid value given: {asi[0]} is not valid stat name")
            
        match asi[1].lower():
            case "str":
                stats[0] += 1
            case "dex":
                stats[1] += 1
            case "con":
                stats[2] += 1
            case "int":
                stats[3] += 1
            case "wis":
                stats[4] += 1
            case "cha":
                stats[5] += 1
            case _:
                raise ValueError(f"invalid value given: {asi[1]} is not valid stat name")
            
    elif len(asi) == 3:
        match asi[0].lower():
            case "str":
                stats[0] += 1
            case "dex":
                stats[1] += 1
            case "con":
                stats[2] += 1
            case "int":
                stats[3] += 1
            case "wis":
                stats[4] += 1
            case "cha":
                stats[5] += 1
            case _:
                raise ValueError(f"invalid value given: {asi[0]} is not valid stat name")
            
        match asi[1].lower():
            case "str":
                stats[0] += 1
            case "dex":
                stats[1] += 1
            case "con":
                stats[2] += 1
            case "int":
                stats[3] += 1
            case "wis":
                stats[4] += 1
            case "cha":
                stats[5] += 1
            case _:
                raise ValueError(f"invalid value given: {asi[1]} is not valid stat name")
            
        match asi[2].lower():
            case "str":
                stats[0] += 1
            case "dex":
                stats[1] += 1
            case "con":
                stats[2] += 1
            case "int":
                stats[3] += 1
            case "wis":
                stats[4] += 1
            case "cha":
                stats[5] += 1
            case _:
                raise ValueError(f"invalid value given: {asi[2]} is not valid stat name")
    else:
        print("Invalid stat names entered")
        allocate_asi(stats)

def prompt_for_asi():
    print("Choose which ability scores to increase.")
    print("Typing a pair of abbreviated stat names ('STR DEX', for example) will grant +2 to the first stat and +1 to the second.")
    print("Alternatively, typing three abbreviated stat names ('STR DEX CON', for example) will instead grant +1 to each.")