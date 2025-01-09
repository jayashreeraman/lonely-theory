"""
Given a string with repeated characters, rearrange the string so that no 
two adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.


"""

from heapq import heappush, heappop
from collections import Counter

str1 = "aaabbc"

class Key:
    def __init__(self, character:str, freq: int) -> None:
        self.character = character
        self.freq = freq

    def __lt__(self, other: "Key") -> bool:
        return self.freq > other.freq

# Function to rearrange character of a string
# so that no char repeats twice

def rearrangeString(s: str):
    n = len(s)

    count = dict()

    for i in s:
        count[ord(i)] = count.get(ord(i), 0) + 1

    pq = []
    for c in range(97, 123):
        if count.get(c, 0):
            heappush(pq, Key(chr(c), count[c]))
    
    
    # null char for previous key checking
    prev = Key('#', -1)
    s = ""

    while pq:
        key = heappop(pq)
        s += key.character

        key.freq -= 1

        # avoid adding if count is 0
        if prev.freq > 0:
            heappush(pq, prev)
        prev = key

    if len(s) != n:
        print(s)
        print("Not Possible")
    else:
        print(s)


rearrangeString(str1)