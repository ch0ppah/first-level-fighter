import random
from sys import exit

def generate():
    STR, DEX, CON, INT, WIS, CHA = 0, 1, 2, 3, 4, 5
    species, name = generate_name()
    stats = generate_stats()
    classes_list = show_classes()
    chosen_class = pick_class(classes_list)
    abilities = get_abilities(chosen_class)
    equipment = get_equipment(chosen_class)
    prompt_for_asi()
    allocate_asi(stats)
    stat_mods = [statmod(stats[STR]),
                 statmod(stats[DEX]),
                 statmod(stats[CON]),
                 statmod(stats[INT]),
                 statmod(stats[WIS]),
                 statmod(stats[CHA])]
    
    return [species, name, stats, stat_mods, chosen_class, abilities, equipment]

def generate_name():
    with open('../content/names.csv') as file:
        names = list(map(lambda line: line.strip().split(','), file))
    
    num_species = len(names[0]) - 1
    num_names = len(names[0][0]) - 1
    species_index = random.randrange(0, num_species)
    name_index = random.randrange(1,num_names)

    species = names[species_index]
    name = names[species_index][name_index]

    print(f"You are {name}, the {species}.")
    print()
    return species, name

def generate_stats():
    stats = [roll_stat(), roll_stat(), roll_stat(), roll_stat(), roll_stat(), roll_stat()]
    STR, DEX, CON, INT, WIS, CHA = stats[0], stats[1], stats[2], stats[3], stats[4], stats[5]

    print("You rolled the following stats:")
    print(f"Strength     (STR): {STR}")
    print(f"Dexterity    (DEX): {DEX}")
    print(f"Constitution (CON): {CON}")
    print(f"Intelligence (INT): {INT}")
    print(f"Wisdom       (WIS): {WIS}")
    print(f"Charisma     (CHA): {CHA}")
    print()
    return stats

def roll_stat():
    lowest_roll, highest_roll = 1, 6
    die_1 = random.randrange(lowest_roll, highest_roll)
    die_2 = random.randrange(lowest_roll, highest_roll)
    die_3 = random.randrange(lowest_roll, highest_roll)
    die_4 = random.randrange(lowest_roll, highest_roll)

    # Puts all die rolls into a list
    top_3_dice = sorted([die_1, die_2, die_3, die_4])[1:]

    return top_3_dice[1] + top_3_dice[2] + top_3_dice[3]

def statmod(stat):
    return (stat - 10) // 2

def get_equipment(chosen_class):
    with open('../content/equipment.csv') as file:
        equipment = list(map(lambda line: line.strip().split(','), file))
    
    return next((row for row in equipment if row[0].startswith(chosen_class)), None)[1:]

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

def get_abilities(chosen_class):
    with open('../content/abilities.csv') as file:
        abilities = list(map(lambda line: line.strip().split(','), file))

    return next((row for row in abilities if row[0].startswith(chosen_class)), None)[1:]

def show_classes():
    with open('../content/abilities.csv') as file:
        classes = list(map(lambda line: line.strip().split(',')[0], file))
    print("Here are the classes you can select:")
    for clas in classes:
        print(f"{clas}")

    return classes

# Might be the most dogshit part of this project
# If anyone sees this function and wants to share a better way to accomplish this please let me know
def allocate_asi(stats):
    STR, DEX, CON, INT, WIS, CHA = 0, 1, 2, 3, 4, 5
    asi = input()
    if asi == 'QUIT':
        print("First Level Fighter terminated")
        exit()
    asi = asi.split()
    if len(asi) == 2:
        match asi[0].upper():
            case "STR":
                stats[STR] += 2
            case "DEX":
                stats[DEX] += 2
            case "CON":
                stats[CON] += 2
            case "INT":
                stats[INT] += 2
            case "WIS":
                stats[WIS] += 2
            case "CHA":
                stats[CHA] += 2
            case _:
                raise ValueError(f"invalid value given: {asi[0]} is not valid stat name")
            
        match asi[1].upper():
            case "STR":
                stats[STR] += 1
            case "DEX":
                stats[DEX] += 1
            case "CON":
                stats[CON] += 1
            case "INT":
                stats[INT] += 1
            case "WIS":
                stats[WIS] += 1
            case "CHA":
                stats[CHA] += 1
            case _:
                raise ValueError(f"invalid value given: {asi[1]} is not valid stat name")
            
    elif len(asi) == 3:
        match asi[0].upper():
            case "STR":
                stats[STR] += 1
            case "DEX":
                stats[DEX] += 1
            case "CON":
                stats[CON] += 1
            case "INT":
                stats[INT] += 1
            case "WIS":
                stats[WIS] += 1
            case "CHA":
                stats[CHA] += 1
            case _:
                raise ValueError(f"invalid value given: {asi[0]} is not valid stat name")
            
        match asi[1].upper():
            case "STR":
                stats[STR] += 1
            case "DEX":
                stats[DEX] += 1
            case "CON":
                stats[CON] += 1
            case "INT":
                stats[INT] += 1
            case "WIS":
                stats[WIS] += 1
            case "CHA":
                stats[CHA] += 1
            case _:
                raise ValueError(f"invalid value given: {asi[1]} is not valid stat name")
            
        match asi[2].upper():
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
    return stats

def prompt_for_asi():
    print("Choose which ability scores to increase.")
    print("Typing a pair of abbreviated stat names ('STR DEX', for example) will grant +2 to the first stat and +1 to the second.")
    print("Alternatively, typing three abbreviated stat names ('STR DEX CON', for example) will instead grant +1 to each.")