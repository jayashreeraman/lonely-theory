"""
Given N boxes containing different number of Books in each box(numBook[i]),
take a minimum number of books from the boxes conditions are such that:


you must take either all or none of the books inside a given box.
you cannot skip taking books from boxes adjacent to each other.
Box1 and 2 can not be skipped but you can skip box 1 and 3.
you must have a minimum number of books in your hand
for example ,if there are 6 boxes and the number of books in box are {7,2,13,12,9,1} 
then the minimum number of books u can take is 15(by skipping box 1,3,5).


0>N>100

numBook[i]<10000
Callback: Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/solutions/773865/a-beginner-s-guide-on-dp-validation-how-to-come-up-with-a-recursive-solution-python-3/

"""

books = [7,2,13,12,9,1]

def return_min_num_books(books):
    
    def dp(n):
        if n < 2:
            return books[n]
        return books[n] + min(dp(n-2), dp(n-1))

    n = len(books)
    return min(dp(n-1), dp(n-2))

print(return_min_num_books(books))

