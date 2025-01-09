"""
Given an array of integers, return a new array where each element in the new array is 
the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0],


"""

nums = [3, 4, 9, 6, 1]
res = [0] * len(nums)


for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if nums[j] < nums[i]:
            res[i] += 1

print(res)