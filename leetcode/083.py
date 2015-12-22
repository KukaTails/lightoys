# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = cur = head
        while pre:
            if cur.val != pre.val:
                cur.next = pre
                cur = cur.next
            pre = pre.next
        if cur:
            cur.next = None
        return head