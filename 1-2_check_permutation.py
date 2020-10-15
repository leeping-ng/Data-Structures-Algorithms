"""
1.2 Check Permutation
Given two strings, write a method to decide if one is a permutation of the other.
"""

"""
Technique used: Hash table of ascii characters, using ord()
"""

str_a = "iamlordvoldemort"
str_b = "tommarvoloriddle"
str_c = "harrypotter"

def optimized(str_1, str_2):
    if len(str_1) != len(str_2): # if different length it's obviously not permutation
        return False

    ascii_array_1 = [0]*128
    ascii_array_2 = [0]*128
    for char in str_1:
        index = ord(char) # get the ascii value
        ascii_array_1[index] += 1
    
    for char in str_2:
        index = ord(char) # get the ascii value
        ascii_array_2[index] += 1

    for index in range(128):
        if ascii_array_1[index] != ascii_array_2[index]:
            return False

    return True

if __name__ == "__main__":
    print(str_a, str_b, optimized(str_a, str_b))
    print(str_a, str_c, optimized(str_a, str_c))



    

