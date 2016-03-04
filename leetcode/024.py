# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = head
        if not pre: return None
        now = pre.next
        if not now: return pre

        rest = self.swapPairs(now.next)
        pre.next = rest
        now.next = pre
        return now