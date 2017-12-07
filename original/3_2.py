import sys
import numpy as np


# Way too hacky. Time complexity is bounded by the input size, although at
# least logarithmically (perhaps the bound is even smaller).

def spiral_memory_sum(num):
    # Start with a spiral of size 20, since resizing is nontrivial.
    # Thankfully, it's easy to tell that the values inside the spiral will grow
    # exponentially, so reaching the target is trivial.
    size = 20
    # The spiral.
    spiral = np.zeros((size, size))
    # The origin is at the center of the spiral.
    y = (size - 1) // 2
    x = y
    # Initialize the origin to 1.
    spiral[x][y] = 1
    # Initialize the current odd square.
    curr_odd_sq = 1
    # Initialize the next odd square.
    next_odd_sq_root = 1
    next_odd_sq = next_odd_sq_root ** 2
    # Initialize the counter (this is how we'll determine which direction we
    # move).
    counter = 1
    # We start 1 to the right of it (1,0), so move there.
    while spiral[x][y] < num:
        if counter == next_odd_sq:
            # Once we reach the next odd square, we move to the right one.
            x += 1
            # Change the next odd square and current odd sq.
            curr_odd_sq = next_odd_sq
            next_odd_sq_root += 2
            next_odd_sq = next_odd_sq_root ** 2
            # This is a bit difficult.
            # # If we exceed the size of our array, double the size.
            # if curr_odd_sq > size:
            #     new_size = (size * 2) + 1
            #     # Reshape the matrix
            #     spiral.resize(size, size)
            #     # Reshape x and y
            #     x += new_size - size
            #     y += new_size - size
            #     size = new_size
        elif counter < curr_odd_sq + (next_odd_sq_root - 1):
            # In this case, we move up.
            y += 1
        elif counter < curr_odd_sq + 2*(next_odd_sq_root - 1):
            # In this case, we move left.
            x -= 1
        elif counter < curr_odd_sq + 3*(next_odd_sq_root - 1):
            # In this case, we move down.
            y -= 1
        else:
            # In this case, we move right.
            x += 1
        # Debug.
        # print('Counter: {}, Next_odd_sq: {}'.format(counter, next_odd_sq))
        # print(spiral[x-1:x+2, y-1:y+2])
        # Set the spiral to the sum.
        spiral[x][y] = spiral[x-1:x+2, y-1:y+2].sum()
        # print(spiral)
        # Debug.
        # print('Value at {},{}: {}'.format(x,y,spiral[x][y]))
        # Increment the counter.
        counter += 1 

    return spiral[x][y]


print(spiral_memory_sum(325489))
