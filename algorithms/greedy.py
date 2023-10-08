from algorithms.wikiracer import WikiRacer


class Greedy(WikiRacer):
    def __init__(self, max_path_length, doc_sim_func):
        """
        Parameters
        ----------
        max_path_length : int 
        doc_sim_func : function
            Takes two wikipedia page titles and returns
            some measure of their similarity.
        """
        super().__init__(max_path_length)
        self.doc_sim = doc_sim_func
        self.max_path_length = max_path_length #18


    def set_max_path(self, max_path_length: int):
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
        pass