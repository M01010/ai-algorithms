import time

from search_algorithms.data_types import SearchAlgorithm, Problem, Stats


def analyze_algorithms(algorithms: list[SearchAlgorithm], problems: list[Problem]) -> list[Stats]:
    """
    analyze algorithms with problems
    """
    stats = [analyze_algorithm(a, problems) for a in algorithms]
    return sorted(stats, key=lambda x: x.avg_time)


def analyze_algorithm(algorithm: SearchAlgorithm, problems: list[Problem]) -> Stats:
    start = time.time()
    accuracy = test_algorithm_accuracy(algorithm, problems)
    time_diff = time.time() - start
    avg_time = time_diff / len(problems)
    return Stats(algorithm, avg_time, accuracy)


def test_algorithm_speed(search_algorithm: SearchAlgorithm, problems: list[Problem]) -> float:
    """
    tests algorithm and heuristic function any number of iterations and returns average time
    """
    start = time.time()
    for p in problems:
        search_algorithm.solve(p)
    time_diff = time.time() - start
    avg_time = time_diff / len(problems)
    return avg_time


def test_algorithm_accuracy(search_algorithm: SearchAlgorithm, problems: list[Problem]) -> float:
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
