def parse_ranges(path):
    with open(path, "r") as f:
        line = f.read().strip()
    ranges = []
    for part in line.split(","):
        a, b = part.split("-")
        ranges.append((int(a), int(b)))
    return ranges

def sum_invalid_ids(ranges):
    total = 0
    for lo, hi in ranges:
        lo_len = len(str(lo))
        hi_len = len(str(hi))

        for L in range(lo_len, hi_len + 1):
            if L % 2 != 0:
                continue
            half = L // 2

            lo_s = str(lo)
            hi_s = str(hi)

            if len(lo_s) == L:
                start_half = int(lo_s[:half])
            else:
                start_half = 10 ** (half - 1)

            if len(hi_s) == L:
                end_half = int(hi_s[:half])
            else:
                end_half = 10 ** half - 1

            for h in range(start_half, end_half + 1):
                hs = str(h)
                if len(hs) < half:
                    hs = "0" * (half - len(hs)) + hs
                cand = int(hs + hs)
                if lo <= cand <= hi:
                    total += cand
    return total

if __name__ == "__main__":
    ranges = parse_ranges("input.txt")   # your txt file
    answer = sum_invalid_ids(ranges)
    print(answer)
