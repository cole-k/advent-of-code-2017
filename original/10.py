from functools import reduce

def reverse(l, start, distance):
    section = [l[ i % len(l)] for i in range(start, start + distance)]
    r_section = list(reversed(section))
    for i in range(start, start + distance):
        l[i % len(l)] = r_section[i - start]


def solve(lengths, index, skip_size, l):
    for length in lengths:
        reverse(l, index, length)
        index += skip_size + length
        skip_size += 1
    return index, skip_size


# with open('10.in') as inp:
#     lengths = list(map(int,inp.read().strip().split(',')))
#     l = list(range(256))
#     l = list(range(5))
#     index = skip_size = 0
#     index, skip_size = solve(lengths,index, skip_size, l)
#     print(l[0] * l[1])

with open('10.in') as inp:
    for line in inp.readlines():
        lengths = list(map(ord,line.strip()))
        lengths += [17, 31, 73, 47, 23]
        l = list(range(256))
        index = skip_size = 0
        for _ in range(64):
            index, skip_size = solve(lengths,index, skip_size, l)
        dense_hash = []
        for i in range(16):
            dense_hash.append(reduce(lambda x,y: x^y, l[i*16:(i+1)*16]))
        output = ''
        for h in dense_hash:
            conv = hex(h)[2:]
            if len(conv) < 2:
               conv = '0' + conv 
            output += conv
        print(output)
