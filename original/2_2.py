import sys


def even_division(l):
    for i in l:
        for j in l:
            if i % j == 0 and i != j:
                return i / j


total = 0

for line in sys.stdin:
    row = list(map(int, line.split('\t')))
    total += even_division(row)

print(total)
