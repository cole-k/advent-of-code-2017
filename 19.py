import itertools, sys, string


class Coord:
    '''
    Simple Cartesian coordinate on a square grid.
    '''
    def __init__(self, x, y, grid=None):
        self.x = x
        self.y = y
        self._grid = grid


    def __add__(self, right):
        return Coord(self.x + right.x, self.y + right.y, self._grid)
    

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)


    def __eq__(self, other):
        # The grid is only for helper functions, so it doesn't matter for
        # equality.
        return self.x == other.x and self.y == other.y
    

    def __hash__(self):
        # See __eq__.
        return hash((self.x, self.y))
    

    def negate(self):
        return Coord(-self.x, -self.y, self._grid)


    def is_bounded(self):
        '''
        Helper function to tell if bounded by a the square grid.
        '''
        if not grid:
            raise Exception('No grid given.')
        return 0 <= self.x < len(self._grid[0]) and \
               0 <= self.y < len(self._grid)


    def char_at(self):
        '''
        Helper function to get the character at the coord in the grid.
        '''
        if not grid:
            raise Exception('No grid given.')
        return self._grid[self.y][self.x]


def solve(grid):
    '''
    Solves day 19.
    The key insight for this problem is that the direction of the pipes
    actually doesn't matter; we just care about non-whitespace characters. But
    if it was a fluke and I passed my test case on accident, accounting for
    this isn't too difficult.
    '''
    left, right, up, down = Coord(-1, 0), Coord(1, 0), Coord(0, -1), Coord(0, 1)
    loc = Coord(0,0,grid)
    direction = None 
    for index, let in enumerate(grid[0]):
        if let == '|':
            loc.x = index
            direction = down
            break
        if let == '-':
            loc.x = index
            direction = right
            break
    letts = ''
    steps = 1
    while True:
        new_loc = loc + direction
        if new_loc.is_bounded() and new_loc.char_at() != ' ':
            steps += 1
            loc = new_loc
            if loc.char_at() in string.ascii_uppercase:
                letts += loc.char_at() 
        else:
            # If our location is unbounded or hits a space, we want to try to
            # move any direction except backwards.
            direction_changed = False
            bwds_dir = direction.negate()
            # Iterate through all of the possible forwards directions.
            for d in {left, right, up, down} - {bwds_dir}:
                new_loc = loc + d
                # If a valid one is found, set the direction to the direction
                # going that way.
                if new_loc.is_bounded() and new_loc.char_at() != ' ': 
                    direction = d
                    direction_changed = True
            # If we can't switch to a new direction, then we've reached the end.
            if not direction_changed:
                return letts, steps
                break


if __name__ == '__main__':
    grid = [line for line in sys.stdin]
    print(solve(grid))
