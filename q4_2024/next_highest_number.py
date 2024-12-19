"""
Given an integer, find the next permutation of it in absolute order. 
For example, given 48975, the next permutation would be 49578.
47958 -> 
45789 -> 47589


"""

import itertools

num1 = 48975

num2 = 23

num3 = 438

num4 = 566

def return_next_highest_number(num):
    num_arr = list(str(num))
    new_num_arr = []
    new_num_perms = list(itertools.permutations(num_arr))
    for t in new_num_perms:
        new_num = "".join(list(t))
        new_num_arr.append(int(new_num))

    diff_dict = {}
    next_perm_highest_num = 0
    for new_num in new_num_arr:
        diff = new_num - num
        if diff > 0:
            diff_dict[new_num] = diff

    next_perm_highest_num = min(diff_dict, key=diff_dict.get)
        
    return next_perm_highest_num


"""
num1 = 48975
num2 = 23
num3 = 438
num4 = 566
"""
"""
print(return_next_highest_number(num1))
print(return_next_highest_number(num2))
print(return_next_highest_number(num3))
print(return_next_highest_number(num4))

"""
def next_highest_permutation(N):
    N = str(N)
    if len(N) == 1:
        return "Not Possible"

    i = len(N) - 1

    while i > 0:
        if N[i] > N[i-1]:
            break
        i -= 1
    
    if i == 0:
        return "Not Possible"
    
    # At this point i contains the index where the increasing order breaks
    # N[i-1] is smaller than N[i] at this point
    # Compare N[i-1] with N[-1] to see which should come first
    #Return value consists of 3 parts
    # N[0:i-1] the first part which will remain untouched
    # N[i-1] followed by N[-1] or the other way around depending on which is smaller
    # N[i:end] where sort order did not break
    s = N[i-1] + N[-1] if N[i-1] > N[-1] else N[-1] + N[i-1]
    #return N[0:i-1] + s + N[i:len(N) - 1]
    
    for j in range(len(N)-1, i-1, -1):
        if N[i-1] < N[j]:
            N = list(N)
            N[j], N[i - 1] = N[i - 1], N[j]
            N = ''.join(N)
            break
    
    # Reverse the digits after (i-1) because the digits after (i-1) are in decreasing order
    # and thus we will get the smallest element possible from these digits
    N = list(N)
    print(N)
    print(i)
    N[i:] = reversed(N[i:])
    N = ''.join(N)

    return N
    

print(next_highest_permutation(218765))
#print(return_next_highest_number(218765))

print(next_highest_permutation(23))
#print(next_highest_permutation(32))

print(next_highest_permutation(76534))


        
    