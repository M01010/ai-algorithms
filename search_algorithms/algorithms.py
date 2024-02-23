from queue import PriorityQueue
from search_algorithms.abstract_types import Node, Problem, HeuristicFunction


def best_first_search(problem: Problem, f: HeuristicFunction) -> Node | None:
    node = Node(problem.initial, f)
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


def greedy_best_first_search(problem: Problem, f: HeuristicFunction) -> Node | None:
    node = Node(problem.initial, f)
    reached = {str(node.state): node}
    return greedy_best_first_search_rec(problem, node, 100, reached)


def greedy_best_first_search_rec(problem: Problem, node: Node, depth, reached) -> Node | None:
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
            res = greedy_best_first_search_rec(problem, best_child, depth - 1, reached)
            if res is not None:
                return res
    return None
