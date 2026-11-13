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

def find_player_bday(text):
    single_match =  re.search(r"var dob\s*=\s*(\d{8})", text)
    return single_match.group(1) if single_match else None

def find_bday_from_gender_page(url_name): 
    for i in PLAYER_URLS:
        res = requests.get(i.format(url_name), headers=HEADERS,timeout = 10)
        if res.status_code == 200:
            bday = find_player_bday(res.text)
            if bday is not None:
                return bday
    raise ValueError(f"Failed to find birthday for {url_name}.")