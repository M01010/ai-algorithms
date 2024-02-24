from typing import Callable

from search_algorithms.data_types.node import Node

HeuristicFunction = Callable[[Node], float]
"""
a Heuristic function you have to minimize
"""
