import random

from search_algorithms.abstract_types import Node, Problem


class NQueensProblem(Problem):

    def __init__(self, n, seed=None):
        self.n = n
        random.seed(seed)
        self.initial_state = self.random_state()

    def random_state(self) -> list[int]:
        # state = [n integers 1 to n]
        state = []
        nums = list(range(1, self.n + 1))
        while nums:
            c = random.choice(nums)
            state.append(c)
            nums.remove(c)
        return state

    def is_goal(self, state):
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if abs(state[j] - state[i]) == j - i:
                    return False
        return True

    def expand(self, node: Node) -> list[Node]:
        new_nodes = []
        for i in range(len(node.state)):
            for j in range(i + 1, len(node.state)):
                state_copy = node.state.copy()
                state_copy[i], state_copy[j] = state_copy[j], state_copy[i]
                new_node = Node(state=state_copy, heuristic_fn=node.f, parent=node, path_cost=node.depth+1)
                new_nodes.append(new_node)
        return new_nodes

    @property
    def initial(self):
        return self.initial_state


def num_queens_endangered(node: Node) -> float:
    state = node.state
    endangered = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if abs(state[j] - state[i]) == j - i:
                endangered += 1
                break
    return endangered


def collisions(node: Node) -> float:
    state = node.state
    diagonal_collision = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if abs(state[j] - state[i]) == j - i:
                diagonal_collision += 1
    return diagonal_collision
