from collections import defaultdict, Counter
from functools import reduce
import itertools
import numpy as np

# Note: This only solves part 2. It was modified from part 1.

def gen(start, fac, mult):
    prev = start
    div = 2147483647
    while True:
        curr = (prev * fac) % div
        if curr % mult == 0:
            yield curr
        prev = curr

with open('15.py') as inp:
    inp_a = 699
    inp_b = 124
    # inp_b = 8921
    # inp_a = 65
    gen_a = gen(inp_a, 16807, 4)
    gen_b = gen(inp_b, 48271, 8)
    div = (2**16) - 1
    count = 0
    for _ in range(5*(10**6)):
        next_a, next_b = next(gen_a), next(gen_b)
        count += (next_a & div) == (next_b & div)
    print(count)
