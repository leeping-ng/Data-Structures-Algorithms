"""
1.6 String Compression
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the compressed string would not become smaller than the original string, your method should 
return the original string.
You can assume the string only has uppercase and lowercase letters (a-z).
"""

"""
Technique used: String builder - append to a list and use ''.join(str), instead of str += char as it 
makes copies and takes O(n^2)
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
        if char != prior:
            # when alphabet changes, except first case
            if prior != '':
                str_output += str(count)
            str_output += char
            prior = char
            count = 1
            
        else:
            count += 1
            # when reach the end of string, need to append the count too
            if i == len(str_input)-1:
                str_output += str(count)

    if len(str_output) >= len(str_input):
        return str_input
    else:
        return str_output


def optimized(str_input):
    """
    This is the faster approach as it uses a string builder.
    """
    str_output = []
    prior = ''
    count = 1
    for i, char in enumerate(str_input):
        if char != prior:
            # when alphabet changes, except first case
            if prior != '':
                str_output.append(str(count))
            str_output.append(char)
            prior = char
            count = 1
            
        else:
            count += 1
            # when reach the end of string, need to append the count too
            if i == len(str_input)-1:
                str_output.append(str(count))

    str_output = ''.join(str_output)

    if len(str_output) >= len(str_input):
        return str_input
    else:
        return str_output

if __name__=="__main__":
    print(optimized('aabcccccaaa'))
    print(optimized('abcdefg'))



