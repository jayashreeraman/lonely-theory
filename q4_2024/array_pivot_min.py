"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.

"""

nums = [5, 7, 10, 3, 4]

nums_v2 = [5, 6, 1, 2, 3, 4]

# O(N)
def get_min_rotated_arr(nums):
    min_val = nums[0]
    for n in nums:
        min_val = min(n, min_val)

    return min_val

print(get_min_rotated_arr(nums))

# O(log N)

def get_min_rotated_arr_faster(nums):
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        if nums[lo] < nums[hi]:
            return nums[lo]

        mid = (lo + hi)//2

        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid

    return nums[lo]

print(get_min_rotated_arr_faster(nums_v2))
