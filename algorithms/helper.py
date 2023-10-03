"""
File with a bunch of miscellaneous helper functions.
If this gets big enough, maybe the functions should be
moved to other files.
"""

import requests
from typing import List

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

def is_valid_path(path: List[str]):
    """
    Checks if each page in path is linked from
    the previous page.
    """
    pass

def get_first_linked_page(page):
    """
    Returns the first linked page on `page`.

    See https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy.
    """
    pass
