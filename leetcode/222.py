# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.height(root)
        if h >= 0:
            if self.height(root.right) == h - 1:
                return (1 << h) + self.countNodes(root.right)
            else: 
                return (1 << (h-1)) + self.countNodes(root.left)
        else:
            return 0

    def height(self, root):
        ans, node = -1, root
        while node:
            ans += 1
            node = node.left
        return ans
