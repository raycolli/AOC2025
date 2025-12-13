from functools import cache
import networkx as nx

def parse_raw():
    with open('input.txt', 'r') as f:
        raw = f.read()
    lines = [line.partition(": ") for line in raw.splitlines()]
    return nx.DiGraph({node: neighbors.split() for node, _, neighbors in lines})

G = parse_raw()

def part1():
    return len(list(nx.all_simple_paths(G, "you", "out")))

@cache
def npaths(node, seen):
    if node == "out":
        return seen == 2
    seen += node in {"fft", "dac"}
    return sum(npaths(neighbor, seen) for neighbor in G[node])

def part2():
    return npaths("svr", 0)

print("Part 1:", part1())
print("Part 2:", part2())