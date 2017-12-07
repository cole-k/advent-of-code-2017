import sys
from collections import Counter

def valid_password(pwd, hashfn):
    '''
        Takes a password pwd and "hash" function hashfn that returns a hashable
        value given a string.
    '''
    hashed_words = set()
    for hashed_word in pwd.split(' '):
        hashable = hashfn(hashed_word)
        # If the password has duplicated hashed words, it's invalid.
        if hashable in words: return False
        hashed_words.add(hashable)
    # If the password has no duplicated hashed words, it's valid.
    return True

result_1 = result_2 = 0
identity = lambda x : x
# "Hash" using Counters, which means anagrams hash to the same value.
counter_hash = lambda x: frozenset(Counter(x).items())
for line in sys.stdin: 
    # Passwords need to have no duplicated words.
    result_1 += valid_password(line.strip(), identity)
    # Passwords need to have no duplicated anagrams.
    result_2 += valid_password(line.strip(), counter_hash)

print('Part 1: {}, Part 2: {}'.format(result_1, result_2))
