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
        if head == None: return head

        header = ListNode(-1)
        header.next = head
        rec_ptr, pre_ptr, next_ptr = header, head, head.next
        while next_ptr:
            if pre_ptr.val == next_ptr.val:
                number, visitor = pre_ptr.val, next_ptr
                while visitor and visitor.val == number:
                    visitor = visitor.next
                rec_ptr.next = visitor
                pre_ptr = rec_ptr.next if rec_ptr else None
                next_ptr = pre_ptr.next if pre_ptr else None
            else:
                rec_ptr = pre_ptr
                pre_ptr = next_ptr
                next_ptr = next_ptr.next
        return header.next
