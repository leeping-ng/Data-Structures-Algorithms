"""
1.4 Palindrome Permutation
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: "Tact Coa"
Output: True (permutations: "taco cat", "atco cta" etc)
"""
str_a = "Tact Coa"
str_b = "Permutation"

def optimized(str_a):
    # change to lower case and remove spaces
    str_a = (str_a.replace(' ','')).lower()
    ascii_array = [0]*128
    for char in str_a:
        index = ord(char)
        ascii_array[index] += 1

    # if the number of unique characters that are odd > 1, it is not a palindrome permutation
    odd_count = 0
    for index in range(len(ascii_array)):
        if ascii_array[index]%2==1:
            odd_count +=1
        if odd_count >1:
            return False
    return True


if __name__=="__main__":
    print(optimized(str_a))
    print(optimized(str_b))
