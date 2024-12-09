
"""

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35


"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Key Function
def find_parent(root, node):
    if root is None:
        return None

    # If the node is the root, it has no parent
    if root == node:
        return None

    # Search in the left subtree
    if node.val < root.val:
        parent = find_parent(root.left, node)
        if parent is None and root.left == node:
            return root
        else:
            return parent

    # Search in the right subtree
    else:
        parent = find_parent(root.right, node)
        if parent is None and root.right == node:
            return root
        else:
            return parent

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(30)

root.right.left = TreeNode(22)
root.right.right = TreeNode(35)


root.right.left.left = TreeNode(11)
root.right.left.right = TreeNode(25)

root.right.right.left = TreeNode(32)
root.right.right.right = TreeNode(70)


def get_next_inorder_successor(curr_node):
    if curr_node.right:
        next_node = curr_node.right
    else:
        next_node = find_parent(root, curr_node)
    return next_node.val

print(get_next_inorder_successor(root.right.left.left))
print(get_next_inorder_successor(root.right.right.left))
