from collections import defaultdict
import sys

def make_grid(inp):
    grid = defaultdict(lambda:'.')
    num_rows = num_cols = 0
    for y, line in enumerate(inp):
        num_rows += 1
        for x, c in enumerate(line.rstrip()):
            num_cols += 1 if x == 0 else 0
            grid[x + 1j*y] = c
    start_x = num_cols // 2
    start_y = num_rows // 2
    pos = start_x + 1j*start_y
    return grid, pos

def part_one(grid, pos, num_iterations=10000):
    direction = -1j
    infections = 0
    for _ in range(num_iterations):
        char = grid[pos]
        if char == '#':
            # The default value is '.' so we may delete this.
            del grid[pos]
            # Multiplying by j corresponds to a right rotation (remember
            # that negative y is up).
            direction *= 1j
        elif char == '.':
            grid[pos] = '#'
            # Since multiplying by j is a right rotation, dividing by it is a
            # left rotation.
            infections += 1
            direction /= 1j
        pos += direction
    return infections

def part_two(grid, pos, num_iterations=10000000):
    direction = -1j
    infections = 0
    for _ in range(num_iterations):
        char = grid[pos]
        if char == '#':
            grid[pos] = 'F'
            # Multiplying by j corresponds to a right rotation (remember
            # that negative y is up).
            direction *= 1j
        elif char == '.':
            grid[pos] = 'W'
            # Since multiplying by j is a right rotation, dividing by it is a
            # left rotation.
            direction /= 1j
        elif char == 'W':
            grid[pos] = '#'
            infections += 1
        elif char == 'F':
            # The default value is '.'.
            del grid[pos]
            direction *= -1
        pos += direction
    return infections

if __name__ == '__main__':
    grid, pos = make_grid(sys.stdin)
    print(part_one(grid, pos))
    print(part_two(grid, pos))
