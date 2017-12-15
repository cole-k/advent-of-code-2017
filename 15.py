from itertools import islice
import numpy as np

def gen(start, fac, mult=1):
    '''
    Constructs a generator.
    start: starting value.
    fac: factor to multiply by.
    mult: multiples to return (default 1).
    '''
    curr = start
    # Hardcoded divisor 
    div = 2147483647
    while True:
        curr = (curr * fac) % div 
        if curr % mult == 0:
            yield curr


def solve(a, b, nums=5*10**6, mult_a=4, mult_b=8):
    '''
    a: factor for generator a.
    b: factor for generator b.
    nums: number of iterations (default 5 million).
    mult_a: multiples generator a returns.
    mult_b: multiples generator b returns.
    '''
    # We only want the last 16 bits.
    mask = (2**16) - 1
    count = 0
    gen_a = gen(a, 16807, mult_a)
    gen_b = gen(b, 48271, mult_b)

    for next_a, next_b in zip(islice(gen_a, nums), islice(gen_b, nums)):
        count += (next_a & mask) == (next_b & mask)
    return count

if __name__ == '__main__':
    inp_a = 699
    inp_b = 124
    # Part 1 runs 40 million times and returns all multiples.
    print(solve(inp_a, inp_b, 40*10**6, 1, 1))
    # Part 2 uses the default values.
    print(solve(inp_a, inp_b))
