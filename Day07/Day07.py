from collections import Counter
with open("input.txt") as f:
    lines = f.read().splitlines()

# find S and all splitters as (row, col)
START = None
SPLITTERS = []

for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch == "S":
            START = (r, c)
        elif ch == "^":
            SPLITTERS.append((r, c))

# sort splitters by row so beams encounter them in the correct order
SPLITTERS.sort()


def part1():
    nsplits = 0
    beams = {START}  # set of (r, c)
    for sr, sc in SPLITTERS:
        new_beams = set()
        for br, bc in beams:
            if bc == sc and br < sr:
                nsplits += 1
                # spawn left and right beams at this row, one column left or right
                new_beams.add((sr, sc - 1))
                new_beams.add((sr, sc + 1))
            else:
                new_beams.add((br, bc))
        beams = new_beams
    return nsplits

# coordinate -> number of timelines
def part2():
    beams = Counter({START: 1})
    for sr, sc in SPLITTERS:
        updated = Counter()
        for (br, bc), count in beams.items():
            if bc == sc and br < sr:
                # split into two timelines
                updated[(sr, sc - 1)] += count
                updated[(sr, sc + 1)] += count
            else:
                updated[(br, bc)] += count
        beams = updated
    return sum(beams.values())


print("Part 1:", part1())
print("Part 2:", part2())