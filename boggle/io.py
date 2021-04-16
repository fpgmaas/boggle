import requests
from typing import List
import numpy as np
import re
from collections import Counter


def download_txt_file(txt_url: str = None, target_path: str = None) -> None:
    req = requests.get(txt_url)
    url_content = req.content 
    with open(target_path, 'wb') as f:
        f.write(url_content)

def get_word_list(txt_path: str) -> List[str]:
    with open(txt_path) as f:
        content = f.read().splitlines()
    return content

def process_word_list(word_list: np.array, min_word_length) -> np.array:
    # remove spaces at start and end of string
    word_list = np.char.strip(word_list)
    # keep only words consisting completely out of lowercase characters
    vmatch = np.vectorize(lambda x:bool(re.compile('^[a-z]+$').match(x)))
    word_list = word_list[vmatch(word_list)]
    # Keep only words with the correct minimum word length
    word_list = word_list[np.vectorize(len)(word_list)>=min_word_length]
    return word_list

def calculate_letter_probs_from_word_list(word_list):
    counter = Counter(''.join(word_list))
    total = sum(counter.values())
    letter_probs = {k: v / total for k, v in counter.items()}
    return letter_probs