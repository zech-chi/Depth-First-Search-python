# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def DFS(node):
            if node.left:
                if node.left.left == None and node.left.right == None:
                    if node.left.val == target:
                        node.left = None
                else:
                    DFS(node.left)
            if node.right:
                if node.right.left == None and node.right.right == None:
                    if node.right.val == target:
                        node.right = None
                else:
                    DFS(node.right)
            
            if node.left:
                if node.left.left == None and node.left.right == None:
                    if node.left.val == target:
                        node.left = None
            if node.right:
                if node.right.left == None and node.right.right == None:
                    if node.right.val == target:
                        node.right = None

        DFS(root)
        if root.left == None and root.right == None and root.val == target:
            return None
        return root
