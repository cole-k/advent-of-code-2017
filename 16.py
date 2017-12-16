import sys

def spin(n, l):
    '''
    Put the n last elements at the front.
    Mutates l.
    '''
    l = l[-n:] + l[:-n]
    return l


def swap_indeces(a, b, l):
    '''
    Swap the elements at positions a and b.
    Mutates l.
    '''
    l[a], l[b] = l[b], l[a]


def swap_elements(a, b, l):
    '''
    Swap the elements a and b.
    Mutates l.
    '''
    a,b = l.index(a), l.index(b)
    swap_indeces(a, b, l)


def solve(moves, iterations=(10**9)-1):
    # The current iteration (0-indexed since arrays are 0-indexed).
    iteration = 0
    # A list of the previous results of the dance.
    prev_results = []
    # List of the programs.
    l = list('abcdefghijklmnop')
    while iteration < iterations:
        for move in moves:
            # Moves start with 's', 'x', or 'p' and are followed by
            # up to two arguments separated by a '/'.
            move_name, args = move[0], move[1:].split('/')
            if move_name == 's':
                # s will only have 1 argument: a positive integer.
                l = spin(int(args[0]), l)
            if move_name == 'x':
                # x will have 2 arguments: 2 positive integers.
                swap_indeces(int(args[0]), int(args[1]), l)
            if move_name == 'p':
                # p will have 2 arguments: 2 element names.
                swap_elements(args[0], args[1], l)
        result = ''.join(l)
        if result in prev_results:
            # When we reach a cycle, we can skip to iterations mod the index of
            # the start of the cycle because it'll cycle through the same
            # results over and over again.
            index = iterations % iteration
            # And we don't even need to do any more computations of the dances,
            # since we have all of the possible results stored: we just take
            # the result corresponding to our index.
            return prev_results[index]
        prev_results.append(result)
        iteration += 1
    # If we're unlucky enough to get unique results for all iterations, we'll
    # just have to return the last value of our array.
    return prev_results[-1]


if __name__ == '__main__':
    moves = sys.stdin.read().rstrip().split(',')
    # Part 1.
    print(solve(moves, 1))
    # Part 2.
    print(solve(moves))
