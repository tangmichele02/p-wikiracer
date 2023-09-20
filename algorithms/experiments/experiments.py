from algorithms.wikiracer import WikiRacer
from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class EvaluationResults():
    def __init__(self, paths: List[List[str]], failedGames: List[Tuple[str, str]], numGames, numVisted):
        assert numGames == len(paths) + len(failedGames)

        self.path_lengths = [len(path) for path in paths] + len(failedGames)*[None]
        self.failedGames = failedGames
        self.successfulGames = [(path[0], path[-1])  for path in paths]
        self.numVisted = numVisted

def evaluate_racer(racer: WikiRacer, numGames = 100):
    """
    Returns `EvaluationResults`.
    """
    pass