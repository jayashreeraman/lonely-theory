"""
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""

nums = [3, 4, -1, 1]

def return_first_missing_positive(nums):
    n = len(nums)
    
    for i in range(len(nums)):
        if nums[i] == 1:
            contains_1 = True
        if nums[i] < 0 or nums[i] >= n:
            nums[i] = 1
    print(nums)

    if not contains_1:
        return 1
    

    for i in range(len(nums)):
        val = abs(nums[i])
        if val == n:
            nums[0] = -abs(nums[0])
        if val < n:
            nums[val] = -abs(nums[val])
        
    print(nums)

    for i in range(1, len(nums)):
        if nums[i] > 0:
            return i
    if nums[0] > 0:
        return n
    return n+1


print(return_first_missing_positive(nums))
