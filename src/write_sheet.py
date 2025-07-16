
from constants import (
    STR_INDEX, DEX_INDEX, CON_INDEX, INT_INDEX, WIS_INDEX, CHA_INDEX,
    SPECIES_INDEX, NAME_INDEX, STATS_INDEX, MODS_INDEX, CLASS_INDEX,
    ABILITIES_INDEX, EQUIPMENT_INDEX, HIT_DICE_INDEX, HIT_POINTS_INDEX,
    REMOVE_HP_INFO, ALIGNMENT_INDEX, SPECIES_ABILITIES_INDEX,

)

# TODO: Read in template.md. For each line, check for an @tag, then replace the tag with the correct information. Save the modified template to 'name_sheet_flf.md'.

def write_sheet(character_info):
    species = character_info[SPECIES_INDEX]
    name = character_info[NAME_INDEX]
    alignment = character_info[ALIGNMENT_INDEX]

    str_score = character_info[STATS_INDEX][STR_INDEX]
    dex_score = character_info[STATS_INDEX][DEX_INDEX]
    con_score = character_info[STATS_INDEX][CON_INDEX]
    int_score = character_info[STATS_INDEX][INT_INDEX]
    wis_score = character_info[STATS_INDEX][WIS_INDEX]
    cha_score = character_info[STATS_INDEX][CHA_INDEX]

    str_mod = character_info[MODS_INDEX][STR_INDEX]
    dex_mod = character_info[MODS_INDEX][DEX_INDEX]
    con_mod = character_info[MODS_INDEX][CON_INDEX]
    int_mod = character_info[MODS_INDEX][INT_INDEX]
    wis_mod = character_info[MODS_INDEX][WIS_INDEX]
    cha_mod = character_info[MODS_INDEX][CHA_INDEX]

    chosen_class = character_info[CLASS_INDEX]
    abilities = character_info[ABILITIES_INDEX]
    species_abilities = character_info[SPECIES_ABILITIES_INDEX]
    hit_dice = character_info[EQUIPMENT_INDEX][HIT_DICE_INDEX]
    hit_points = character_info[EQUIPMENT_INDEX][HIT_POINTS_INDEX] + con_mod
    equipment = character_info[EQUIPMENT_INDEX][REMOVE_HP_INFO:]

    passive_perception = 10 + wis_mod