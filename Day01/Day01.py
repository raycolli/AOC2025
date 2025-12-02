def count_zero_hits(lines):
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

with open("input.txt") as f:
    lines = f.readlines()

print(count_zero_hits(lines))
