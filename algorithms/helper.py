"""
File with a bunch of miscellaneous helper functions.
If this gets big enough, maybe the functions should be
moved to other files.
"""

import requests
from typing import List

from sentence_transformers import SentenceTransformer, util

# Download model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

class PageRequestError(Exception):
    pass

def get_random_page():
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnnamespace": 0,  # Retrieve pages only from the main namespace (articles)
    }

    response = requests.get(api_url, params=params)

    if response.status_code != 200:
        raise PageRequestError(f"Status code {response.status_code}")

    data = response.json()
    random_page_title = data["query"]["random"][0]["title"]

    return random_page_title

def isValidPath(path: List[str]):
    """
    Checks if each page in path is linked from
    the previous page.
    """
    pass

def getFirstLinkedPage(page):
    """
    Returns the first linked page on `page`.

    See https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy.
    """

def getLinkedPages(page):
    """
    returns the title of all the linked pages of a wikipedia page
    """
    api_url = "https://en.wikipedia.org/w/api.php"

    params = {
    'action': 'parse',
    'page': page,
    'format': 'json'
    }

    response = requests.get(api_url, params=params)
    data = response.json()
    # print(type(data['parse']['links']))

    res = []
    #res.append(page)

    for row in data['parse']['links']:
        res.append(row['*'])

    return res

print(getLinkedPages("Pomona College"))

def getCosSim(links, target_page):
    # target_embed = model.encode(getLinkedPages(target_page))
    sim_list = []
    encoded_target = model.encode(target_page)

    for ind in range(len(links)):
        encoded_link = model.encode(links[ind])
        sim = util.cos_sim(encoded_link, encoded_target)

        sim_list.append((links[ind], sim))
    return sim_list
        
