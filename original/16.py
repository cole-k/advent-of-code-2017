import sys

def spin(n, l):
    return l[-n:] + l[:-n]

def swap(a, b, l):
    l[a], l[b] = l[b], l[a]
    return l

def swap_names(a, b, l):
    a = l.index(a)
    b = l.index(b)
    return swap(a, b, l)

for line in sys.stdin:    
    iterations = 1*(10**9) - 1
    i = 0
    l = list('abcdefghijklmnop')
    ordered_outputs = []
    while True:
        commands = line.rstrip().split(',')
        for command in commands:
            comm, args = command[0], command[1:].split('/')
            if comm == 's':
                l = spin(int(args[0]), l)
            if comm == 'x':
                l = swap(int(args[0]), int(args[1]), l)
            if comm == 'p':
                l = swap_names(args[0], args[1], l)
        output = ''.join(l)
        if output in ordered_outputs:
            index = iterations % i
            print(ordered_outputs[index])
            print(index, ordered_outputs[index-1], ordered_outputs[index + 1])
        ordered_outputs.append(output)
        i += 1
        if i > iterations:
            break
    print(''.join(l))
