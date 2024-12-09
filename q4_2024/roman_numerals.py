"""
DCP: 617

Given a number in Roman numeral format, convert it to decimal.
{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.

"""

roman_dict = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def convert_roman_to_int(roman_repr):
    res = 0
    roman_repr = list(roman_repr)

    res = roman_dict[roman_repr[-1]]
    for i in range(len(roman_repr)-2, -1, -1):
        if roman_dict[roman_repr[i]] < roman_dict[roman_repr[i+1]] :
            res -= roman_dict[roman_repr[i]]
        else:
            res += roman_dict[roman_repr[i]]
    print(res)
    return res

convert_roman_to_int('XXVIV')

