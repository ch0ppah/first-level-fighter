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
class TestGenerate(unittest.TestCase):
    def test_generate(self):
        with open('content/names.csv') as file:
            names = list(map(lambda line: line.strip().split(','), file))
        with open('content/abilities.csv') as file:
            classes = list(map(lambda line: line.strip().split(',')[0], file))
        with open('content/equipment.csv') as file:
            equipment_list = list(map(lambda line: line.strip().split(','), file))
        
        for _ in range(10):
            species, name, stats, stat_mods, chosen_class, abilities, equipment = generate()
            self.assertIn(species, names, f"{species} is not a species in names.csv")
            self.assertIn(name, names, f"{name} is not a name in names.csv")
            for stat in stats:
                self.assertGreaterEqual(stat, 3, f"Rolled stat ({stat}) is not greater than or equal to 3")
                self.assertLessEqual(stat, 18, f"Rolled stat ({stat}) is not less than or equal to 18")
            for stat_mod in stat_mods:
                self.assertGreaterEqual(stat_mod, -4, f"Rolled stat ({stat_mod}) is not greater than or equal to -4")
                self.assertLessEqual(stat_mod, 4, f"Rolled stat ({stat_mod}) is not less than or equal to 4")
            self.assertIn(chosen_class, classes, f"{chosen_class} is not in abilities.csv")
            self.assertIn(abilities, classes, f"Error pulling abilities for the {chosen_class} class")
            self.assertIn(equipment, equipment_list, f"Error pulling equipment for the {chosen_class} class")