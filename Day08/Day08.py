from heapq import nlargest
from itertools import combinations
from math import dist, prod
import re


def extract_ints(text):
    return list(map(int, re.findall(r"-?\d+", text)))

def chunk(lst, size):
    return [tuple(lst[i:i+size]) for i in range(0, len(lst), size)]

class UnionFind:
    def __init__(self, items):
        self.parent = {x: x for x in items}
        self.size = {x: 1 for x in items}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

    @property
    def elements(self):
        return list(self.parent.keys())

    @property
    def components(self):
        groups = {}
        for x in self.parent:
            root = self.find(x)
            groups.setdefault(root, []).append(x)
        return list(groups.values())


with open("input.txt") as f:
    raw = f.read()

coords = chunk(extract_ints(raw), 3)
UF = UnionFind(coords)
DISTANCES = sorted(combinations(UF.elements, 2), key=lambda ps: dist(*ps))


def part1():
    uf = UnionFind(coords)
    for a, b in DISTANCES[:1000]:
        uf.merge(a, b)
    return prod(nlargest(3, map(len, uf.components)))


def part2():
    uf = UnionFind(coords)
    for a, b in DISTANCES:
        uf.merge(a, b)
        if len(uf.components) == 1:
            return a[0] * b[0]


print("Part 1:", part1())
print("Part 2:", part2())