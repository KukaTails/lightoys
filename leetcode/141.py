# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        pre_vis = cur_vis = head
        while pre_vis and cur_vis:
            cur_vis = cur_vis.next
            pre_vis = pre_vis.next
            if not pre_vis:
                return False
            pre_vis = pre_vis.next
            if pre_vis == cur_vis:
                return True
        return False
