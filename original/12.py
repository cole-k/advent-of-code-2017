from collections import defaultdict, Counter
import numpy as np

def dfs_count(adj, start, seen = set()): 
    if start in seen:
        return 0
    else:
        seen.add(start)
        return 1 + sum([dfs_count(adj, child, seen) for child in adj[start]])

def dfs(adj, start, seen = set()): 
    if start in seen:
        return seen
    else:
        seen.add(start)
        for child in adj[start]:
            dfs(adj, child)
        return seen 

with open('12.in') as inp:
    adj = defaultdict(set)
    for line in inp.readlines(): 
        start, nodes = line.strip().split(' <-> ')
        adj[start] = set(nodes.split(', '))
        for node in adj[start]:
            adj[node].add(start)
    # print(dfs_count(adj, '0')) 
    print(adj)
    total_sets = set()
    for start in adj.keys():
        total_sets.add(frozenset(dfs(adj, start)))
    print(len(total_sets))
