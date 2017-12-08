from collections import defaultdict

with open('8.in') as inp:
    regs = defaultdict(int)
    max_value = 0
    for line in inp.readlines():
        # Lines look like 'register command value if register condition value'
        reg, comm, val, _, cond_reg, cond, cond_val = line.strip().split(' ')
        # This should be an int, so cast it to one.
        val = int(val)
        # Compare the register in the conditional to the value in the
        # conditional.
        if eval(str(regs[cond_reg]) + cond + cond_val):
            # If the command is 'inc', add the value to the register.
            if comm == 'inc':
                regs[reg] += val
            # If it's 'dec', subtract it.
            elif comm == 'dec':
                regs[reg] -= val
            # Update the maximum value acheived.
            max_value = max(max_value, regs[reg])

    # Part 1.
    print(max(regs.values()))
    # Part 2.
    print(max_value)
