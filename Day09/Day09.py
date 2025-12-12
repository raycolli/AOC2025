from itertools import combinations
from pathlib import Path
from shapely.geometry import Polygon

def load_points():
    points = []
    base = Path(__file__).parent
    with open(base / "input.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(","))
                points.append((x, y))
    return points

POINTS = load_points()

def area(a, b):
    x1, y1 = a
    x2, y2 = b
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

def rect(a, b):
    x1, y1 = a
    x2, y2 = b
    return Polygon([a, (x2, y1), b, (x1, y2)])

def part1():
    return max(area(a, b) for a, b in combinations(POINTS, 2))

def part2():
    polygon = Polygon(POINTS)
    return max(
        area(a, b) for a, b in combinations(POINTS, 2)
        if polygon.covers(rect(a, b))
    )

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())