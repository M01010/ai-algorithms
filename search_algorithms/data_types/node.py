from typing import Self, Callable


class Node:
    """
    Node class representing a node in the graph\n
    includes variables like state, depth, heuristic_fn
    """

    def __init__(self,
                 state,
                 heuristic_fn: Callable[[Self], float] = lambda x: 0,
                 path_cost: int = 0,
                 parent: Self = None,
                 ):
        self.state = state
        self.f = heuristic_fn

        self.path_cost = path_cost
        self.parent = parent

        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

        self.heuristic_value = heuristic_fn(self)

    @property
    def path(self) -> list[Self]:
        """
        gets all the nodes from the initial node to the solution
        :return: nodes: list[Node]
        """
        path = []
        current = self
        while current:
            path.append(current)
            current = current.parent
        return list(reversed(path))

    def show_path(self) -> None:
        """
        shows the path of the solution as a list of strings for each state
        """
        seq = ' -> '.join([str(x) for x in self.path])
        print(seq)

    def __repr__(self) -> str:
        return str(self.state)

    def __lt__(self, other: Self):
        """
        this is necessary to use a node inside a priority queue
        """
        return self.heuristic_value < other.heuristic_value
