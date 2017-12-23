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
    count = 0
    index = 0
    last_played = None
    seen_before = {}
    while index < len(instructions):
        instr, x, y = parse_instruction(instructions[index], regs)
        # The following is a straightforward implementation of the spec given
        # in the problem.
        if instr == 'set':
            regs[x] = y
        if instr == 'sub':
            regs[x] -= y
        if instr == 'mul':
            regs[x] *= y
            count += 1
        if instr == 'jnz':
            if (x not in regs and eval(x) !=0) or (x in regs and regs[x] != 0): 
                index += y
                continue
        index += 1
    return count 


if __name__ == '__main__':
    instructions = [line.rstrip() for line in sys.stdin]
    print(part_one(instructions))
