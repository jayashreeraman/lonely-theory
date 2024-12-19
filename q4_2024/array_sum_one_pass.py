"""
DCP: 560

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""

nums = [10, 15, 3, 7]
k = 17

def is_sum_possible(nums, k):
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if (nums[i] + nums[j] == k):
                print("True")
                print(nums[i])
                print(nums[j])
                break

    # Single Pass
    for i in range(0, len(nums)):
        diff = k - nums[i]
        if diff in nums:
            print("True")
            print(nums[i])
            print(diff)
            break

is_sum_possible(nums, k)