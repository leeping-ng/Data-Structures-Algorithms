"""
1.5 One Away
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given 2 strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE:
pale,   ple     -> true
pales,  pale    -> true
pale,   bale    -> true
pale,   bake    -> false
"""

"""
Technique used: 2 pointers moving separately across 2 arrays
"""

def optimized(str_a, str_b):
    if abs(len(str_a) - len(str_b))>1:
        return False

    if len(str_a) > len(str_b):
        str_long = str_a
        str_short = str_b
    else:
        str_long = str_b
        str_short = str_a

    idx_short = 0
    idx_long = 0
    diff = 0
    for i in range(len(str_long)):
        # if indexes don't tally, skip one and try again next loop, and record 1 diff
        if str_long[idx_long] != str_short[idx_short]:
            idx_short -= 1
            diff += 1

        if diff > 1:
            return False
        idx_short += 1
        idx_long += 1

    return True

if __name__=="__main__":
    print(optimized('palace', 'place'))
    print(optimized('pale', 'bake'))
    print(optimized('rail', 'liar')) # I forgot this scenario initially

