"""
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

"""

char_dict = dict()

s1='abc'
s2='bcd'

s3='foo'
s4='bar'

s5 ='lee'
s6='poo'

def get_one_to_one_mapping(s1, s2):
    for char1, char2 in zip(s1, s2):
        if char1 not in char_dict.keys():
            char_dict[char1] = char2
        else:
            if char_dict[char1] != char2:
                return False
    return True                

print(get_one_to_one_mapping(s1, s2))
print(get_one_to_one_mapping(s3, s4))
print(get_one_to_one_mapping(s5, s6))