from dataclasses import dataclass

from search_algorithms.data_types.search_algorithm import SearchAlgorithm, HeuristicSearchAlgorithm


@dataclass
class Stats:
    algorithm: SearchAlgorithm
    avg_time: float
    accuracy: float

    def __repr__(self):
        if isinstance(self.algorithm, HeuristicSearchAlgorithm):
            line1 = f'algorithm: {type(self.algorithm).__name__}, heuristic: {self.algorithm.heuristic.__name__}\n'
        else:
            line1 = f'algorithm: {type(self.algorithm).__name__}\n'
        line2 = f'time: {round(self.avg_time, 6)} Seconds, accuracy: {round(self.accuracy * 100, 6)}%\n'
        return line1 + line2
