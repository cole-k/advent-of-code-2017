from collections import defaultdict
state = 'A'
steps = 12261543

# Yup. Hardcoded. If I hadn't made very small mistake (just in the
# beginning part) I probably would've placed. If I hadn't
# hardcoded I probably would've placed. Such is life.
states = {'A':{0:(1,1,'B'), 1:(0,-1,'C')},
          'B':{0:(1,-1,'A'), 1:(1,1,'C')},
          'C':{0:(1,1,'A'),  1:(0,-1,'D')},
          'D':{0:(1,-1,'E'), 1:(1,-1,'C')},
          'E':{0:(1,1,'F'),  1:(1,1,'A')},
          'F':{0:(1,1,'A'),  1:(1,1,'E')}}
tape = defaultdict(int)
position = 0
for _ in range(steps):
    write_val, direction, next_state = states[state][tape[position]]
    if write_val == 0:
        del tape[position]
    else:
        tape[position] = write_val
    position += direction
    state = next_state
tot = 0
for val in tape.values():
    tot += val
print(tot)
