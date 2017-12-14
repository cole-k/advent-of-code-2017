from functools import reduce

def reverse(l, start, end):
    '''
    Reverse a section of l from start to start + distance. These values
    don't need to be less than the size of the list; they will be modded by its
    size. Mutates l.
    '''
    section = [l[ i % len(l)] for i in range(start, end)]
    r_section = list(reversed(section))
    for i in range(start, end):
        l[i % len(l)] = r_section[i - start]


def knot_hash(lengths, index, skip_size, l):
    '''
    Perform the knot hash (mutates l).
    '''
    for length in lengths:
        # Reverse the section from index to index + length.
        reverse(l, index, index + length)
        # These are per the spec.
        index += skip_size + length
        skip_size += 1
    # Return the new index and skip_size to be reused.
    return index, skip_size


def dense_hash(l):
    '''
    XOR groups of 16 together (len(l) must be a multiple of 16).
    '''
    dh = []
    for i in range(len(l)//16):
        # Reduce by XOR on slices of 16.
        dh.append(reduce(lambda x,y: x^y, l[i*16:(i+1)*16]))
    return dh


def complete_knot_hash(lengths):
    '''
    Computes the full knot hash from part 2 of day 10.
    '''
    # Convert to character codes.
    lengths = list(map(ord, lengths)) 
    # Prepend the values specified in the hash.
    lengths += [17, 31, 73, 47, 23]
    l = list(range(256))
    index = skip_size = 0
    for _ in range(64):
        index, skip_size = knot_hash(lengths, index, skip_size, l) 
    dh = dense_hash(l)
    return dh


def search(x, y, grid, visited):
    '''
    Simple BFS on grid given a set of visited nodes.
    Returns the updated set of visited nodes.
    '''
    q = [(x,y)]
    while q:
        x, y = q.pop(0)
        if (x,y) not in visited:
            visited.add((x,y))
            # Only traverse if it's a used region (represented by a '1').
            if hashes[x][y] == '1':
                # Traversing to adjacent cells in a 2D Cartesian plane means
                # moving 1 in either the x or y direction.
                possibilities = [(0,1), (1,0), (-1,0), (0,-1)]
                for dx, dy in possibilities:
                    # Check that we have the right bounds.
                    if 0 <= dx + x < 128 and 0 <= dy + y < 128:
                        q.append((x + dx, y + dy))
    return visited
        

if __name__ == '__main__':
    string = 'xlqgujun'
    num_used = 0
    grid = []
    
    for i in range(128):
        dh = complete_knot_hash(string + '-' + str(i))
        # Convert each digit to 8 digits in binary and flatten to a single
        # string.
        b = ''.join(list(map('{0:08b}'.format, dh)))
        num_used += sum(map(int,b))
        grid.append(b)
    print(num_used)
    visited = set()
    num_regions = 0
    locations = [(i,j) for i in range(128) for j in range(128)]
    for i,j in locations:
        if (i,j) not in visited and hashes[i][j] != '0':
            visited = search(i, j, hashes, visited)
            num_regions += 1
    print(num_regions)

