# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node_num = self.get_node_num(head)
        if node_num == 0: return head

        k = node_num - (k % node_num)
        kth_node = self.get_kth_node(head, k)

        first_list = head
        second_list = kth_node.next
        kth_node.next = None
        first_list = self.reverse_list(first_list)
        second_list = self.reverse_list(second_list)
        #self.print_list(first_list)
        #self.print_list(second_list)

        new_list = self.link_lists(first_list, second_list)
        new_list = self.reverse_list(new_list)
        #self.print_list(new_list)
        return new_list

    @staticmethod
    def link_lists(first_list_head, second_list_head):
        if first_list_head == None:
            return second_list_head
        else:
            visitor = first_list_head
            while visitor.next != None:
                visitor = visitor.next
            visitor.next = second_list_head
            return first_list_head

    @staticmethod
    def reverse_list(head):
        new_head = ListNode(-1)
        while head != None:
            tmp = head.next
            head.next = new_head.next
            new_head.next = head
            head = tmp
        return new_head.next

    @staticmethod
    def get_kth_node(head, k):
        visitor = head
        for i in range(1, k):
            visitor = visitor.next
        return visitor

    @staticmethod
    def get_node_num(head):
        cnt, visitor = 0, head
        while visitor != None:
            cnt += 1
            visitor = visitor.next
        return cnt

    @staticmethod
    def build_list(values):
        visitor = head = ListNode(-1)
        for value in values:
            visitor.next = ListNode(value)
            visitor = visitor.next
        visitor.next = None
        return head.next

    @staticmethod
    def print_list(head):
        ls = []
        while head != None:
            ls.append(head.val)
            head = head.next
        print(ls)


# testing
test_cases = ([[], 0], [[], 1], [[1], 0], [[1], 1], [[1], 2],
              [[1, 2, 3], 0], [[1, 2, 3], 1], [[1, 2, 3], 2],
              [[1, 2, 3], 3], [[1, 2, 3], 4], [[1, 2, 3], 5])
for case in test_cases:
    solution = Solution()
    ls = solution.build_list(case[0])
    ls = solution.rotateRight(ls, case[1])
    solution.print_list(ls)