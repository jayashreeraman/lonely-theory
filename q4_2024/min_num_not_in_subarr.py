"""
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.

"""

arr = [1, 2, 3, 10]

#arr = [3, 6, 9, 10, 20, 28]


def return_lowest_sum_not_in_array(arr):
    running_sum = 1

    for elem in arr:
        ## Key piece of logic
        if elem <= running_sum:
            running_sum += elem
        else:
            break
    return running_sum
        

print(return_lowest_sum_not_in_array(arr))



