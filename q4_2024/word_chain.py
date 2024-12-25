"""
Given a list of words, determine whether the words can be chained to form a circle. 
A word X can be placed in front of another word Y in a circle if the last character of X 
is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can form the following circle: 
chair --> racket --> touch --> height --> tunic --> chair


"""
words = ['chair', 'height', 'racket', 'touch', 'tunic']

def is_word_circle_possible(words):
    #start_word = words[0]
    #start_char = start_word[0:1]
    len_lst = len(words)

    emp_lst = []

    for w in words:
        start_char = w[0:1]
        #print(w)
        if w.startswith(start_char):
            emp_lst.append(w)
            #words.remove(w)
            start_char = w[0:1]
        else:
            print("Not possible")
    len_new_words = len(emp_lst)
    print(len_new_words)
    if len_new_words == len_lst:
        print("Word Chain Possible")

is_word_circle_possible(words)
