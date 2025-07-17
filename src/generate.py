import random
from sys import exit
from constants import (
    STR_INDEX, DEX_INDEX, CON_INDEX, INT_INDEX, WIS_INDEX, CHA_INDEX,
    ROLL_LOWER_BOUND, ROLL_HIGHER_BOUND, SPECIES, PLUS_2, PLUS_1,
    REMOVE_CLASS_NAME, REMOVE_SPECIES_NAME, REMOVE_LOWEST_DIE,
    DIE_1_INDEX, DIE_2_INDEX, DIE_3_INDEX, ALIGN_LOWER_BOUND, ALIGN_HIGHER_BOUND
)

def generate():
    species, name, alignment = generate_name()
    stats = generate_stats()
    classes_list = show_classes()
    chosen_class = pick_class(classes_list)
    class_abilities = get_class_abilities(chosen_class)
    species_abilities = get_species_abilities(species)
    equipment = get_equipment(chosen_class)
    prompt_for_asi()
    allocate_asi(stats)
    stat_mods = [statmod(stats[STR_INDEX]),
                 statmod(stats[DEX_INDEX]),
                 statmod(stats[CON_INDEX]),
                 statmod(stats[INT_INDEX]),
                 statmod(stats[WIS_INDEX]),
                 statmod(stats[CHA_INDEX])]
    
    return [species, name,  alignment, stats, stat_mods, chosen_class, class_abilities, species_abilities, equipment]

def generate_name():
    with open('content/names.csv', encoding='utf-8-sig') as file:
        names = list(map(lambda line: line.strip().split(','), file))
    
    num_species = len(names)
    species_index = random.randrange(num_species)
    num_names = len(names[species_index])
    name_index = random.randrange(REMOVE_SPECIES_NAME, num_names)

    species = names[species_index][SPECIES]
    name = names[species_index][name_index]
    alignment = generate_alignment()
    print("------------------------------")
    print(f"You are {name}, the {species}.")
    print(f"Your alignment is {alignment}.")
    print()
    return species, name, alignment

def generate_stats():
    stats = [roll_stat(), roll_stat(), roll_stat(), roll_stat(), roll_stat(), roll_stat()]
    STR_roll, DEX_roll, CON_roll, INT_roll, WIS_roll, CHA_roll = stats[STR_INDEX], stats[DEX_INDEX], stats[CON_INDEX], stats[INT_INDEX], stats[WIS_INDEX], stats[CHA_INDEX]

    print("------------------------------")
    print("You rolled the following stats:")
    print(f"Strength     (STR): {STR_roll}")
    print(f"Dexterity    (DEX): {DEX_roll}")
    print(f"Constitution (CON): {CON_roll}")
    print(f"Intelligence (INT): {INT_roll}")
    print(f"Wisdom       (WIS): {WIS_roll}")
    print(f"Charisma     (CHA): {CHA_roll}")
    print("------------------------------")
    return stats

def generate_alignment():
    alignment = None
    law_v_chaos = ["Lawful", "Neutral", "Chaotic"]
    good_v_evil = ["Good", "Neutral", "Evil"]
    law_v_chaos_lean = law_v_chaos[random.randrange(ALIGN_LOWER_BOUND, ALIGN_HIGHER_BOUND)]
    good_v_evil_lean = good_v_evil[random.randrange(ALIGN_LOWER_BOUND, ALIGN_HIGHER_BOUND)]

    if law_v_chaos_lean == good_v_evil_lean:
        alignment = "True Neutral"
    else:
        alignment = f"{law_v_chaos_lean} {good_v_evil_lean}"
    return alignment

def roll_stat():
    die_1 = random.randrange(ROLL_LOWER_BOUND, ROLL_HIGHER_BOUND)
    die_2 = random.randrange(ROLL_LOWER_BOUND, ROLL_HIGHER_BOUND)
    die_3 = random.randrange(ROLL_LOWER_BOUND, ROLL_HIGHER_BOUND)
    die_4 = random.randrange(ROLL_LOWER_BOUND, ROLL_HIGHER_BOUND)

    top_3_dice = sorted([die_1, die_2, die_3, die_4])[REMOVE_LOWEST_DIE:]
    return top_3_dice[DIE_1_INDEX] + top_3_dice[DIE_2_INDEX] + top_3_dice[DIE_3_INDEX]

def statmod(stat):
    return (stat - 10) // 2

def pick_class(classes):
    chosen_class = input_check_quit("Please type in the class you would like to use with your stat spread: ")
    print()
    if chosen_class.lower().capitalize() in classes:
        return chosen_class.lower().capitalize()
    else:
        print("Invalid class")
        return pick_class(classes)

def get_class_abilities(chosen_class):
    with open('content/abilities.csv', encoding='utf-8-sig') as file:
        abilities = list(map(lambda line: line.strip().split(','), file))

    return next((row for row in abilities if row[0].startswith(chosen_class)), None)[REMOVE_CLASS_NAME:]

def get_equipment(chosen_class):
    with open('content/equipment.csv', encoding='utf-8-sig') as file:
        equipment = list(map(lambda line: line.strip().split(','), file))
    
    return next((row for row in equipment if row[0].startswith(chosen_class)), None)[REMOVE_CLASS_NAME:]

def get_species_abilities(species):
    with open('content/species_bonuses.csv', encoding='utf-8-sig') as file:
        species_abilities = list(map(lambda line: line.strip().split(','), file))

    return next((row for row in species_abilities if row[0].startswith(species)), None)[REMOVE_SPECIES_NAME:]

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
            increment_amount = PLUS_2
            if i == 1:
                increment_amount = PLUS_1
            match asis[i].upper():
                case "STR":
                    stats[STR_INDEX] += increment_amount
                case "DEX":
                    stats[DEX_INDEX] += increment_amount
                case "CON":
                    stats[CON_INDEX] += increment_amount
                case "INT":
                    stats[INT_INDEX] += increment_amount
                case "WIS":
                    stats[WIS_INDEX] += increment_amount
                case "CHA":
                    stats[CHA_INDEX] += increment_amount
                case _:
                    print(f"'{asis[i]}' is not valid stat name LEN 2 CHECK")
                    print('Please enter 2-3 valid stat names (STR, DEX, CON, INT, WIS, CHA)')
                    print()
                    allocate_asi(stats)
        return stats
            
    elif len(asis) == 3:
        increment_amount = PLUS_1
        for stat in asis:
            match stat.upper():
                case "STR":
                    stats[STR_INDEX] += increment_amount
                case "DEX":
                    stats[DEX_INDEX] += increment_amount
                case "CON":
                    stats[CON_INDEX] += increment_amount
                case "INT":
                    stats[INT_INDEX] += increment_amount
                case "WIS":
                    stats[WIS_INDEX] += increment_amount
                case "CHA":
                    stats[CHA_INDEX] += increment_amount
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