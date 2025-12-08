from functools import reduce
from operator import mul

class Problem:
    def __init__(self, op, nums):
        self.op = op
        self.nums = nums

def solve(problems):
    total = 0
    for problem in problems:
        if problem.op == '+':
            total += sum(problem.nums)
        elif problem.op == '*':
            total += reduce(mul, problem.nums, 1)
        else:
            raise ValueError(f"Unknown operator {problem.op}")
    return total

def parse_blocks(lines):
    """Split input into vertical blocks by columns of spaces."""
    ccol = len(lines[0])
    block_start = 0
    for icol in range(ccol):
        if all(line[icol] == ' ' for line in lines):
            yield get_block(lines, block_start, icol)
            block_start = icol + 1
    yield get_block(lines, block_start, ccol)

def get_block(lines, icol_from, icol_to):
    """Return a block as a list of strings for each row, sliced by column range."""
    return [line[icol_from:icol_to] for line in lines]

def transpose(lines):
    """Transpose rows and columns."""
    return [''.join(line[i] for line in lines) for i in range(len(lines[0]))]

def part1(input_text):
    lines = [line.rstrip('\n') for line in input_text.splitlines() if line.strip()]
    problems = []
    for block in parse_blocks(lines):
        op = block[-1].strip()
        nums = [int(line.strip()) for line in block[:-1]]
        problems.append(Problem(op, nums))
    return solve(problems)

def part2(input_text):
    lines = [line.rstrip('\n') for line in input_text.splitlines() if line.strip()]
    problems = []
    for block in parse_blocks(lines):
        t_block = transpose(block)
        op = t_block[0].strip()[-1]
        nums = [int(col[:-1]) for col in t_block]
        problems.append(Problem(op, nums))
    return solve(problems)

if __name__ == "__main__":
    with open("input.txt") as f:
        input_text = f.read()
    part1 = part1(input_text)
    part2 = part2(input_text)
    print("Part 1:", part1)
    print("Part 2:", part2)