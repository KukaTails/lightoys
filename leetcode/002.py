class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val_l1 = getValue(l1)
        val_l2 = getValue(l2)
        result = val_l1 + val_l2
        return createListNode(result)

def getValue(list):
    if list.next != None:
        next_value = getValue(list.next)
        return 10 * next_value + list.val
    else:
        return list.val


def createListNode(value):
    if value // 10 == 0:
        return ListNode(value)
    rest = value % 10
    next = createListNode(value // 10)
    result = ListNode(rest)
    result.next = next
    return result