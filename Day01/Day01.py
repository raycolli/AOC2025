def count_part1(lines):
    pos = 50
    zeros = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        if direction == 'L':
            pos = (pos - distance) % 100
        else:
            pos = (pos + distance) % 100

        if pos == 0:
            zeros += 1

    return zeros


def count_part2(lines):
    pos = 50
    zeros = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        step = -1 if direction == 'L' else 1

        for _ in range(distance):
            pos = (pos + step) % 100
            if pos == 0:
                zeros += 1

    return zeros


with open("input.txt") as f:
    lines = f.readlines()

print("Part 1:", count_part1(lines))
print("Part 2:", count_part2(lines))

