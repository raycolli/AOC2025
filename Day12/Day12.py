import numpy as np

def extract_ints(s):
    """Extract all integers from a string."""
    import re
    return [int(x) for x in re.findall(r'-?\d+', s)]

def parse_raw():
    with open('input.txt', 'r') as f:
        data = f.read()
    
    *packages, regions = data.split("\n\n")
    areas = np.array([package.count("#") for package in packages])
    as_ints = map(extract_ints, regions.splitlines())
    fits = [(h * w, np.array(data)) for h, w, *data in as_ints]
    return areas, fits

AREA, FITS = parse_raw()

def part1():
    return sum(area >= AREA @ region for area, region in FITS)

if __name__ == "__main__":
    print(f"Part 1: {part1()}")