#import algorithms
from wikiracer import MaxPathLengthExceeded
from helper import PageRequestError, PathDeadend, FailedPath #import get_linked_pages, get_cos_sim

import requests
import wikipediaapi
from typing import List
from sentence_transformers import SentenceTransformer, util


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
        # accessing wikipedia api 
        wiki_access = wikipediaapi.Wikipedia('Aldo & Richard', 'en')
        wiki_start = wiki_access.page(start_page) # wiki page for start 
        wiki_dest = wiki_access.page(dest_page) # wiki page for dest

        if (wiki_start.exists() and wiki_dest.exists()):
            visited = [start_page] # list of visisted pages
            count = 0 # # page visit count
            current_wiki = wiki_start # tracks current wiki page

            while count < self.max_path_length:
                # comment out lateer, helps us visualize the path
                print(count)
                print(visited)

                # exception for dead pages
                if not current_wiki.exists:
                    raise PathDeadend
                
                # get Linked Pages - we will only once per title
                links = self.get_linked_pages(current_wiki, visited)

                # get link with highest cos sim and 'visit'
                most_sim_page = self.get_most_similar(links, dest_page)
                visited.append(most_sim_page)

                # path completed
                if most_sim_page == dest_page:
                    return visited
                
                # updated current and count
                current_wiki = wiki_access.page(most_sim_page)
                count += 1
            
            raise MaxPathLengthExceeded(f"Path of length less than or equal to {self.max_path_length} could not be found.")
        
        # start doesn't exist
        elif (not wiki_start.exists()):
            raise PageRequestError("Start page does not exist as a wikipedia title")
        
        # dest doesn't exist
        else:
            raise PageRequestError("Destination page does not exist as a wikipedia title")


    def get_linked_pages(self, page, visited):
        """
        returns the title of all the linked pages of a wikipedia page
        """
        #gets the raw pages
        links = page.links
        linked_pages = []
        for title in links.keys():
            if title not in visited: 
                # print(type(title))
                linked_pages.append(title)

        return linked_pages
        

    def get_most_similar(self, links, target_page):
        """
        returns the t
        """
        # encoding target page
        encoded_target = self.model.encode(target_page)

        # sorting links by cosine similarity
        sorted_links = sorted(links,key = lambda title: util.cos_sim(self.model.encode(title), encoded_target)[0][0].item(), reverse=True)
        
        # checking if page w/ highets cos sim exists
        wiki_page = wiki_access.page(sorted_links[0])


        while not wiki_page.exists(): 
            # checking to see if there exists a lists
            if not sorted_links:
                raise PathDeadend
            
            # pop out pages that don't exist
            sorted_links.pop(0)
            wiki_page = wiki_access.page(sorted_links[0])
            
        return sorted_links[0]


    

# def main():
#     findPath("Pomona College", "Pitzer College")

if __name__ == "__main__":
#     main()
    tester_1 = Greedy()
    # print(tester_1.find_path("Pomona College", "Inland Empire"))
    # print("done")

    wiki_access = wikipediaapi.Wikipedia('Aldo & Richard', 'en')
    # wiki_start = wiki_access.page("Pomona College") 
    # wiki_start = wiki_access.page("Moses Hahl")
    # print(wiki_start.exists())
    print(tester_1.find_path("Pomona College", "Albert Einstein"))

    # Issue with Pomona College to Albert Einstein - parse line 80


