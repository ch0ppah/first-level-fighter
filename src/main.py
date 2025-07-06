import readchar
from readchar import key
from generate import generate


# 0: typing "QUIT" at any point will exit the program. All other input is case-insensitive.
# 1: Roll random numbers to generate stats and species
# -: If the numbers are too low, reroll quietly.
# 2: Present the stat spread to the user. If they want to reroll, type 'reroll' (case unsensitive). Otherwise, type the name of the class to use.
# - Invalid inputs should reprompt the user
# - Present the user with a list of valid class names to choose
# 3: Use the given class to get abilities and starting equipment list
# 4: Prompt the user for where to put their +2/+1 or +1/+1/+1 bonuses
# - 'STR DEX' allocates +2 to STR and +1 to DEX, 'DEX STR' allocates +2 to DEX and +1 to STR)
# = Listing any 3 attributes should instead apply +1 to each. Attempting to input <2 or 3> attributes reprompts the user.
# 5: Use final stat spread to generate mod scores for sheet
# 6: ??? Am i missing something
# 7: Read in template doc, replace all tokens with corresponding values
# 8: Save completed md file onto user's computer
# 9: Prompt to begin process again or exit program

def main():
    greet()
    while True:
        k = readchar.readkey()
        if k == key.ENTER:
            generate()


def greet():
    print("Welcome to First Level Fighter (FLF)!")
    print()
    print("Press ENTER to generate a first level character sheet for DND 5E(2014)")

if __name__ == "__main__":
    main()