"""
Given a list of possibly overlapping intervals, 
return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

"""



#input_arr = [(1, 3), (5, 8), (4, 10), (6,9), (20, 25)]

input_arr = [(1, 3), (7, 8), (4, 6), (6,9), (20, 25)]

# Converting i/p to list of lists - for easy reassignment
input_sorted = [list(i) for i in input_arr]
input_sorted.sort(key=lambda interval: interval[0])

merged_list = [input_sorted[0]]

for current in input_sorted:
    previous = merged_list[-1]
    if current[0] <= previous[1]:
        print(current[0])
        previous[1] = max(previous[1], current[1])
    else:
        merged_list.append(current)

# Converting o/p to list of tuples
merged_list = [tuple(i) for i in merged_list]
print(merged_list)
