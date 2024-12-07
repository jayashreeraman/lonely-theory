"""
Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

FOAM --> True
MASS --> TRUE
SEAL --> False
"""

mat = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
]

words_arr = ['FOAM', 'MASS', 'SEAL']

def check_word_in_mat(word):
    int_words = []
    for i in range(0, len(mat)):
        int_word = "".join(l for l in mat[i])
        int_words.append(int_word)
    
    transposed = list(zip(*mat))
    
    
    for i in range(0, len(transposed)):
        int_word = "".join(l for l in transposed[i])
        int_words.append(int_word)
    
    if word in int_words:
        return True
    else: 
        return False

    """
    Alternate , without zip()
    s={}
    for j in range(0, len(mat)):
        for i in range(0, len(mat)):
            if i not in s:
                s[i]=mat[j][i]
            else:
                s[i] += (mat[j][i])
    print(s.values())
    
    """
    

print(check_word_in_mat('FOAM'))
print(check_word_in_mat('MASS'))
print(check_word_in_mat('ABNA'))
print(check_word_in_mat('ACME'))
#for word in words_arr:

