LIMIT = 12

def max_joltage_part2(s: str) -> int:
    to_remove = len(s) - LIMIT
    stack = []

    for ch in s:
        while stack and to_remove > 0 and ch > stack[-1]:
            stack.pop()
            to_remove -= 1
        stack.append(ch)

    stack = stack[:LIMIT]
    joltage = 0
    for d in stack:
        joltage = joltage * 10 + int(d)
    return joltage

def max_joltage_part1(s: str) -> int:
    if not s:
        return 0
    max_joltage = 0
    for i, ch in enumerate(s):
        d = int(ch)
        # look left
        bl = max((int(x) * 10 + d for x in s[:i]), default=0)
        # look right
        br = max((d * 10 + int(x) for x in s[i+1:]), default=0)
        max_joltage = max(max_joltage, bl, br)
    return max_joltage

def main(file_path: str, part2: bool = True) -> int:
    total = 0
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if part2:
                total += max_joltage_part2(line)
            else:
                total += max_joltage_part1(line)
    return total

if __name__ == "__main__":
    file_path = "input.txt"
    print("Part1:", main(file_path, part2=False))
    print("Part2:", main(file_path, part2=True))
