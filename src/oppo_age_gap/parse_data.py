import json
import pandas as pd 
col = {"date": 0, "tournament": 1, "ground": 2, "result": 4,
           "opponent": 11, "opp_bday": 16}


#output lists of matches from the js text
def find_all_matches(text):
    start = text.index("[[")
    end = text.rindex("]") + 1
    return json.loads(text[start:end])

def build_match_df(matches):
    return pd.DataFrame({a: [m[i] for m in matches] for a, i in col.items()})

def bday_format_check(bday):
    if len(bday) == 8 and bday.isdigit():
        return True 
    return False

def oppo_age_insert(table):
    tab= table.copy()
    tab['date']  = pd.to_datetime(tab['date'], format='%Y%m%d')
    part = tab.loc[tab['opp_bday']!= "", "opp_bday"].iloc[0]
    if bday_format_check(part):
        bday_date = pd.to_datetime(tab['opp_bday'], format='%Y%m%d', errors="coerce")
        tab['oppo_age'] = (tab['date'] - bday_date).dt.days / 365.25
    else: 
        tab['oppo_age'] = pd.to_numeric(tab['opp_bday'], errors='coerce')
    return tab


def player_age_insert(table,player_bday):
    tb = table.copy()
    player_bday = pd.to_datetime(player_bday, format='%Y%m%d')
    tb['player_age'] = (tb['date'] - player_bday).dt.days / 365.25
    tb['age_diff'] = tb['player_age'] - tb['oppo_age']
    return tb