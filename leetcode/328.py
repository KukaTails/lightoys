# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        odd_visit, even_visit = head, head.next
        head_odd, head_even = head, head.next
        visit, node_count = head.next.next, 0
        while visit:
            node_count += 1
            if node_count & 1:
                odd_visit.next = visit
                odd_visit = visit
            else:
                even_visit.next = visit
                even_visit = visit
            visit = visit.next
        odd_visit.next = None
        even_visit.next = None
        odd_visit.next = head_even
        return head_odd
