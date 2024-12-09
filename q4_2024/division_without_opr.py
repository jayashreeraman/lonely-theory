"""

DCP: 610
Implement division of two positive integers without using the division, multiplication, or modulus operators.
 Return the quotient as an integer, ignoring the remainder.


"""

def divide_wo_opr(dividend,divisor):
    quot = 0
    while dividend >= divisor:
        dividend = dividend - divisor
        quot += 1
    
    return quot

print(divide_wo_opr(20, 5))
print(divide_wo_opr(60, 7))
print(divide_wo_opr(3, 6))
print(divide_wo_opr(90, 10))