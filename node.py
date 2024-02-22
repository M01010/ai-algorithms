class Node:
    # state = [n numbers 1 to n]
    def __init__(self, state, f, path_cost=0, parent=None):
        self.state = state
        self.path_cost = path_cost
        self.parent = parent
        self.f = f
        self.heuristic_value = f(self)

    def __gt__(self, other):
        return self.heuristic_value > other.heuristic_value

    def __lt__(self, other):
        return self.heuristic_value < other.heuristic_value
