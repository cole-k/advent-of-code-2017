import sys, re
from collections import defaultdict


def get_state(line):
    # The first capital from the back is the desired capital.
    line = ''.join(list(reversed(line)))
    return re.search('[A-Z]', line)[0]


def get_number(line):
    # Just extract the number from the line.
    return int(re.search(r'\d+', line)[0])


def get_direction(line):
    # Extract 'left' or 'right'.
    return re.search('left|right', line)[0]


def get_input(f):
    blueprint = {}
    start_state = get_state(f.readline())
    num_steps = get_number(f.readline())
    # Continually consume the newline.
    while f.readline():
        state = get_state(f.readline())
        blueprint[state] = {}
        for _ in range(2):
            condition = get_number(f.readline())
            write_val = get_number(f.readline())
            direction = 1 if get_direction(f.readline()) == 'right' else -1
            next_state = get_state(f.readline())
            blueprint[state][condition] = (write_val, direction,
                next_state)
    return blueprint, start_state, num_steps
        

def solve(blueprint, start_state, iterations):
    state = start_state
    tape = defaultdict(int)
    position = 0
    for _ in range(iterations):
        write_val, direction, next_state = blueprint[state][tape[position]]
        if write_val == 0:
            del tape[position]
        else:
            tape[position] = write_val
        position += direction
        state = next_state
    return sum(tape.values())

if __name__ == '__main__':
    blueprint, start_state, num_steps = get_input(sys.stdin)
    print(solve(blueprint, start_state, num_steps))
