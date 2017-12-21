from collections import Counter, defaultdict
from functools import reduce
import sys, itertools
import numpy as np

def match(a, d):
    temp = a[:]
    for _ in range(4):
        hashable = tuple(map(tuple,temp))
        if hashable in d:
            return d[hashable]
        flipped = np.flip(temp, 1)
        hashable_flipped = tuple(map(tuple,flipped))
        if hashable_flipped in d:
            return d[hashable_flipped]
        temp = np.rot90(temp)
    return False

size_two = {}
size_three = {}
for line in sys.stdin:
    a, _, b = line.rstrip().split(' ')
    a, b = a.split('/'), b.split('/')
    a, b = tuple(map(tuple, a)), tuple(map(tuple, b))
    if len(a) == 2:
        size_two[a] = b
    if len(a) == 3:
        size_three[a] = b

fractal = np.array(list('.#...####'))
fractal.shape = (3,3)

for i in range(5):
    print(i)
    if len(fractal) % 2 == 0:
        new_fractal = [] 
        for i in range(len(fractal) // 2):
            new_row = [] 
            for j in range(len(fractal) //2):
                s = fractal[2*i:2*i+2,2*j:2*j+2]
                s = tuple(map(tuple,s))
                m = match(s,size_two)
                if not m:
                    print('failure')
                if j == 0:
                    new_row = m
                else:
                    new_row = np.concatenate((new_row, m), axis=1)
            if i == 0:
                new_fractal = new_row
            else:
                new_fractal = np.concatenate((new_fractal, new_row), axis=0)
        fractal = np.array(new_fractal)

    elif len(fractal) % 3 == 0:
        new_fractal = [] 
        for i in range(len(fractal) // 3):
            new_row = [] 
            for j in range(len(fractal) //3):
                s = fractal[3*i:3*i+3,3*j:3*j+3]
                s = tuple(map(tuple,s[:]))
                m = match(s,size_three)
                if not m:
                    print('failure')
                if j == 0:
                    new_row = m
                else:
                    new_row = np.concatenate((new_row, m), axis=1)
            if i == 0:
                new_fractal = new_row
            else:
                new_fractal = np.concatenate((new_fractal, new_row), axis=0)
        fractal = np.array(new_fractal)

print(sum(sum(fractal == '#')))
