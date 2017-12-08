from collections import defaultdict
import numpy as np

with open('8.in') as inp:
    regs = defaultdict(int)
    m = 0
    for line in inp.readlines():
        val, comm, v, p, left, cond, right = line.strip().split(' ')
        if eval(str(regs[left]) + cond + right):
           if comm == 'inc':
               regs[val] += int(v)
           elif comm == 'dec':
               regs[val] -= int(v)
        m = max(m, max(regs.values()))

    print(max(regs.values()))
    print(m)
