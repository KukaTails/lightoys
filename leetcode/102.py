# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        nodes = []
        if root:
            nodes.append(root)
            ans.append(map(lambda x: x.val, nodes))
        while nodes:
            next_level_nodes = nums = []
            for node in nodes:
                if node.left:  next_level_nodes.append(node.left)
                if node.right: next_level_nodes.append(node.right)
            if not next_level_nodes: break
            ans.append(map(lambda x: x.val, next_level_nodes))
            nodes = next_level_nodes
        return ans