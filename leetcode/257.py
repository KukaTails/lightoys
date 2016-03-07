# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        elif not root.left and not root.right:
            return [str(root.val)]
        else:
            val = str(root.val) + "->"
            paths = []
            if root.left:
                paths += self.binaryTreePaths(root.left)
            if root.right:
                paths += self.binaryTreePaths(root.right)
            return map(lambda x: val + x, paths)