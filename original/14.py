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
        dh.append(functools.reduce(lambda x,y: x^y, l[i*16:(i+1)*16]))
    return dh

def search(x,y, hashes, visited):
    q = [(x,y)]
    while q:
        x, y= q.pop()
        if (x,y) not in visited:
            visited.add((x,y))
            if hashes[x][y] == '1':
                possibilities = [(0,1), (1,0), (-1,0), (0,-1)]
                for dx, dy in possibilities:
                    if 0 <= dx + x < 128 and 0 <= dy + y < 128:
                        q.append((x + dx, y + dy))
    return visited
        

with open('14.in') as inp:
    test = 'flqrgnkx'
    s = 'xlqgujun'
    count = 0
    hashes = []
    for i in range(128):
        lengths = list(map(ord, s + '-' + str(i)))
        lengths += [17, 31, 73, 47, 23]
        l = list(range(256))
        index = skip_size = 0
        for _ in range(64):
            index, skip_size = knot_hash(lengths, index, skip_size, l) 
        dh = dense_hash(l)
        b = ''.join(list(map('{0:08b}'.format, dh)))
        count += sum(map(int,b))
        hashes.append(b)
    # print(count)
    visited = set()
    regions = 0
    locations = [(i,j) for i in range(128) for j in range(128)]
    for i,j in locations:
        if (i,j) not in visited and hashes[i][j] != '0':
            visited = search(i, j, hashes, visited)
            regions += 1
    print(regions)

