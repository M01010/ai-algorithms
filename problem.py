from abc import ABC, abstractmethod
from node import Node


class Problem(ABC):
    @abstractmethod
    def is_goal(self, state):
        pass

    @abstractmethod
    def expand(self, node: Node) -> list[Node]:
        pass

    @abstractmethod
    def get_initial(self):
        pass
