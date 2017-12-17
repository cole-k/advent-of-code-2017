def part_one(num_steps, end=2017):
    '''
    Returns the value after the last inserted value in the buffer.
    '''
    buff = [0]
    curr_pos = 0
    for i in range(1, end + 1):
       curr_pos += num_steps
       # The array grows exactly with i.
       curr_pos %= i
       buff.insert(curr_pos, i)
       curr_pos += 1
    # Return the value after the last inserted value.
    return buff[curr_pos % len(buff)]


def part_two(num_steps, end=50*10**6):
    '''
    Returns the value after zero in the buffer after all iterations.
    '''
    value_after_zero = None
    curr_pos = 0
    for i in range(1, end + 1):
        curr_pos += num_steps
        curr_pos %= i
        # We only care about updating the value that comes after zero.
        if curr_pos == 0:
            value_after_zero = i
        curr_pos += 1
    return value_after_zero

print(part_one(316))
print(part_two(316))
