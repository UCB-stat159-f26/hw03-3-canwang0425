from .get_data import (download_abstract_file, find_bday_from_gender_page,
                       get_player_for_url, name_shown)
from .parse_data import (build_match_df, find_all_matches, oppo_age_insert,
                         player_age_insert)


#uses all the outputs from other helper functiosn to make into a comprehensive table for each player
def get_player_matches_data(name):
    url_name  = get_player_for_url(name)
    text = download_abstract_file(url_name)
    table = oppo_age_insert(build_match_df(find_all_matches(text)))
    player_bday = find_bday_from_gender_page(url_name)
    table = player_age_insert(table, player_bday)
    table['player'] = name_shown(url_name)
    return table.reset_index(drop=True)