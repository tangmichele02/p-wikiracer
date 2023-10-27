#import algorithms
from wikiracer import WikiRacer
import helper #import get_linked_pages, get_cos_sim

import requests
from typing import List
from sentence_transformers import SentenceTransformer, util

import os
print("blah")
print(os.getcwd())

class Greedy():
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


    def find_path(self, start_page: str, dest_page: str):
        """
        Returns a list of Wikipedia page titles representing the path.
        The `start_page` should be included as the first page of the path
        and the `dest_page` should be included at the end of the path.

        Should raise `FailedPath` exception if it can't find a path for
        a reason other than an api call failure.
        """
 
        try:
            self.access_data(start_page)
        except:
            return "Start page does not exist"
        
        try:
            self.access_data(dest_page)
        except:
            return "Destination page does not exist "
        
        visited = [start_page]
        count = 0 #or 1
        # Need to run a while loop that while we have not reached max path length
        # Or the destination has to been found
        current_page = start_page

        while count < self.max_path_length:
            print(count)
            print(visited)
            # get Linked Pages - we will only once per title
            links = self.get_linked_pages(current_page, visited)
            most_sim_page = self.get_most_similar(links, dest_page)
            visited.append(most_sim_page)
            if most_sim_page == dest_page:
                return visited
            current_page = most_sim_page
            count += 1
            # get_cos_sim - Pomona -> Claremont Colleges -> Pomonaona 
            # Call that until we get a unqiue vale
        raise Exception('Failed Path')

        
        

        

    def access_data(self, page):
        """
        returns a list of links for a wikipedia page 
        """

        api_url = "https://en.wikipedia.org/w/api.php"

        params = {
        'action': 'parse',
        'page': page,
        'format': 'json'
        }

        response = requests.get(api_url, params=params)
        data = response.json()

        return data
        



    def get_linked_pages(self, page, visited):
        """
        returns the title of all the linked pages of a wikipedia page
        """

        try:
            data = self.access_data(page)
        except:
            return "Page does not exist"
        # try: 
        #     api_url = "https://en.wikipedia.org/w/api.php"

        #     params = {
        #     'action': 'parse',
        #     'page': page,
        #     'format': 'json'
        #     }

        #     response = requests.get(api_url, params=params)
        #     data = response.json()
        # except:
        #     print("Page does not exist")
        # print(type(data['parse']['links']))

        linked_pages = []
        #res.append(page)
        

        for row in data['parse']['links']: # possibility of of adding list comprehensio
            # title of a linked page
            cur_page = row['*']
            if cur_page not in visited:
                linked_pages.append(cur_page)

        return linked_pages

    def get_most_similar(self, links, target_page):
        # target_embed = model.encode(getLinkedPages(target_page))
        highest_sim = ("", -1)
        encoded_target = self.model.encode(target_page)

        for ind in range(len(links)):
            encoded_link = self.model.encode(links[ind])
            sim = util.cos_sim(encoded_link, encoded_target)
            sim_val = sim[0][0].item()
            if (sim_val > highest_sim[1]):  #and sim value not in visited?
                highest_sim = (links[ind], sim_val)
        
        return highest_sim[0]

# def main():
#     findPath("Pomona College", "Pitzer College")

# if __name__ == "__main__":
#     main()
tester_1 = Greedy()
print(tester_1.find_path("Tilo RC", "Inland Empire"))
# Issue with Pomona College to Albert Einstein - parse line 80

