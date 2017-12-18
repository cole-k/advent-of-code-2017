import sys, string


def parse_instruction(instruction, regs):
    '''
    Return the value of X and Y from the instruction.
    Input is of the form 'instr X [Y]' where Y is optional.
    '''
    instr, *args = instruction.split() 
    x = args[0]
    # If we're given a Y value.
    y = None
    if len(args) > 1:
        # Check if it's a register value and assign it to that value if so.
        if args[1] in regs: 
            y = regs[args[1]]
        # Otherwise, treat it as a string.
        else:
            y = eval(args[1])
    return instr, x, y
    

def part_one(instructions):
    regs = {key:0 for key in string.ascii_lowercase}
    index = 0
    last_played = None
    while index < len(instructions):
        instr, x, y = parse_instruction(instructions[index], regs)
        # The following is a straightforward implementation of the spec given
        # in the problem.
        if instr == 'snd':
            last_played = regs[x] 
        if instr == 'set':
            regs[x] = y
        if instr == 'add':
            regs[x] += y
        if instr == 'mul':
            regs[x] *= y
        if instr == 'mod':
            regs[x] %= y
        if instr == 'rcv' and regs[x] != 0:
            regs[x] = last_played
            return last_played
        if instr == 'jgz' and regs[x] > 0:
            index += y
            # Avoid incrementing the index.
            continue
        index += 1


def part_two(instructions):
    regs_list = [{key:0 for key in string.ascii_lowercase} for _ in range(2)]
    # ID of program 1 is 1.
    regs_list[1]['p'] = 1
    indices = [0, 0]
    waiting = [False, False]
    queues = [[], []]
    times_sent_from_one = 0
    while not all(waiting):
        for program in range(2):
            regs, index, queue = regs_list[program], indices[program], \
                                 queues[program]
            # I mean ... it works.
            other_program = not program
            instr, x, y = parse_instruction(instructions[index], regs)
            if instr == 'snd':
                if x in regs:
                    queues[other_program].append(regs[x])
                else:
                    queues[other_program].append(eval(x))
                if program == 1:
                    times_sent_from_one += 1
            if instr == 'set':
                regs[x] = y
            if instr == 'add':
                regs[x] += y
            if instr == 'mul':
                regs[x] *= y
            if instr == 'mod':
                regs[x] %= y
            if instr == 'rcv': 
                if queue:
                    regs[x] = queue.pop(0)
                    waiting[program] = False 
                else:
                    waiting[program] = True
                    # Avoid incrementing the index.
                    continue
            if instr == 'jgz':
                if x in regs:
                    x = regs[x]
                else:
                    x = eval(x)
                if x > 0:
                    indices[program] += y
                    # Avoid incrementing the index.
                    continue
            indices[program] += 1
    return times_sent_from_one
            

if __name__ == '__main__':
    instructions = [line.rstrip() for line in sys.stdin]
    print(part_one(instructions))
    print(part_two(instructions))
