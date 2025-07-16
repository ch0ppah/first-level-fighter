
from constants import (
    STR_INDEX, DEX_INDEX, CON_INDEX, INT_INDEX, WIS_INDEX, CHA_INDEX,
    SPECIES_INDEX, NAME_INDEX, STATS_INDEX, MODS_INDEX, CLASS_INDEX,
    ABILITIES_INDEX, EQUIPMENT_INDEX, HIT_DICE_INDEX, HIT_POINTS_INDEX,
    REMOVE_HP_INFO

)

def write_sheet(character_info):
    species = character_info[SPECIES_INDEX]
    name = character_info[NAME_INDEX]

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
    hit_dice = character_info[EQUIPMENT_INDEX][HIT_DICE_INDEX]
    hit_points = character_info[EQUIPMENT_INDEX][HIT_POINTS_INDEX]
    equipment = character_info[EQUIPMENT_INDEX][REMOVE_HP_INFO:]