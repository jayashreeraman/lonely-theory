"""
Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

"""

s = "hello world here"


# option 1
print(" ".join(s.split(" ")[::-1]))

# option 2
print(" ".join(reversed(s.split())))

