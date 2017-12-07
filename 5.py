import sys

def time_to_escape(offsets, part):
    # Copy input.
    offsets = list(offsets)
    pos = ctr = 0
    while 0 <= pos < len(offsets):
        ctr += 1
        old_pos = pos
        pos += offsets[pos]
        # For part 1, you don't care about the value.
        if part == 1:
            offsets[old_pos] += 1
        # For part 2, you do.
        elif part == 2:
            if offsets[old_pos] >= 3:
                offsets[old_pos] -= 1
            else:
                offsets[old_pos] += 1
        else:
            raise Exception('invalid part')
    return ctr 

inp = [int(line.strip()) for line in sys.stdin]
print(time_to_escape(inp, 1))
print(time_to_escape(inp, 2))
