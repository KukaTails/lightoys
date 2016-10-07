# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        values = self.convert_to_array(head)
        return self.build_tree(values)


    def convert_to_array(self, head):
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return array


    def build_tree(self, values):
        if len(values) == 0: return None

        low, high = 0, len(values)-1
        mid = low + (high-low) // 2
        root = TreeNode(values[mid])
        left = self.build_tree(values[:max(0,mid-1)])
        right = self.build_tree(values[min(high+1,mid+1):])
        root.left, root.right = left, right
        return root
