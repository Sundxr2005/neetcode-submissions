# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            leftheight = dfs(node.left)
            rightheight = dfs(node.right)
            diameter = max(diameter, leftheight + rightheight)

            return 1 + max(leftheight, rightheight)
        dfs(root)
        return diameter

        