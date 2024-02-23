import time
from itertools import product
from search_algorithms.abstract_types import Problem, SearchAlgorithm, HeuristicFunction


def test_algorithm_combinations(problem: Problem, algorithms: list[SearchAlgorithm],
                                heuristics: list[HeuristicFunction], iterations=1):
    combinations = product(algorithms, heuristics)
    for algorithm, heuristic in combinations:
        test_algorithm(problem, algorithm, heuristic, iterations)


def test_algorithm(problem: Problem, search_algorithm: SearchAlgorithm, h: HeuristicFunction, iterations=1):
    print(f'algorithm: {search_algorithm.__name__}')
    print(f'heuristic: {h.__name__}')
    start = time.time()
    failures = 0
    for i in range(iterations):
        solution = search_algorithm(problem, h)
        if solution is None:
            failures += 1
    accuracy = (iterations - failures) / iterations
    time_diff = time.time() - start
    avg_time = time_diff / iterations
    print(f'time: {round(avg_time, 6)} Seconds')
    print(f'accuracy: {round(accuracy*100, 6)}%')
    print()
