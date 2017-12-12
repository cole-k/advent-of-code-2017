from collections import defaultdict

def count_connected(adj, start, seen=set()): 
    '''
    Counts the number of nodes connected to start.
    '''
    if start in seen:
        return 0
    else:
        seen.add(start)
        return 1 + sum([count_connected(adj, child, seen) for child in
                        adj[start]])

def connected_group(adj, start, seen=set()): 
    '''
    Returns the set of nodes connected to start.
    '''
    if start in seen:
        return seen
    else:
        seen.add(start)
        for child in adj[start]:
            # This actually isn't necessary by virtue of how optional
            # parameters work in Python, but it's better to be explicit.
            seen = connected_group(adj, child, seen)
        return seen 

with open('12.in') as inp:
    # Adjacency list of the form {node: set(children)}.
    adj = defaultdict(set)
    for line in inp:
        start, nodes = line.strip().split(' <-> ')
        adj[start] = set(nodes.split(', '))
        # This graph is bidirectional, so update the adjacency list for the
        # children, too.
        for node in adj[start]:
            adj[node].add(start)
    # Part 1.
    print(count_connected(adj, '0')) 
    groups = set()
    # Find the connected groups starting from each node.
    for start in adj.keys():
        # Sets aren't hashable, so use frozenset.
        groups.add(frozenset(connected_group(adj, start)))
    # Part 2.
    print(len(groups))
