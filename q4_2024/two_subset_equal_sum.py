"""
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, 
since we can split it up into {15, 5, 10, 15, 10}
 and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets 
that add up to the same sum.

"""

ms1 = [15, 5, 20, 10, 35, 15, 10]

ms2 = [15, 5, 20, 10, 35]

def return_if_two_subset_possible(ms):
    
    set_sum = sum(ms)

    if set_sum%2 != 0:
        return False

    target = set_sum/2
    sums = set([0])

    """
    dp = set([0])
    for i in range(len(ms)):
        
        temp_set = set()
        for sum_t in dp:
            if sum_t + ms[i] == target:
                return True
            temp_set.add(sum_t + ms[i])
        dp.update(temp_set)
        print(dp)
    return False
    
    """
    
    # iterate through nums, adding unique sums
    # [15, 5, 20, 10, 35, 15, 10]
    for n in ms:
        for s in sums.copy():
            if s + n <= target:
                print(s+n)
                sums.add(s + n)
        #sums.add(n)
        print(n)
        print(sums)
        # just to save time in case we reach half early
        if target in sums:
            return True
    return False



print(return_if_two_subset_possible(ms1))
print(return_if_two_subset_possible(ms2))
