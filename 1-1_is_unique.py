"""
1.1 Is Unique
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

str_a = 'tensorflow'
str_b = 'pytorch'

def brute_force(str_input):
    for i, char1 in enumerate(str_input):
        for j, char2 in enumerate(str_input):
            if i==j:
                pass
            elif char1==char2:
                return False
    return True

def optimized(str_input):
    ascii_array = [True]*128 # True means unique
    for char in str_input:
        index = ord(char)
        #print(char, ord(char), ascii_array[index])
        if not ascii_array[index]: # If not unique
            return False
        else:
            ascii_array[index]=False
    return True


if __name__=='__main__':
    print(optimized(str_a))
    print(optimized(str_b))


