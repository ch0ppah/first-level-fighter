import os
from generate import generate
from write_sheet import write_sheet

def main():
    print("--- FIRST LEVEL FIGHTER ---")
    print("Type 'QUIT' to quit the program at any time.")
    print()
    character = generate()
    character_sheet = write_sheet(character)
    name = character[1]
    save_sheet(character_sheet, name)

def save_sheet(sheet, name):
    directory = "flf_sheets"
    if not os.path.exists(directory):
        os.makedirs(directory)

    sanitized_name = name.replace(' ', '_').replace('/', '_')
    filename = f"{sanitized_name}_character_sheet.md"

    full_path = os.path.join(directory, filename)
    absolute_path = os.path.abspath(full_path)

    with open(full_path, 'w') as file:
        for line in sheet:
            file.write(line + '\n')

    print (f"Character sheet saved to {absolute_path}")
    return absolute_path
if __name__ == "__main__":
    main()