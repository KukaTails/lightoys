# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        handle = ListNode(-1)
        handle.next = head
        slow = fast = handle
        for i in range(1, m):
            if slow == None or fast == None:
                return handle.next
            slow = slow.next
        fast = slow.next
        slow.next = None
        for i in range(m, n+1):
            if fast == None:
                break
            tmp = fast.next
            fast.next = slow.next
            slow.next = fast
            fast = tmp
        while slow.next:
            slow = slow.next
        slow.next = fast
        return handle.next