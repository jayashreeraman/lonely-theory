"""
Given a mapping of digits to letters (as in a phone number), and a digit string, 
return all possible letters the number could represent. You can assume each valid number
 in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” 
should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

"""

import itertools

num_alpha_dict = {
                "2": ["a", "b", "c"], 
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"],
                }

def return_alpha_combo(digit):
    parent_list = []
    for d in digit:
        parent_list.append(num_alpha_dict[d])

    #Key piece oflogic
    res = list(itertools.product(*parent_list))
    result = []
    for elem in res:
        result.append("".join(a for a in elem))

    print(result)

return_alpha_combo("23")
return_alpha_combo("789")

    
