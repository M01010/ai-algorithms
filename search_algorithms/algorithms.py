from enum import auto, Enum
from queue import PriorityQueue, LifoQueue

from search_algorithms.abstract_types import Problem, Node, SearchAlgorithm, HeuristicSearchAlgorithm, HeuristicFunction


class SolutionType(Enum):
    Cutoff = auto()
    Failure = auto()


class GreedyBestFirstSearch(HeuristicSearchAlgorithm):
    def __init__(self, heuristic):
        self.heuristic_function = heuristic

    @property
    def heuristic(self):
        return self.heuristic_function

    def solve(self, problem: Problem) -> Node | None:
        node = Node(state=problem.initial, heuristic_fn=self.heuristic)
        reached = {str(node.state): node}
        return self.greedy_bfs_rec(problem, node, 100, reached)

    @staticmethod
    def greedy_bfs_rec(problem: Problem, node: Node, depth, reached) -> Node | None:
        if depth <= 0:
            return None
        if problem.is_goal(node.state):
            return node
        children = problem.expand(node)
        while children:
            best_child = min(children, key=lambda x: x.heuristic_value)
            children.remove(best_child)
            s = str(best_child.state)
            if s not in reached:
                reached[s] = best_child
                res = GreedyBestFirstSearch.greedy_bfs_rec(problem, best_child, depth - 1, reached)
                if res is not None:
                    return res
        return None


class BestFirstSearch(HeuristicSearchAlgorithm):
    def __init__(self, heuristic):
        self.heuristic_function = heuristic

    @property
    def heuristic(self):
        return self.heuristic_function

    def solve(self, problem: Problem):
        node = Node(state=problem.initial, heuristic_fn=self.heuristic)
        frontier = PriorityQueue()
        frontier.put(node)
        reached = {str(node.state): node}
        while not frontier.empty():
            node = frontier.get()
            if problem.is_goal(node.state):
                return node
            for child in problem.expand(node):
                s = str(child.state)
                if s not in reached or child.path_cost < reached[s].path_cost:
                    reached[s] = child
                    frontier.put(child)
        return None


class AStarSearch(HeuristicSearchAlgorithm):
    def __init__(self, heuristic):

        self.heuristic_function = heuristic

    @property
    def heuristic(self) -> HeuristicFunction:
        return self.heuristic_function

    def solve(self, problem: Problem) -> Node | None:
        def gn_hn(node):
            return node.path_cost + self.heuristic(node)
        return BestFirstSearch(gn_hn).solve(problem)


class UniformCostSearch(HeuristicSearchAlgorithm):
    def __init__(self):
        def path_cost(node: Node):
            return node.path_cost

        self.heuristic_function = path_cost

    @property
    def heuristic(self) -> HeuristicFunction:
        return self.heuristic_function

    def solve(self, problem: Problem) -> Node | None:
        return BestFirstSearch(self.heuristic).solve(problem)


class BreadthFirstSearch(HeuristicSearchAlgorithm):
    def __init__(self):
        def node_depth(node: Node):
            return node.depth

        self.heuristic_function = node_depth

    @property
    def heuristic(self) -> HeuristicFunction:
        return self.heuristic_function

    def solve(self, problem: Problem) -> Node | None:
        return BestFirstSearch(self.heuristic).solve(problem)


class DepthFirstSearch(SearchAlgorithm):
    def solve(self, problem: Problem) -> Node | None:
        node = Node(state=problem.initial)
        frontier = LifoQueue()
        frontier.put(node)
        reached = {str(node.state): node}
        while not frontier.empty():
            node = frontier.get()
            for child in problem.expand(node):
                s = str(child.state)
                if problem.is_goal(child.state):
                    return child
                if s not in reached:
                    reached[s] = child
                    frontier.put(child)
        return None


class DepthLimitedSearch(SearchAlgorithm):
    def __init__(self, limit):
        self.limit = limit

    def solve(self, problem: Problem):
        return self.recursiveDLS(Node(problem.initial), problem, self.limit)

    @staticmethod
    def recursiveDLS(node: Node, problem: Problem, limit):
        cutoff = False
        if problem.is_goal(node.state):
            return node
        elif node.depth == limit:
            return SolutionType.Cutoff
        for child in problem.expand(node):
            res = DepthLimitedSearch.recursiveDLS(child, problem, limit)
            if res == SolutionType.Cutoff:
                cutoff = True
            elif res is not None:
                return None
        if cutoff:
            return SolutionType.Cutoff
        return None


class IterativeDeepeningSearch(SearchAlgorithm):
    def solve(self, problem: Problem):
        for d in range(0, 100):
            sol = DepthLimitedSearch(d).solve(problem)
            if sol != SolutionType.Cutoff:
                return sol
        return None
