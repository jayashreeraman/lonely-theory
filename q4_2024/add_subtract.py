"""
DCP: 682

Write a function, add_subtract, which alternately adds and subtracts curried arguments. 
Here are some sample operations:

add_subtract(7) -> 7

add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0

add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11

"""

from __future__ import annotations


def add_subtract_str_input(curried_str):
    curried_str_split = curried_str.split(")(")
    #print(curried_str_split)
    curried_str_split[0] = curried_str_split[0].split("(")[1]
    curried_str_split[-1] = curried_str_split[-1].split(")")[0]
    result = int(curried_str_split[0])

    for i in range(1, len(curried_str_split)):
        if i % 2 == 0:
            result += int(curried_str_split[i]) * (-1)
        elif i % 2 == 1:
            result += int(curried_str_split[i])

    return result

class CallableInt(int):
    def __init__(self, value:int) -> None:
        int.__init__(value)
        self.should_add = True

    def update_sign(self, should_add:bool) -> None:
        self.should_add = should_add

    def __call__(self, value:int) -> CallableInt:
        if self.should_add:
            result = CallableInt(self + value)
        else:
            result = CallableInt(self - value)
        result.update_sign(not self.should_add)
        return result

def add_subtract(value: int) -> CallableInt:
    return CallableInt(value)

print(add_subtract(-5)(10)(3)(9))

