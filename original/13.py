from collections import Counter, defaultdict
import itertools, functools
import numpy as np

with open('13.in') as inp:
    l = {} 
    for line in inp:
        ind, length = map(int,line.strip().split(': '))
        l[ind] = length
    triggered = True 
    delay = -1
    while triggered:
        triggered = False
        total = 0
        for key in l.keys():
            if (key + delay) % (2 * (l[key] - 1)) == 0:
                triggered = True
                total += l[key] * key
        delay += 1
    print(total)
    print(delay - 1)
