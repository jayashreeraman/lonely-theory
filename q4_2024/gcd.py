"""
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14

"""

nums = [42, 56, 14]
nums_v2 = [63, 81, 72, 90]

def get_gcd(x, y):
    while(y):
        x, y = y, x % y
 
    return x

def get_gcd_arr(nums):
    num1 = nums[0]
    num2 = nums[1]

    gcd = get_gcd(num1, num2)

    for i in range(2, len(nums)):
        gcd = get_gcd(gcd, nums[i])
    return gcd

print(get_gcd_arr(nums))
print(get_gcd_arr(nums_v2))