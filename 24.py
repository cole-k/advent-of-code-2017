import sys


def part_one(connecting_value, ports):
    valid_ports = (port for port in ports if connecting_value in port)
    
    max_length = 0
    for a, b in valid_ports:
        next_value = None
        if a == connecting_value:
            next_value = b
        else:
            next_value = a
        next_length = part_one(next_value, ports - {(a,b)})
        next_length += a + b 
        max_length = max(max_length, next_length)
    return max_length 


def part_two(connecting_value, ports, depth=0):
    valid_ports = (port for port in ports if connecting_value in port)
    
    # (max strength, length)
    max_strength = (depth,0)
    for a, b in valid_ports:
        next_value = None
        if a == connecting_value:
            next_value = b
        else:
            next_value = a
        next_depth, next_length = part_two(next_value, ports - {(a,b)},depth + 1)
        next_length += a + b 
        max_strength = max(max_strength, (next_depth, next_length))
    return max_strength

if __name__ == '__main__':
    ports = set([tuple(map(int,line.rstrip().split('/'))) for line in
        sys.stdin])

    print(part_one(0, ports))
    print(part_two(0, ports))
