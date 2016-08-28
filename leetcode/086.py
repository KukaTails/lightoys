# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        handle = ListNode(-1)
        handle.next = head
        i, pre, j = handle, handle, head
        while j != None:
            if j.val < x:
                if i.next != j:
                    pre.next = j.next
                    tmp = i.next
                    i.next = j
                    j.next = tmp
                    j = pre.next
                    i = i.next
                else:
                    i = i.next
                    pre = pre.next
                    j = j.next
            else:
                pre = pre.next
                j = j.next
        return handle.next

    @staticmethod
    def print_list(head):
        ls = []
        while head != None:
            ls.append(head.val)
        print(ls)

# testing
# [] 0 => []
# [] 2 => []
# [1] 0 => [1]
# [1] 1 => [1]
# [1] 2 => [1]
# [1, 2, 3, 4] 4 => [1, 2, 3, 4]
# [1, 2, 3, 4] 5 => [1, 2, 3, 4]
# [1, 4, 2, 3] 2 => [1, 4, 2, 3]
# [1, 4, 2, 3] 3 => [1, 2, 4, 3]
# [3,1,2] 3 => [1, 2, 3]