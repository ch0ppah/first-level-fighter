import unittest
from generate import (
    generate,
    generate_name,
    generate_stats,
    roll_stat,
    statmod,
    get_equipment,
    pick_class,
    show_classes,
    allocate_asi,
)

# TODO: RUN THE TESTS!!!!

class TestGenerate(unittest.TestCase):
    def test_generate(self):
        with open('content/names.csv', encoding='utf-8-sig') as file:
            names = list(map(lambda line: line.strip().split(','), file))
        with open('content/abilities.csv', encoding='utf-8-sig') as file:
            classes = list(map(lambda line: line.strip().split(','), file))
        with open('content/equipment.csv', encoding='utf-8-sig') as file:
            equipment_list = list(map(lambda line: line.strip().split(','), file))
        
        for _ in range(1):
            species, name, stats, stat_mods, chosen_class, abilities, equipment = generate()
            self.assertIn(species, [row[0] for row in names], f"{species} is not a species in names.csv")
            species_row = next(row for row in names if row[0] == species)
            self.assertIn(name, species_row[1:], f"{name} is not a valid name for species {species} in names.csv")
            for stat in stats:
                self.assertGreaterEqual(stat, 3, f"Rolled stat ({stat}) is not greater than or equal to 3")
                self.assertLessEqual(stat, 18, f"Rolled stat ({stat}) is not less than or equal to 18")
            for stat_mod in stat_mods:
                self.assertGreaterEqual(stat_mod, -4, f"Rolled stat ({stat_mod}) is not greater than or equal to -4")
                self.assertLessEqual(stat_mod, 4, f"Rolled stat ({stat_mod}) is not less than or equal to 4")
            classes_row = [row[0] for row in classes]
            self.assertIn(chosen_class, classes_row, f"{chosen_class} is not in {classes_row}")
            abilities_row = next(row for row in classes if row[0] == chosen_class)[1:]
            self.assertEqual(abilities, abilities_row, f"Error pulling abilities for the {chosen_class} class")
            equipment_row = next(row for row in equipment_list if row[0] == chosen_class)[1:]
            self.assertEqual(equipment, equipment_row, f"Error pulling equipment for the {chosen_class} class")