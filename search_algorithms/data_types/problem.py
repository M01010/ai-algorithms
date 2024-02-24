from abc import ABC, abstractmethod

from search_algorithms.data_types.node import Node


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
