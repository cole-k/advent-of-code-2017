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


def to_hexstring(l):
    '''
    Convert a list of values in the range[0,256) to a hexstring.
    '''
    hexstring = ''
    for e in l:
        # Convert to hex and strip the '0x'.
        conv = hex(e).strip('0x')
        # Prepend zero to pad to length 2 if needed.
        if len(conv) < 2:
           conv = '0' + conv 
        hexstring += conv
    return hexstring 


with open('10.in') as inp:
    lengths = list(map(int,inp.read().strip().split(',')))
    l = list(range(256))
    index = skip_size = 0
    knot_hash(lengths,index, skip_size, l)
    print(l[0] * l[1])

with open('10.in') as inp:
    lengths = list(map(ord,inp.read().strip()))
    lengths += [17, 31, 73, 47, 23]
    l = list(range(256))
    index = skip_size = 0
    # Apply the knot hash 64 times.
    for _ in range(64):
        index, skip_size = knot_hash(lengths,index, skip_size, l)
    dh = dense_hash(l)
    print(to_hexstring(dh))
