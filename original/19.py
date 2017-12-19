import itertools, sys, string


grid = [line for line in sys.stdin]
x = y = 0
prev_dir = (0, 0)
for index, let in enumerate(grid[0]):
    if let == '|':
        x = index
        prev_dir = (0, 1)
        break
    if let == '-':
        x = index
        prev_dir = (1,0)
        break
letts = ''
dirs = {(-1,0), (1,0), (0,1), (0,-1)}
steps = 1
while True:
    new_x, new_y = x + prev_dir[0], y + prev_dir[1]
    if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] != ' ':
        steps += 1
        x, y = new_x, new_y
        if grid[y][x] in string.ascii_uppercase:
            letts += grid[y][x]
    else:
        success = False
        bwds_dir = (-prev_dir[0], -prev_dir[1])
        for d in dirs - {bwds_dir}:
            new_x, new_y = x + d[0], y + d[1]
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                if grid[new_y][new_x] != ' ':
                    prev_dir = d
                    success = True
        if not success:
            print(letts)
            print(steps)
            break
