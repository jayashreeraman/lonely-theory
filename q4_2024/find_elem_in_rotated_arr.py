"""
An sorted array of integers was rotated an unknown number of times.
Given such an array, find the index of the element in the array in faster than linear time. 
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.

"""

nums = [13, 18, 25, 2, 8, 10]
n = 8

def find_index_of_elem(nums, n):

    lo = 0
    hi = len(nums) - 1

    while lo <= hi:

        mid = lo + (hi - lo)//2

        if nums[mid] == n:
            return mid
        
        # If Left Half is sorted
        if nums[mid] >= n:
            if n >= nums[lo] and n < nums[mid]:
                hi = mid - 1

            else:
                lo = mid + 1


        else:
            if n < nums[mid] and n <= nums[hi]:
                lo = mid+1
            else:
                hi = mid - 1

    # If n not found 
    return -1

print(find_index_of_elem(nums, n))
