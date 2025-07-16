from generate import generate
from write_sheet import write_sheet

def main():
    print("--- FIRST LEVEL FIGHTER ---")
    print("Type 'QUIT' to quit the program at any time.")
    print()
    write_sheet(generate())

if __name__ == "__main__":
    main()