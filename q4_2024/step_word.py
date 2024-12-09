"""
DCP: 642

A step word is formed by taking a given word, adding a letter, and anagramming the result. 
For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns all valid step words.

"""
import string

word_dict = {'CITE', 'CATE', 'COAT', 'CITA', 'APPEAL', 'APPLES', 'SAPPLE'}

word_1 = 'CAT'
word_2 = 'APPLE'

characters = string.ascii_uppercase

def get_valid_step_words(input_word):
    ip_set = set(input_word)
    valid_step_words = []

    for c in characters:
        for w in word_dict:
            if((ip_set | {c} ) == set(w)):
                valid_step_words.append(w)
    return set(valid_step_words)

print(get_valid_step_words(word_1))
print(get_valid_step_words(word_2))




