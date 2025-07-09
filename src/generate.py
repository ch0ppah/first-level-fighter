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
    with open('content/names.csv', encoding='utf-8-sig') as file:
        names = list(map(lambda line: line.strip().split(','), file))
    
    num_species = len(names)
    species_index = random.randrange(num_species)
    num_names = len(names[species_index])
    name_index = random.randrange(1, num_names)

    species = names[species_index][0]
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
    lowest_roll, highest_roll = 1, 7
    die_1 = random.randrange(lowest_roll, highest_roll)
    die_2 = random.randrange(lowest_roll, highest_roll)
    die_3 = random.randrange(lowest_roll, highest_roll)
    die_4 = random.randrange(lowest_roll, highest_roll)

    # Puts all die rolls into a list
    top_3_dice = sorted([die_1, die_2, die_3, die_4])[1:]
    # print("-----------DEBUGGING MESSAGES-----------")
    # print(f"top_3_dice[0]: {top_3_dice[0]}")
    # print(f"top_3_dice[1]: {top_3_dice[1]}")
    # print(f"top_3_dice[2]: {top_3_dice[2]}")
    # print(f"TOTAL: {top_3_dice[0] + top_3_dice[1] + top_3_dice[2]}")
    return top_3_dice[0] + top_3_dice[1] + top_3_dice[2]

def statmod(stat):
    return (stat - 10) // 2

def get_equipment(chosen_class):
    with open('content/equipment.csv', encoding='utf-8-sig') as file:
        equipment = list(map(lambda line: line.strip().split(','), file))
    
    return next((row for row in equipment if row[0].startswith(chosen_class)), None)[1:]

def pick_class(classes):
    chosen_class = input_check_quit("Please type in the class you would like to use with your stat spread: ")
    print()
    if chosen_class.lower().capitalize() in classes:
        return chosen_class.lower().capitalize()
    else:
        print("Invalid class")
        return pick_class(classes)

def get_abilities(chosen_class):
    with open('content/abilities.csv', encoding='utf-8-sig') as file:
        abilities = list(map(lambda line: line.strip().split(','), file))

    return next((row for row in abilities if row[0].startswith(chosen_class)), None)[1:]

def show_classes():
    with open('content/abilities.csv', encoding='utf-8-sig') as file:
        classes = list(map(lambda line: line.strip().split(',')[0], file))
    print("Here are the classes you can select:")
    for clas in classes:
        print(f"{clas}")

    return classes

# Might be the most dogshit part of this project
# If anyone sees this function and wants to share a better way to accomplish this please let me know
def allocate_asi(stats):
    STR, DEX, CON, INT, WIS, CHA = 0, 1, 2, 3, 4, 5
    stat_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
    asis = input_check_quit().split()
    
    if len(set(asis)) < 2 or len(set(asis)) > 3:
        print("Improper amount of unique inputs.")
        print("Please enter 2-3 valid stat names (STR, DEX, CON, INT, WIS, CHA)")
        print()
        return allocate_asi(stats)

    for stat in set(asis):
        if stat.upper() not in stat_names:
            print(f"'{stat}' is not a valid stat name SET CHECK")
            print('Please enter 2-3 valid stat names (STR, DEX, CON, INT, WIS, CHA)')
            print()
            return allocate_asi(stats)

    if len(asis) == 2:
        for i in range(2):
            increment_amount = 2
            if i == 1:
                increment_amount = 1
            match asis[i].upper():
                case "STR":
                    stats[STR] += increment_amount
                case "DEX":
                    stats[DEX] += increment_amount
                case "CON":
                    stats[CON] += increment_amount
                case "INT":
                    stats[INT] += increment_amount
                case "WIS":
                    stats[WIS] += increment_amount
                case "CHA":
                    stats[CHA] += increment_amount
                case _:
                    print(f"'{asis[i]}' is not valid stat name LEN 2 CHECK")
                    print('Please enter 2-3 valid stat names (STR, DEX, CON, INT, WIS, CHA)')
                    print()
                    allocate_asi(stats)
        return stats
            
    elif len(asis) == 3:
        increment_amount = 1
        for stat in asis:
            match stat.upper():
                case "STR":
                    stats[STR] += increment_amount
                case "DEX":
                    stats[DEX] += increment_amount
                case "CON":
                    stats[CON] += increment_amount
                case "INT":
                    stats[INT] += increment_amount
                case "WIS":
                    stats[WIS] += increment_amount
                case "CHA":
                    stats[CHA] += increment_amount
                case _:
                    print(f"'{asis}' is not valid stat name LEN 3 CHECK")
                    print('Please enter 2-3 valid stat names (STR, DEX, CON, INT, WIS, CHA)')
                    print()
                    allocate_asi(stats)
    return stats

def prompt_for_asi():
    print("Choose which ability scores to increase.")
    print("Typing a pair of abbreviated stat names ('STR DEX', for example) will grant +2 to the first stat and +1 to the second.")
    print("Alternatively, typing three abbreviated stat names ('STR DEX CON', for example) will instead grant +1 to each.")

def input_check_quit(prompt=""):
    inp = input(prompt)
    if 'QUIT' in inp:
        print("First Level Fighter Terminated")
        print()
        exit()
    else:
        return inp