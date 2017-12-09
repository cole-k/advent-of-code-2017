import collections, itertools
import numpy as np

with open('9.in') as inp:
    for line in inp.readlines():
        line = line.strip()
        flag = False
        sanitized = ''
        score = 0
        level = 0
        flag = False
        gb = 0
        garbage = False
        for i in line: 
            if flag:
                flag = False
                continue
            if i == '!':
                flag = True
                continue
            if i == '{' and not garbage:
                level += 1
            if i == '>':
                garbage = False
            if garbage:
                gb += 1
            if i == '<':
                garbage = True
            if i == '}' and not garbage:
                score += level
                level -= 1
        print(gb)

