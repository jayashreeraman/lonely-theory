"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, 
where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. 
That is, no element of nums is included in any of the ranges, and each missing number is covered by 
one of the ranges.

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
Example 2:

Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.


"""

nums = [0,1,3,50,75]
lower = 0
upper = 99

nums2 = [-1]
lower2 = -1
upper2 = -1


nums3 = [0,1,3,50,75]
lower3 = 0
upper3 = 99

# Case 4 -  when lower is more than nums[0] and upper is less than nums[n]

nums4 = [0,1,3,50,75]
lower4 = 0
upper4 = 99

def return_missing_subset_ranges(nums, lower, upper):
    subset_ranges = []

    if nums == []:
        return [lower, upper]
    
    len_nums = len(nums)
    # Append Upper to iterate the array through the upper limit
    """
    Removing this to accommodate Case 4
    nums.insert(0, lower)
    nums.append(upper+1)
    print(nums)
    
    """

    # [3,50,75]
    lower = 1
    upper = 74
    
    if lower < nums[0]:
        subset_ranges.append([lower, nums[0]-1])

    
    for j in range(0, len(nums)-1):
        diff = nums[j+1] - nums[j]
        #diff = nums[j+1] - nums[j]
        #print(diff)
        if diff > 1:
            sub_lower = nums[j] + 1
            sub_upper = nums[j+1] - 1
            subset_ranges.append([sub_lower, sub_upper])
            
    if upper > nums[-1]:
        subset_ranges.append([nums[-1], upper])

    print(subset_ranges)

return_missing_subset_ranges(nums, lower, upper)

#return_missing_subset_ranges(nums2, lower2, upper2)



