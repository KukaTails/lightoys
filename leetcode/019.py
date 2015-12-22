# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = cur = head
        for i in range(n):
            pre = pre.next
        if pre is None:
            return cur.next
        while pre.next is not None:
            pre = pre.next
            cur = cur.next
        cur.next = cur.next.next
        return head