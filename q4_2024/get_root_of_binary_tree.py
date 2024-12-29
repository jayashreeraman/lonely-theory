"""
You are given a 2D integer array descriptions where
 descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree 
 of unique values. 
 
Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


desc1 = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]

desc2 = [[1,2,1],[2,3,0],[3,4,1]]

def createBinaryTree(descriptions):
    # TreeNode with parent and node
    treeNodesDict = {}
    
    for d in descriptions:
        if d[0] not in treeNodesDict:
            treeNodesDict[d[0]] = [TreeNode(d[0]), None]
        parent = treeNodesDict[d[0]][0]
        if d[1] not in treeNodesDict:
            treeNodesDict[d[1]] = [TreeNode(d[1]), TreeNode(d[0])]
        child = treeNodesDict[d[1]][0]
        

        # Assign child to parent
        if d[2] == 1:
            parent.left = child
        else:
            parent.right = child

    for t in treeNodesDict:
        val = treeNodesDict[t]
        
        if not val[1]:
            root = val[0]
            root_dict = vars(root)
            print(root_dict['val'])
            return(root_dict['val'])
    
createBinaryTree(desc2)

