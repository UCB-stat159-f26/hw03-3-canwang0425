import re
import pandas as pd
import requests

ABSTRACT_URL = "https://www.tennisabstract.com/jsmatches/{}Career.js"
PLAYER_URLS = ["https://www.tennisabstract.com/cgi-bin/wplayer.cgi?p={}",
               "https://www.tennisabstract.com/cgi-bin/player.cgi?p={}"]
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_player_for_url(name):
    first_last = name.strip().split()
    return "".join(f[0].upper() + f[1:] for f in first_last)

def name_shown(url_name):
    return re.sub(r"(?<!^)(?=[A-Z])", " ", url_name)

