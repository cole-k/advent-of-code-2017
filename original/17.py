def buffer(num_steps):
    buff = [0]
    last_val = None
    curr_pos = 0
    for i in range(1,50 * 10**6):
       curr_pos += num_steps
       curr_pos %= i
       if curr_pos == 0:
           last_val = i
       prev_pos = curr_pos
       curr_pos += 1
    return last_val


# print(buffer(3))
print(buffer(316))
