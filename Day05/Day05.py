def parse_ranges(lines):
    ranges = []
    for line in lines:
        if not line.strip():
            break
        start, end = map(int, line.strip().split('-'))
        ranges.append((start, end))
    return ranges

def part1_fresh_count(file_path: str) -> int:
    """Count how many available ingredient IDs are fresh."""
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    blank_index = lines.index('\n')
    range_lines = lines[:blank_index]
    id_lines = lines[blank_index+1:]
    
    ranges = parse_ranges(range_lines)
    fresh_count = 0
    
    for line in id_lines:
        if not line.strip():
            continue
        ingredient_id = int(line.strip())
        if any(start <= ingredient_id <= end for start, end in ranges):
            fresh_count += 1
            
    return fresh_count

def part2_total_fresh(file_path: str) -> int:
    """Count all IDs considered fresh by the ranges, ignoring available IDs."""
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    blank_index = lines.index('\n')
    range_lines = lines[:blank_index]
    
    ranges = parse_ranges(range_lines)
    
    # merge overlapping ranges to avoid double-counting
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    for start, end in sorted_ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    
    # sum total number of fresh IDs
    total_fresh = sum(end - start + 1 for start, end in merged)
    return total_fresh

if __name__ == "__main__":
    file_path = "input.txt"
    part1 = part1_fresh_count(file_path)
    part2 = part2_total_fresh(file_path)
    print("Part 1:", part1)
    print("Part 2:", part2)
