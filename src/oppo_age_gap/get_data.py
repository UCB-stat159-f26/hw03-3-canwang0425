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

def download_abstract_file(url_name):
    res = requests.get(ABSTRACT_URL.format(url_name), headers=HEADERS,timeout = 10)
    if res.status_code == 200 and  "[[" in res.text:
        return res.text
    raise ValueError(f"Having issues to download file for {url_name}. Status code: {res.status_code}")