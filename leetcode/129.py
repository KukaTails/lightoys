# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        ans = 0
        if not root: return 0
        nodes = deque()
        nodes.append([root, root.val])
        while nodes:
            node, value = nodes.popleft()
            leaf_node = True
            if node.left:
                leaf_node = False
                nodes.append([node.left, value * 10 + node.left.val])
            if node.right:
                leaf_node = False
                nodes.append([node.right, value * 10 + node.right.val])
            if leaf_node:
                ans += value
        return ans