import time

from heuristics import collisions_1, collisions_2, num_queens_endangered
from n_queens_problem import NQueensProblem
from searches import best_first_search, greedy_best_first_search


def test_alg(p, alg, h, num=1):
    start = time.time()
    for i in range(num):
        alg(p, h)
    end = time.time()
    return end - start


def main():
    p = NQueensProblem(50)
    combinations = [
        (best_first_search, collisions_1),
        (best_first_search, collisions_2),
        (best_first_search, num_queens_endangered),
        (greedy_best_first_search, collisions_1),
        (greedy_best_first_search, collisions_2),
        (greedy_best_first_search, num_queens_endangered),
    ]
    num = 100

    for alg, h in combinations:
        time_diff = test_alg(p, alg, h, num)
        avg_time = time_diff / num
        print(f'algorithm: {alg.__name__}')
        print(f'heuristic: {h.__name__}')
        print(f'time: {round(avg_time, 6)} S\n')


if __name__ == '__main__':
    main()
