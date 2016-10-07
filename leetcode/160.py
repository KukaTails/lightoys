# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a_length = self.get_length(headA)
        b_length = self.get_length(headB)
        if a_length > b_length:
            first, second = headA, headB
        else:
            first, second = headB, headA

        move_length = abs(a_length-b_length)
        while move_length:
            first = first.next
            move_length -= 1

        while first and second and first != second:
            first = first.next
            second = second.next
        gc.collect()
        return first

    @staticmethod
    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
