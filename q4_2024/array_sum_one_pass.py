"""
DCP: 560

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""

nums = [10, 15, 3, 7]
k = 17

nums2 = [10, 15,3, 10]
k2 = 20

def is_sum_possible(nums, k):
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if (nums[i] + nums[j] == k):
                print("True")
                print(nums[i])
                print(nums[j])
                break

    # Single Pass
    nums_set = set()
    for i in range(0, len(nums)):
        diff = k - nums[i]
        if diff in nums_set:
            print("True")
            return True
        else:
            nums_set.add(diff)
    print("False - Not Possible")
    return False

is_sum_possible(nums, k)
is_sum_possible(nums2, k2)