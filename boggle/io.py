import requests
from typing import List

def download_txt_file(txt_url: str = None, target_path: str = None) -> None:
    req = requests.get(txt_url)
    url_content = req.content 
    with open(target_path, 'wb') as f:
        f.write(url_content)

def get_word_list(txt_path: str) -> List[str]:
    with open('../data/wordlist.txt') as f:
        content = f.read().splitlines()
    return content
