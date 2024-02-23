import time
from dataclasses import dataclass

from search_algorithms.abstract_types import Problem, SearchAlgorithm, HeuristicSearchAlgorithm


@dataclass
class Stats:
    algorithm: SearchAlgorithm
    avg_time: float
    accuracy: float


def analyze_algorithms(problems: list[Problem], algorithms: list[SearchAlgorithm]) -> list[Stats]:
    """
    analyze algorithms with problems
    """
    stats = []
    for algorithm in algorithms:
        start = time.time()
        accuracy = test_algorithm_accuracy(problems, algorithm)
        time_diff = time.time() - start
        avg_time = time_diff / len(problems)
        stats.append(Stats(algorithm, avg_time, accuracy))
    stats = sorted(stats, key=lambda x: x.avg_time)
    return stats


def show_stats(stats: list[Stats]):
    for s in stats:
        if isinstance(s.algorithm, HeuristicSearchAlgorithm):
            print(f'algorithm: {type(s.algorithm).__name__}, heuristic: {s.algorithm.heuristic.__name__}')
        else:
            print(f'algorithm: {type(s.algorithm).__name__}')
        print(f'time: {round(s.avg_time, 6)} Seconds, accuracy: {round(s.accuracy * 100, 6)}%')
        print()


def test_algorithm_speed(problems: list[Problem], search_algorithm: SearchAlgorithm):
    """
    tests algorithm and heuristic function any number of iterations and returns average time
    """
    start = time.time()
    for p in problems:
        search_algorithm.solve(p)
    time_diff = time.time() - start
    avg_time = time_diff / len(problems)
    return avg_time


def test_algorithm_accuracy(problems: list[Problem], search_algorithm: SearchAlgorithm):
    """
    tests algorithm and heuristic function on a list of different problems and returns accuracy
    """
    total_problems = len(problems)
    failures = 0
    for p in problems:
        solution = search_algorithm.solve(p)
        if solution is None:
            failures += 1
    accuracy = (total_problems - failures) / total_problems
    return accuracy
