"""
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

"""

str1 = "acbbac"

str2 = "abcdef"

def return_first_recurring_char(s):
    cdict = {}
    for c in s:
        if c in cdict:
            return c
        else:
            cdict[c] = 1
            
    return None

print(return_first_recurring_char(str1))

print(return_first_recurring_char(str2))