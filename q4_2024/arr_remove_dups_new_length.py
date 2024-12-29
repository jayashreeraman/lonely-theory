"""
Given a sorted list of numbers, remove duplicates and return the new length. 
You must do this in-place and without using extra memory.

Input: [0, 0, 1, 1, 1, 2, 2].

Output: 3.

Your function should modify the list in place so that the first three elements become 0, 1, 2. 
Return 3 because the new length is 3.


"""

nums = [0, 0, 1, 1, 1, 2, 2]

def remove_dups_return_new_len(nums):
    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1

print(remove_dups_return_new_len(nums))