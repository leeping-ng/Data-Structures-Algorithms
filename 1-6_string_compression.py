"""
1.6 String Compression
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the compressed string would not become smaller than the original string, your method should 
return the original string.
You can assume the string only has uppercase and lowercase letters (a-z).
"""

def brute_force(str_input):
    """
    This is very slow because in Python, strings are immutable.
    Therefore, before concatenating to it, the characters of the old string need to be copied first.
    Time complexity will be O(n^2)
    """
    str_output = ''
    prior = ''
    count = 1
    for i, char in enumerate(str_input):
        print(i)
        if char != prior:
            # when alphabet changes, except first case
            if prior != '':
                str_output += str(count)
            str_output += char
            print(str_output)
            prior = char
            count = 1
            
        else:
            count += 1
            # when reach the end of string, need to append the count too
            if i == len(str_input)-1:
                str_output += str(count)

    return str_output

if __name__=="__main__":
    print(optimized('aabcccccaaa'))



