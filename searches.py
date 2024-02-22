from queue import PriorityQueue
from typing import Callable

from node import Node
from problem import Problem


def best_first_search(problem: Problem, f: Callable) -> Node | None:
    node = Node(problem.get_initial(), f)
    frontier = PriorityQueue()
    frontier.put((f(node), node))
    reached = {str(node.state): node}
    while not frontier.empty():
        node = frontier.get()[1]
        if problem.is_goal(node.state):
            return node
        for child in problem.expand(node):
            s = str(child.state)
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.put((f(child), child))
    return None


def greedy_best_first_search(problem: Problem, f: Callable) -> Node | None:
    node = Node(problem.get_initial(), f)
    return greedy_best_first_search_rec(problem, node, 100, {str(node.state): node})


def greedy_best_first_search_rec(problem: Problem, node: Node, depth, seen) -> Node | None:
    if depth <= 0:
        return None
    if problem.is_goal(node.state):
        return node
    children = problem.expand(node)
    while children:
        best_child = min(children, key=lambda x: x.heuristic_value)
        children.remove(best_child)
        s = str(best_child.state)
        if s not in seen:
            seen[s] = best_child
            res = greedy_best_first_search_rec(problem, best_child, depth - 1, seen)
            if res is not None:
                return res
    return None
