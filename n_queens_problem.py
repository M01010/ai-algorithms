import random

from node import Node
from problem import Problem


class NQueensProblem(Problem):

    def __init__(self, n):
        self.n = n
        self.initial = self.random_state(n)

    @staticmethod
    def random_state(n) -> list[int]:
        state = []
        nums = list(range(1, n + 1))
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
                new_node = Node(state_copy, node.f, node.path_cost + 1, node)
                new_nodes.append(new_node)
        return new_nodes

    def get_initial(self):
        return self.initial
