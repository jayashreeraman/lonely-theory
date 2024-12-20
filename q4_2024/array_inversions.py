"""
We can determine how "out of order" an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. 
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. 
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). 
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

"""

arr1 = [5, 4, 3, 2, 1]
arr2 = [2, 4, 1, 3, 5]

# O N^2

def return_num_inversions(arr):
    numinv = 0
    inv_elems = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                numinv += 1
                inv_elems.append((arr[j], arr[i]))
    print(inv_elems)
    return numinv

print(return_num_inversions(arr1))

print(return_num_inversions(arr2))
