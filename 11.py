with open('11.in') as inp:
    for line in inp.readlines():
        directions = line.strip().split(',')
        x, y = 0, 0
        max_dist = 0
        # See 11.md for a justification for these distances.
        values = {'n': (0, 2), 's': (0, -2), 'ne': (1, 1), 'nw': (-1, 1),
                  'se': (1, -1), 'sw': (-1, -1)}
        for direction in directions:
            dx, dy = values[direction]
            x += dx
            y += dy
            x_dist, y_dist = abs(x), abs(y)
            # See 11.md for a justification on this formula and how the grid works.
            dist = x_dist + (y_dist - min(x_dist, y_dist))//2
            max_dist = max(max_dist, dist)

        # Part 1.
        print(dist)
        # Part 2.
        print(max_dist)
