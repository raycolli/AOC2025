from itertools import combinations, count
import numpy as np
from scipy.optimize import linprog
import re

def extract_ints(s):
    """Extract all integers from a string."""
    return [int(x) for x in re.findall(r'-?\d+', s)]

with open('input.txt', 'r') as f:
    RAW = f.read()

def parse_raw():
    for line in RAW.splitlines():
        lights, *buttons, joltages = line.split()
        lights = sum(2**i * (c == "#") for i, c in enumerate(lights[1:-1]))
        buttons = [sum(1 << i for i in extract_ints(button)) for button in buttons]
        joltages = list(extract_ints(joltages))
        yield lights, buttons, joltages

DATA: list[tuple[int, list[int], list[int]]] = list(parse_raw())

def fold_xor(pressed: tuple[int, ...]) -> int:
    initial, *rest = pressed
    for button in rest:
        initial ^= button
    return initial

def subset_sum(target: int, buttons: list[int]):
    for r in count(1):
        for pressed in combinations(buttons, r=r):
            if fold_xor(pressed) == target:
                return r
    return 0 

def part1():
    return sum(subset_sum(lights, buttons) for lights, buttons, _ in DATA)

def cheaty(buttons, goal):
    A = [[bool(button & (1 << i)) for button in buttons] for i in range(len(goal))]
    return linprog(np.ones(len(buttons)), A_eq=A, b_eq=goal, integrality=True).fun

def part2():
    return int(sum(cheaty(buttons, joltages) for _, buttons, joltages in DATA))

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")