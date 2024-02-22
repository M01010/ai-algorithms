from node import Node


def num_queens_endangered(node: Node) -> int:
    state = node.state
    endangered = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if abs(state[j] - state[i]) == j - i:
                endangered += 1
                break
    return endangered


def collisions_1(node: Node) -> int:
    state = node.state
    vertical_collisions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if abs(state[j] - state[i]) == j - i:
                vertical_collisions += 1
    return vertical_collisions


def collisions_2(node: Node) -> int:
    state = node.state
    vertical_collisions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if abs(state[j] - state[i]) == j - i:
                vertical_collisions += 1
        for j in range(i):
            if abs(state[i] - state[j]) == i - j:
                vertical_collisions += 1
    return vertical_collisions
