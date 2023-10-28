#import algorithms
from wikiracer import MaxPathLengthExceeded
from helper import PageRequestError #import get_linked_pages, get_cos_sim

import requests
import wikipediaapi
from typing import List
from sentence_transformers import SentenceTransformer, util

import os
# print("blah")
# print(os.getcwd())

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
        wiki_access = wikipediaapi.Wikipedia('Aldo & Richard', 'en')
        wiki_start = wiki_access.page(start_page) 
        wiki_dest = wiki_access.page(dest_page)

        if (wiki_start.exists() and wiki_dest.exists()):
            visited = [start_page]
            count = 0 #or 1
            current_wiki = wiki_start

            while count < self.max_path_length:
                print(count)
                print(visited)
                # get Linked Pages - we will only once per title
                links = self.get_linked_pages(current_wiki, visited)
                # print(links)


                most_sim_page = self.get_most_similar(links, dest_page)
                visited.append(most_sim_page)
                if most_sim_page == dest_page:
                    return visited
                current_wiki = wiki_access.page(most_sim_page)
                count += 1
            raise MaxPathLengthExceeded(f"Path of length less than or equal to {self.max_path_length} could not be found.")
        elif (not wiki_start.exists()):
            raise PageRequestError("Start page does not exist as a wikipedia title")
        else:
            raise PageRequestError("Destination page does not exist as a wikipedia title")
        

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
        #gets the raw pages
        links = page.links
        linked_pages = []
        for title in sorted(links.keys()):
            if title not in visited:
                # print(type(title))
                linked_pages.append(title)

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
# tester_1 = Greedy()
# print(tester_1.find_path("Pomona College", "Inland Empire"))
# print("done")

# wiki_access = wikipediaapi.Wikipedia('Aldo & Richard', 'en')
# wiki_start = wiki_access.page("Pomona College") 
# print(tester_1.get_linked_pages(wiki_start, []))

# Issue with Pomona College to Albert Einstein - parse line 80

