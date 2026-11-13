import json
from google_crc32c import value
import pandas as pd 
col = {"date": 0, "tournament": 1, "ground": 2, "result": 4,
           "opponent": 11, "opp_bday": 16}


#output lists of matches from the js text
def find_all_matches(text):
    start = text.index("[[")
    end = text.rindex("]") + 1
    return json.loads(text[start:end])

def build_match_df(ma):
    return pd.DataFrame({col: [m[i] for m in ma] for col, i in col.items()})

def bday_format_check(bday):
    if len(bday) == 8 and bday.isdigit():
        return True 
    return False

def oppo_age_insert(tb):
    tb= tb.copy()
    tb['date']  = pd.to_datetime(tb['date'], format='%Y%m%d')
    part = tb.loc[tb['opp_bday']!= "", "opp_bday"].iloc[0]
    if bday_format_check(part):
        bday_date = pd.to_datetime(tb['opp_bday'], format='%Y%m%d', errors="coerce")
        tb['oppo_age'] = (tb['date'] - bday_date).dt.days // 365.25
    else: 
        tb['oppo_age'] = pd.to_numeric(tb['opp_bday'], errors='coerce')
    return tb


