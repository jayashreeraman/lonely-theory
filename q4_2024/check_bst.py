"""
DCP: 651

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint 
that the key in the left child must be less than or equal to the root 
and the key in the right child must be greater than or equal to the root.

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

root = TreeNode(20)
root.left = TreeNode(8)
# root.left = TreeNode(80)
root.right = TreeNode(12)
root.left.left = TreeNode(6)
root.left.right = TreeNode(10)

root.right.left = TreeNode(11)
root.right.right = TreeNode(15)


def check_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True

    if node.val <= min_val or node.val > max_val:
        return False
    
    return check_valid_bst(node.left, min_val, node.val) and check_valid_bst(node.right, node.val, max_val)

print(check_valid_bst(root))

