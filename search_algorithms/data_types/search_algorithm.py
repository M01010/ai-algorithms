from abc import ABC, abstractmethod

from search_algorithms.data_types.problem import Problem
from search_algorithms.data_types.node import Node
from search_algorithms.data_types.heuristic import HeuristicFunction


class SearchAlgorithm(ABC):

    @abstractmethod
    def solve(self, problem: Problem) -> Node | None:
        """
        solves the problem using a search algorithm
        :param problem: Problem\n
        use abstract class Problem to formulate your own problem to solve it using this method
        :return: Node for a solution / None for no solution
        """
        pass


class HeuristicSearchAlgorithm(SearchAlgorithm):
    @property
    @abstractmethod
    def heuristic(self) -> HeuristicFunction:
        pass
