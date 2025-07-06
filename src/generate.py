import random

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
    chosen_class = pick_class()
    equipment = get_equipment(chosen_class)

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

    return species, name

# roll stats using '4d6 drop lowest', store results in order as a list
# returns a list of integers
def generate_stats():
    stats = []
    return stats

# create list of class equipment to fill sheet with
# returns 2D-array of class-equipment info
def get_equipment(chosen_class):
    with open('../content/equipment.csv') as file:
        equipment = list(map(lambda line: line.strip().split(','), file))
    
    return next((row for row in equipment if row[0].startswith(chosen_class)), None)

# poll user for what class to use
# Inform user of what the valid classes are
# If an invalid string is given, inform user of mistake and poll again
# returns a string
def pick_class():
    print("Here are the classes you can select:")
    print("Artificer, Barbarian, Bard, Cleric, Druid")
    print("Fighter, Monk, Paladin, Ranger, Rogue")
    print("Sorcerer, Warlock, Wizard")
    chosen_class = input("Please select a class by typing in the class you would like to use for this stat spread.")
    return chosen_class