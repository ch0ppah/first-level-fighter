import unittest
from generate import (
    generate,
    roll_stat
)

class TestGenerate(unittest.TestCase):
    def test_generate(self):
        with open('content/names.csv', encoding='utf-8-sig') as file:
            names = list(map(lambda line: line.strip().split(','), file))
        with open('content/abilities.csv', encoding='utf-8-sig') as file:
            classes = list(map(lambda line: line.strip().split(','), file))
        with open('content/equipment.csv', encoding='utf-8-sig') as file:
            equipment_list = list(map(lambda line: line.strip().split(','), file))
        with open('content/species_bonuses.csv', encoding='utf-8-sig') as file:
            species_bonuses = list(map(lambda line: line.strip().split(','), file))
        
        alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
        species, name, alignment, stats, stat_mods, chosen_class, class_abilities, species_abilities, equipment = generate()
        self.assertIn(alignment, alignments, f"{alignment} is not a valid alignment")
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
        self.assertEqual(class_abilities, abilities_row, f"Error pulling abilities for the {chosen_class} class")
        species_abilities_row = next(row for row in species_bonuses if row[0] == species)[1:]
        self.assertEqual(species_abilities, species_abilities_row, f"Error pulling species abilities for the {species} species")
        equipment_row = next(row for row in equipment_list if row[0] == chosen_class)[1:]
        self.assertEqual(equipment, equipment_row, f"Error pulling equipment for the {chosen_class} class")



    def test_roll_stats(self):
        for i in range(100):
            stat = roll_stat()
            self.assertGreaterEqual(stat, 3, f"Rolled stat ({stat}) is not greater than or equal to 3")
            self.assertLessEqual(stat, 18, f"Rolled stat ({stat}) is not less than or equal to 18")
            i += 1