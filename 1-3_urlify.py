"""
1.3 URLify
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the 'true' length of the string.
(Note: if implementing in Java, please use a character array so that you can perform this operation
in place.)

EXAMPLE
Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
"""

"""
Technique used: Edit a string starting from the end and working backwards.
(Commonly used in string manipulation)
"""

str_input = "Mr John Smith    "
true_length = 13

def brute_force(str_input, true_length):
    """
    This is the "brute force" method because of space complexity rather than time complexity.
    Another string needs to be created here rather than being modified in-place.
    """
    str_output = ""
    for char in str_input:
        if char!=" ":
            str_output += char
        elif len(str_output) >= true_length:
            return str_output
        else:
            str_output += "%20"
    return str_output

def optimized(str_input, true_length):

    # this chunk of code scans the string once to find the number of spaces in between
    num_spaces_total = 0
    for char in str_input:
        if char==" ":
            num_spaces_total += 1
    num_spaces_between = int(num_spaces_total/3)    # because "%20" has 3 characters

    idx_new = true_length + 2*num_spaces_between - 1 # need to increase from 1 to 3 spaces
    
    # this chunk replaces a space when we see it
    str_input = list(str_input)                     # python string is immutable
    for idx_old in range(true_length-1, -1, -1):
        if str_input[idx_old] == " ":
            str_input[idx_new] = "0"
            str_input[idx_new-1] = "2"
            str_input[idx_new-2] = "%"
            idx_new -= 3
        else:    
            str_input[idx_new] = str_input[idx_old]
            idx_new -= 1
    
    str_input="".join(str_input)

    return str_input

if __name__=="__main__":
    print(optimized(str_input, true_length))
    print(brute_force(str_input, true_length))