# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        counter = 0

        def DFS(cur_node):
            nonlocal counter
            Sum = cur_node.val
            count_nodes = 1

            if cur_node.left:
                left_sum, left_count_nodes = DFS(cur_node.left)
                Sum += left_sum
                count_nodes += left_count_nodes
            
            if cur_node.right:
                right_sum, right_count_nodes = DFS(cur_node.right)
                Sum += right_sum
                count_nodes += right_count_nodes

            if Sum // count_nodes == cur_node.val:
                counter += 1
            return (Sum, count_nodes)
        
        DFS(root)
        return counter
