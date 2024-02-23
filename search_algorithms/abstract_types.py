from abc import ABC, abstractmethod
from typing import Callable


class Node:
    """
    Node class representing a node in the graph
    """

    def __init__(self, state, heuristic_fn=lambda x: 0, path_cost=0, parent=None):
        self.state = state
        self.f = heuristic_fn

        self.path_cost = path_cost
        self.parent = parent

        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

        self.heuristic_value = heuristic_fn(self)

    def __lt__(self, other):
        """
        this is necessary to use a node inside a priority queue
        """
        return self.heuristic_value < other.heuristic_value


class Problem(ABC):
    """
    Abstract Problem class representing any problem
    """

    @property
    @abstractmethod
    def initial(self):
        """
        initial state of the problem:\n
        you can use a random state or any state you like
        """
        pass

    @abstractmethod
    def is_goal(self, state):
        """
        check if the state is a solution to the problem
        """
        pass

    @abstractmethod
    def expand(self, node: Node) -> list[Node]:
        """
        produces all children / neighbors of a node in the graph
        """
        pass


HeuristicFunction = Callable[[Node], float]
"""
a Heuristic function you have to minimize
"""

null_heuristic: HeuristicFunction = lambda x: 0


class SearchAlgorithm(ABC):

    @abstractmethod
    def solve(self, problem: Problem) -> Node | None:
        pass


class HeuristicSearchAlgorithm(SearchAlgorithm):
    @property
    @abstractmethod
    def heuristic(self) -> HeuristicFunction:
        pass
