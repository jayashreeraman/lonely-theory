
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

def get_all_tree_paths(root):
    if not root:
        return []

    paths = []
    stack = [(root, [root.val])]

    while stack:
        node, path = stack.pop()

        if not node.left and not node.right:
            paths.append(path)

        if node.left:
            stack.append([node.left, path +[node.left.val]])

        if node.right:
            stack.append([node.right, path +[node.right.val]])

    return paths

def get_paths_recursive(curr_node, path, paths):

    path = path + [curr_node.val]
    if not curr_node.left and not curr_node.right:
        paths.append(path)
        return
    
    if curr_node.left:
        get_paths_recursive(curr_node.left, path, paths)

    if curr_node.right:
        get_paths_recursive(curr_node.right, path, paths)


print(get_all_tree_paths(root))

tree_paths = []
print(get_paths_recursive(root, [], tree_paths))
print(tree_paths)

    

