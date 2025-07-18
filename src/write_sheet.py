
from constants import (
    STR_INDEX, DEX_INDEX, CON_INDEX, INT_INDEX, WIS_INDEX, CHA_INDEX,
    SPECIES_INDEX, NAME_INDEX, STATS_INDEX, MODS_INDEX, CLASS_INDEX,
    ABILITIES_INDEX, EQUIPMENT_INDEX, HIT_DICE_INDEX, HIT_POINTS_INDEX,
    REMOVE_HP_INFO, ALIGNMENT_INDEX, SPECIES_ABILITIES_INDEX, SIZE_INDEX,
    SPEED_INDEX, PASSIVE_PERCEPTION_BASE,

)

def write_sheet(character_info):
    token_dict = fill_dict(character_info)
    template = read_template('content/template.md')

    final_lines = []
    for line in template:
        processed_line = line
        for token, replacement in token_dict.items():
            if isinstance(replacement, list):
                replacement_list = '\n'.join(str(item) for item in replacement)
                processed_line = processed_line.replace(token, replacement_list)
            else:
                processed_line = processed_line.replace(token, str(replacement))
        final_lines.append(processed_line)

    expanded_lines = []
    for line in final_lines:
        expanded_lines.extend(line.split('\n'))
    return expanded_lines

def fill_dict(character_info):
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
    class_abilities = character_info[ABILITIES_INDEX]
    species_abilities = character_info[SPECIES_ABILITIES_INDEX]
    size = species_abilities[SIZE_INDEX]
    speed = species_abilities[SPEED_INDEX]
    hit_dice_size = character_info[EQUIPMENT_INDEX][HIT_DICE_INDEX]
    hit_points = int(character_info[EQUIPMENT_INDEX][HIT_POINTS_INDEX]) + con_mod
    equipment = character_info[EQUIPMENT_INDEX][REMOVE_HP_INFO:]
    passive_perception = PASSIVE_PERCEPTION_BASE + wis_mod

    token_dict = {
        "@str" : str_score,
        "@dex" : dex_score,
        "@con" : con_score,
        "@int" : int_score,
        "@wis" : wis_score,
        "@cha" : cha_score,
        "@stm" : str_mod,
        "@dem" : dex_mod,
        "@com" : con_mod,
        "@inm" : int_mod,
        "@wim" : wis_mod,
        "@chm" : cha_mod,
        "@spe" : species,
        "@name" : name,
        "@cla" : chosen_class,
        "@ali" : alignment,
        "@spd" : speed,
        "@siz" : size,
        "@hpm" : hit_points,
        "@die" : hit_dice_size,
        "@ppr" : passive_perception,
        "@cab" : class_abilities,
        "@sab" : species_abilities[2:],
        "@eqp" : equipment
    }
    return token_dict

def read_template(filepath):
    with open(filepath) as file:
        lines_list = list(map(str.strip, file))

    return lines_list