from abc import ABC, abstractmethod
from typing import List

class FailedPath(Exception):
    """
    Raised when a WikiRacer fails to find a path between the
    destination and start page.

    Note that if a WikiRacer fails to find a path because of
    an issue with an api call, that should *not* be considered
    a FailedPath exception.
    """
    pass

class MaxPathLengthExceeded(FailedPath):
    """
    Raised when path length exceeds the maximum allowed
    path length.
    """
    pass

class CyclingPath(FailedPath):
    """
    Raised when a page occurs more than once in a given path.
    """
    pass

class PathDeadend(FailedPath):
    """
    Raised when there are no pages left to visit.
    """
    pass

class WikiRacer(ABC):
    """
    Abstract base class for WikiRacers.

    Subclasses should implement the `find_path` method.
    """
    @abstractmethod
    def __init__(self, max_path_length):
        if max_path_length < 1:
            raise ValueError("Max path length must be at least 1")
        self.max_path_length = max_path_length
    @abstractmethod
    def find_path(self, start_page: str, dest_page: str) -> List[str]:
        """
        Returns a list of Wikipedia page titles representing the path.
        The `start_page` should be included as the first page of the path
        and the `dest_page` should be included at the end of the path.

        Should raise `FailedPath` exception if it can't find a path for
        a reason other than an api call failure.
        """
        pass


if __name__ == '__main__':
    a = WikiRacer()