# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.head = head
        self.head_index = 0
        self.len = 0
        while head:
            self.len += 1
            head = head.next



    def helper(self, start, end):
        if self.head_index > end:
            return None
        mid = (start + end) // 2
        left = self.helper(start, mid-1)
        node = TreeNode(self.head[self.head_index])
        self.head_index += 1
        right = self.helper(mid+1, end)
        node.left, node.right = left, right
        return node