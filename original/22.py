import sys

grid = [list(line.rstrip()) for line in sys.stdin]
y = len(grid) // 2
x = len(grid[0]) // 2
pos = x + 1j*y
direction = -1j
infections = 0
memo = {}
for _ in range(10000000):
    if pos.real >= len(grid[0]):
        grid = list(map(lambda x: x + ['.'], grid))
    if pos.imag >= len(grid):
        row = [list('.' * len(grid[0]))]
        grid += row
    if pos.real < 0:
        pos = 0 + pos.imag*1j
        grid = list(map(lambda x: ['.'] + x, grid))
    if pos.imag < 0:
        pos = pos.real
        grid = [list('.' * len(grid[0]))] + grid
    x, y = int(pos.real), int(pos.imag)
    if grid[int(pos.imag)][int(pos.real)] == '#':
        grid[int(pos.imag)][int(pos.real)] = 'F'
        direction *= 1j
    elif grid[int(pos.imag)][int(pos.real)] == '.':
        grid[int(pos.imag)][int(pos.real)] = 'W'
        direction /= 1j
    elif grid[y][x] == 'W':
        grid[y][x] = '#'
        infections += 1
    elif grid[y][x] == 'F':
        grid[y][x] = '.'
        direction *= -1
    # memo[(grid,pos,direction)] = (grid, grid[y][x] == '#')
    pos += direction
print(infections) 
