with open('9.in') as inp:
    garbage = False
    garbage_count = score = level = 0
    # The iterator is used to skip characters preceded by a '!'.
    stream = iter(inp.read())
    for character in stream:
        # Skip one character after '!'.
        if character == '!':
            # Consume the next character.
            next(stream,None)
            continue
        if garbage:
            # Stop parsing garbage after '>'.
            if character == '>':
                garbage = False
            else:
                garbage_count += 1
        else:
            # Start parsing garbage after '<'.
            if character == '<':
                garbage = True
            # Go one level deeper if in '{'.
            if character == '{': 
                level += 1
            # Go one level up if a '}' is met, and add the score of the pair.
            if character == '}': 
                score += level
                level -= 1
    print(score, garbage_count)

