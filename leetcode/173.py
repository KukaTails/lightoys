# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack, self.visit_node = [], root

    def hasNext(self):
        """
        :rtype: bool
        """
        return not (self.stack == [] and self.visit_node == None)


    def next(self):
        """
        :rtype: int
        """
        while True:
            if self.visit_node:
                self.stack.append(self.visit_node)
                self.visit_node = self.visit_node.left
            else:
                ans = self.visit_node = self.stack.pop()
                self.visit_node = self.visit_node.right
                return ans.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())