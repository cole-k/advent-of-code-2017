from collections import Counter, defaultdict
from functools import reduce
import sys, itertools
import numpy as np

def match(a, b):
    temp = a[:]
    for _ in range(4):
        if np.array_equal(temp, b):
            return True
        if np.array_equal(np.flip(temp, 1),b):
            return True
        temp = np.rot90(temp)
    return False

size_two = []
size_three = []
for line in sys.stdin:
    a, _, b = line.rstrip().split(' ')
    a, b = a.split('/'), b.split('/')
    a, b = list(map(list, a)), list(map(list, b))
    if len(a) == 2:
        size_two.append((a,b))
    if len(a) == 3:
        size_three.append((a,b))

fractal = np.array(list('.#...####'))
fractal.shape = (3,3)

for i in range(18):
    print(i)
    if len(fractal) % 2 == 0:
        new_fractal = [] 
        for i in range(len(fractal) // 2):
            new_row = [] 
            for j in range(len(fractal) //2):
                s = fractal[2*i:2*i+2,2*j:2*j+2]
                for m in size_two:
                    if match(s,m[0]):
                        if j == 0:
                            new_row = m[1]
                        else:
                            new_row = np.concatenate((new_row, m[1]), axis=1)
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
                for m in size_three:
                    if match(s,m[0]):
                        if j == 0:
                            new_row = m[1]
                        else:
                            new_row = np.concatenate((new_row, m[1]), axis=1)
            if i == 0:
                new_fractal = new_row
            else:
                new_fractal = np.concatenate((new_fractal, new_row), axis=0)
        fractal = np.array(new_fractal)

print(sum(sum(fractal == '#')))
