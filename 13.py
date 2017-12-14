def severity(lengths):
    total = 0
    for key in lengths.keys():
        if key % (2 * (lengths[key] - 1)) == 0:
            total += lengths[key] * key
    return total

def does_trigger(lengths, delay):
    for key in lengths.keys():
        if (key + delay) % (2 * (lengths[key] - 1)) == 0:
            return True
    return False

def shortest_delay(lengths):
    '''
    This is a brute force implementation of part 2.
    '''
    delay = 0
    while does_trigger(lengths, delay):
        delay += 1
    return delay

with open('13.in') as inp:
    lengths = {} 
    for line in inp:
        ind, length = map(int,line.strip().split(': '))
        lengths[ind] = length
    # Part 1.
    print(severity(lengths))
    # Part 2.
    print(shortest_delay(lengths))
