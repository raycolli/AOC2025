#!/usr/bin/env python3
from math import ceil, floor

def parse_ranges(path):
    with open(path, "r") as f:
        data = f.read().strip()
    ranges = []
    for part in data.split(","):
        a, b = part.split("-")
        ranges.append((int(a), int(b)))
    return ranges

def pow10(n):
    return 10 ** n

def part_one_sum(ranges):
    total = 0
    for lo, hi in ranges:
        found = set()
        lo_len = len(str(lo))
        hi_len = len(str(hi))
        for L in range(lo_len, hi_len + 1):
            if L % 2 != 0:
                continue
            half = L // 2
            # multiplier = 10**half + 1
            multiplier = pow10(half) + 1

            lo_s = str(lo)
            hi_s = str(hi)

            if len(lo_s) == L:
                start_half = int(lo_s[:half])
            else:
                start_half = pow10(half - 1)

            if len(hi_s) == L:
                end_half = int(hi_s[:half])
            else:
                end_half = pow10(half) - 1

            for h in range(start_half, end_half + 1):
                cand = h * multiplier
                if lo <= cand <= hi and len(str(cand)) == L:
                    found.add(cand)
        total += sum(found)
    return total

def part_two_sum(ranges):
    total_sum = 0
    for lo, hi in ranges:
        found = set()
        lo_len = len(str(lo))
        hi_len = len(str(hi))

        for L in range(lo_len, hi_len + 1):
            for d in range(1, L // 2 + 1):
                if L % d != 0:
                    continue
                r = L // d
                if r < 2:
                    continue

                multiplier = (pow10(d * r) - 1) // (pow10(d) - 1)

                p_min = ceil(lo / multiplier)
                p_max = floor(hi / multiplier)

                p_min = max(p_min, pow10(d - 1))
                p_max = min(p_max, pow10(d) - 1)
                if p_min > p_max:
                    continue

                for p in range(p_min, p_max + 1):
                    cand = p * multiplier
                    if lo <= cand <= hi and len(str(cand)) == L:
                        found.add(cand)

        total_sum += sum(found)
    return total_sum

if __name__ == "__main__":
    ranges = parse_ranges("input.txt")

    part1 = part_one_sum(ranges)
    part2 = part_two_sum(ranges)

    print("Part 1:", part1)
    print("Part 2:", part2)
