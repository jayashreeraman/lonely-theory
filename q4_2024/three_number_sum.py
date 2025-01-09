"""
Given an array of numbers and a number k, determine if there are three entries in the array 
which add up to the specified number k. 
For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.

"""

nums = [20, 303, 3, 4, 25]

k = 50

def return_if_three_num_sum_exists(nums, k):
    n = nums[:]
    for i in range(len(n)):
        diff_out = k - n[i]
        
        nums_new = n[0:i] + n[i+1:]
        print(nums_new)
        x = return_if_two_sum_exists(nums_new, diff_out)
        if x:
            return x
    return False

def return_if_two_sum_exists(nums, k):
    """
    for i in range(len(nums)):
        diff = k - nums[i]
        if diff in nums:
            return True
    return False
    
    """
    diff_dict = {}
    for i in range(len(nums)):
        diff = k - nums[i]
        diff_dict[diff] = diff_dict.get(diff, 0) + 1
        #diff_arr.add(k-nums[i])

    for i in range(len(nums)):
        if nums[i] in diff_dict:
            diff_dict[nums[i]] = diff_dict.get(nums[i]) - 1
            if diff_dict[nums[i]] > 0:
                return True
    return False
    

#print(return_if_three_num_sum_exists(nums, k))

print(return_if_two_sum_exists([5,7, 5], 10))