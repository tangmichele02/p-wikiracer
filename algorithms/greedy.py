from algorithms.wikiracer import WikiRacer
#import algorithms.helper #import get_linked_pages, get_cos_sim
import requests
from typing import List
from sentence_transformers import SentenceTransformer, util


class Greedy(WikiRacer):
    def __init__(self):
        """
        Parameters
        ----------
        max_path_length : int 
        doc_sim_func : function
            Takes two wikipedia page titles and returns
            some measure of their similarity.
        """
        #super().__init__(max_path_length)
        #self.doc_sim = doc_sim_func
        self.max_path_length = 18 
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')



    def set_max_path(self, max_path_length):
        if max_path_length < 1:
            raise ValueError("Max path length must be at least 1")
        self.max_path_length = max_path_length


    def find_path(self, start_page: str, dest_page: str) -> List[str]:
        """
        Returns a list of Wikipedia page titles representing the path.
        The `start_page` should be included as the first page of the path
        and the `dest_page` should be included at the end of the path.

        Should raise `FailedPath` exception if it can't find a path for
        a reason other than an api call failure.
        """
        visited = set()
        count = 1 #or 0
        # Need to run a while loop that while we have not reached max path length
        # Or the destination has to been found
        while True:
            
            # get Linked Pages - we will only once per title
            # get_cos_sim - Pomona -> Claremont Colleges -> Pomonaona 
            # Call that until we get a unqiue vale
            #
        

    def get_linked_pages(self, page):
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

def get_most_similar(self, links, target_page, visited):
    # target_embed = model.encode(getLinkedPages(target_page))
    highest_sim = ("", -1)
    encoded_target = self.model.encode(target_page)

    for ind in range(len(links)):
        encoded_link = self.model.encode(links[ind])
        sim = util.cos_sim(encoded_link, encoded_target)
        sim_val = sim[0][0].item()
        if sim_val > highest_sim[1] and sim_val not in visited:
            highest_sim = (links[ind], sim_val)
    return highest_sim[0]
