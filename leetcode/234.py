# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast.next and fast.next.next:
            slow = solw.next
            fast = fast.next.next
        slow.next = self.reverse(slow.next)
        slow = slow.next
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True


    def reverse(self, head):
        pre = next = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
