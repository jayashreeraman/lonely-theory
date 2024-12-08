"""
DCP 588

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.

"""

import sys

arr_obj = [0,0,0,0,0,0,8,9,0,0,0,0,0,0,0,6,3,0,0,0,0]

class SparseArray:
    def __init__(self, arr, size):
        self.arr = dict.fromkeys(range(size), 0)

    def set_item(self,i, val):
        self.arr[i] = val

    def get(self, i):
        return self.arr[i]

s = SparseArray(arr_obj, len(arr_obj))
s.set_item(6,8)
s.set_item(7,9)
s.set_item(13,6)
s.set_item(14,4)

print(s.get(7))
print(s.get(4))
print(sys.getsizeof(arr_obj))
print(sys.getsizeof(s))