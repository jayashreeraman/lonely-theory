"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

"""

lst = [-10, -10, 5, 2]

lst_sorted = sorted(lst)
print(lst_sorted)

max_prod = max((lst_sorted[-1]*lst_sorted[-2]*lst_sorted[-3]), (lst_sorted[0]*lst_sorted[1]*lst_sorted[-1]))
print(max_prod)
    

