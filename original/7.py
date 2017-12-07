from collections import defaultdict, Counter
import numpy as np

def sub_sum(nodes, vals, n):
    if n not in nodes:
        return vals[n]
    s = 0
    for node in nodes[n]:
        t = sub_sum(nodes, vals, node)
        s += t
    return s + vals[n]

def traverse(nodes, vals, root):
    ns = []
    sub_sums = []
    c = Counter()
    for node in nodes[root]:
        ss = sub_sum(nodes, vals, node)
        ns.append(node)
        sub_sums.append(ss)
    next_node = None
    for i in range(len(sub_sums)):
        if i < len(sub_sums) - 1 and sub_sums[i] not in sub_sums[0:i] + sub_sums[i+1:]:
            print(root)
            print(sub_sums)
            print(vals[ns[i]])
            next_result = traverse(nodes, vals, ns[i])
            if next_result:
                return next_result
            else:
                return vals[ns[i]] + ((list(set(sub_sums) - {sub_sums[i]})[0]) - sub_sums[i])
        else:
            result = traverse(nodes, vals, ns[i])
            if result:
                return result

with open('7.in') as inp:
    vals = {}
    nodes = defaultdict(list)
    start = set()
    end = set()
    for line in inp.readlines():
        values = line.strip().split(' ')
        vals[values[0]] = int(values[1][1:-1])
        start.add(values[0])
        latter = values[3:]
        if latter:
            for val in map(lambda x: x.strip(','), latter):
                end.add(val)
                nodes[values[0]].append(val)
    root = list(start - end)[0]
    print(root)
    print(traverse(nodes, vals, root))
