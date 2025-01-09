"""
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits 
and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

"""

from itertools import count


input_str = "AAAABBBCCDAA"

def encode_rle(s):
    rle_str = ""
    counter = 1
    char = ""

    for i in range(len(s)-1):
        char = s[i]
        
        if s[i+1] == s[i]:
            counter +=1
        else:
            rle_str += str(counter) + str(char)
            char = s[i+1]
            counter = 1 
    rle_str += str(counter) + str(char)
        
    return rle_str

print(encode_rle(input_str))

rle_str = encode_rle(input_str)

def decode_rle(s):
    output = ""
    for i in range(0, len(s), 2):
        counter = int(s[i])
        char = s[i+1]

        for j in range(counter):
            output += str(char)

    print(output)
    return output

decode_rle(rle_str)

