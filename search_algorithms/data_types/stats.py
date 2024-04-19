from dataclasses import dataclass

from search_algorithms.data_types.search_algorithm import SearchAlgorithm, HeuristicSearchAlgorithm


@dataclass
class Stats:
    algorithm: SearchAlgorithm
    avg_time: float
    accuracy: float

    def __repr__(self):
        return f'{self.algorithm}\ntime: {round(self.avg_time, 6)} Seconds, accuracy: {round(self.accuracy * 100, 6)}%'
