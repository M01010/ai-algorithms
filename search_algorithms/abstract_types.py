from abc import ABC, abstractmethod
from typing import Callable


class Node:
    def __init__(self, state, f, path_cost=0, parent=None):
        self.state = state
        self.path_cost = path_cost
        self.parent = parent
        self.f = f
        self.heuristic_value = f(self)

    def __lt__(self, other):
        return self.heuristic_value < other.heuristic_value


class Problem(ABC):

    @property
    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def is_goal(self, state):
        pass

    @abstractmethod
    def expand(self, node: Node) -> list[Node]:
        pass


HeuristicFunction = Callable[[Node], float]
SearchAlgorithm = Callable[[Problem, HeuristicFunction], Node | None]
