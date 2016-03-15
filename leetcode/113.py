# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.count = 0
        self.sum = sum
        self.path = []
        self.paths = []
        self.helper(0, root)
        return self.paths
    
    def helper(self, deep, node):
        if not node:
            return
        self.count += node.val
        self.path.append(node.val)
        if node.left:
            self.helper(deep + 1, node.left)
        if node.right:
            self.helper(deep + 1, node.right)
        if not node.left and not node.right and self.count == self.sum:
            path = [elem for elem in self.path]
            self.paths.append(path)
        self.count -= node.val
        self.path.pop()