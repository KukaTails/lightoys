# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return head
        pre = visitor = head
        while pre and visitor:
            pre = pre.next
            visitor = visitor.next
            if visitor == None:
                return None
            visitor = visitor.next
            if pre == visitor:
                break
        if pre == None or visitor == None:
            return None
        pre = head
        while pre != visitor:
            pre = pre.next
            visitor = visitor.next
        return pre