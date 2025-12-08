def accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            neighbors += 1
                if neighbors < 4:
                    count += 1
    return count

def total_removed_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    total_removed = 0
    while True:
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    neighbors = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '@':
                                neighbors += 1
                    if neighbors < 4:
                        to_remove.append((r, c))
        if not to_remove:
            break
        for r, c in to_remove:
            grid[r][c] = '.'
        total_removed += len(to_remove)
    
    return total_removed

with open("input.txt") as f:
    grid = [list(line.strip()) for line in f if line.strip()]

part1 = accessible_rolls(grid)
print("Part 1:", part1)
import copy
part2 = total_removed_rolls(copy.deepcopy(grid))
print("Part 2:", part2)
