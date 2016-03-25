# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root: return
        node = root
        while node.left and node.right:
            node.left.next = node.right
            pre, visit = node, node.next
            while visit:
                pre.right.next = visit.left
                visit.left.next = visit.right
                pre = visit
                visit = visit.next
            node = node.left
