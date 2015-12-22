# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_lhs = l1
        cur_rhs = l2
        ls = cur = ListNode(-1)
        while cur_lhs is not None and cur_rhs is not None:
            if cur_lhs.val < cur_rhs.val:
                cur.next = cur_lhs
                cur = cur.next
                cur_lhs = cur_lhs.next
            else:
                cur.next = cur_rhs
                cur = cur.next
                cur_rhs = cur_rhs.next
        while cur_lhs is not None:
            cur.next = cur_lhs
            cur = cur.next
            cur_lhs = cur_lhs.next
        while cur_rhs is not None:
            cur.next = cur_rhs
            cur = cur.next
            cur_rhs = cur_rhs.next
        cur.next = None
        return ls.next