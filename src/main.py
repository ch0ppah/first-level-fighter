from generate import generate
from write_sheet import write_sheet
# 6: ??? Am i missing something
# 7: Read in template doc, replace all tokens with corresponding values
# 8: Save completed md file onto user's computer
# 9: Prompt to begin process again or exit program

# k = readchar.readkey()
# if k == key.ENTER:
def main():
    print("--- FIRST LEVEL FIGHTER ---")
    print("Type 'QUIT' to quit the program at any time.")
    print()
    write_sheet(generate())

if __name__ == "__main__":
    main()