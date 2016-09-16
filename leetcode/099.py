# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        import sys
        self.pre, self.vis = -sys.maxsize-1, None
        self.nodes = []
        self.visit(root)
        if len(self.nodes) == 0:
            return
        elif len(self.nodes) == 1:
            left, right = self.nodes[0][0], self.nodes[0][1]
        elif len(self.nodes) == 2:
            left, right = self.nodes[0][0], self.nodes[1][1]
        left.val, right.val = right.val, left.val

    def visit(self, root):
        if not root: return
        self.visit(root.left)
        if self.vis == None:
            self.vis = root
        else:
            self.pre = self.vis
            self.vis = root
            if self.pre.val > self.vis.val:
                self.nodes.append([self.pre, self.vis])
        self.visit(root.right)