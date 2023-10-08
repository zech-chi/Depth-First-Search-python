# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def DFS(root, leafs):
            if not root.left and not root.right:
                leafs.append(root.val)
                return
            if root.left:
                DFS(root.left, leafs)
            if root.right:
                DFS(root.right, leafs)
  
        leafs1 = []
        leafs2 = []
        DFS(root1, leafs1)
        DFS(root2, leafs2)

        if len(leafs1) != len(leafs2):
            return False

        for i in range(len(leafs1)):
            if leafs1[i] != leafs2[i]:
                return False
        return True
