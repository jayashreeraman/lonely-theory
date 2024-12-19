"""

A girl is walking along an apple orchard with a bag in each hand. 
She likes to pick apples from each tree as she goes along, but is meticulous about not putting 
different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, 
determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, 
with a length of four.

"""

path = [2, 1, 2, 3, 3, 1, 3, 5]

def n_uniq_elems(arr: list):
    return len(list(set(arr)))

def get_longest_apple_path_len(paths):
    path_arr = []

    for i in range(len(paths)):
        for j in range(len(paths)):
            if n_uniq_elems(paths[i:j]) < 3:
                path_arr.append(len(paths[i:j]))
        
    print(path_arr)
    return max(path_arr)

print(get_longest_apple_path_len(path))
