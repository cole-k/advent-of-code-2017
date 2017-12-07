import sys
import math


def spiral_memory(num):
    sqrt = math.floor(math.sqrt(num))
    # Find the first odd square less than the number
    first_odd_square = sqrt - ((sqrt % 2) == 0)
    # We will traverse the spiral starting from the coordinates of this odd
    # square.
    start = (first_odd_square - 1)/2
    x, y = start, -start 
    # The number at (x,y) is the odd number squared. We will traverse past it
    # until we reach num.
    num -= first_odd_square**2
    # Debug print statements.
    # print(x,y)
    # print('num: {}, first_odd_square: {}'.format(num, first_odd_square))
    if num:
        # The first traversal is moving 1 unit to the right.
        x += 1
        num -= 1
    if num:
        # The next traversal is moving odd_square units up.
        diff = min(first_odd_square, num)
        y += diff
        num -= diff
    if num:
        # The third traversal is moving odd_square + 1 units to the left.
        diff = min(first_odd_square + 1, num)
        x -= diff
        num -= diff
    if num:
        # The fourth traversal is moving odd_square + 1 units down.
        diff = min(first_odd_square + 1, num)
        y -= diff
        num -= diff
    if num:
        # The final traversal is moving odd_square units to the right.
        diff = min(first_odd_square, num)
        x += diff
        num -= diff
    return abs(x) + abs(y)


while True:
    try:
        inp = int(input('Integer: '))
        print(spiral_memory(inp))
    except:
        exit(0)
