"""
This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, 
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False

"""

nums1 = [2, 0, 1, 0]

nums2 = [1, 1, 0, 1]

nums3 = [1, 2, 0, 0, 0, 1, 0]

def return_if_end_can_be_reached(nums):
    n = len(nums)
    
    curr_position, last_index = 0, n - 1

    while curr_position < n:
        if curr_position == last_index:
            return True
        elif nums[curr_position] == 0:
            return False
        curr_position += nums[curr_position]

    return False

print(return_if_end_can_be_reached(nums1))

print(return_if_end_can_be_reached(nums2))

print(return_if_end_can_be_reached(nums3))
