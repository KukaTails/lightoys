# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        return self.helper(0, len(nums) - 1)

    def helper(self, l, r):
        if l > r: return None
        mid = (l + r) / 2
        root = TreeNode(self.nums[mid])
        left_tree = self.helper(l, mid - 1)
        right_tree = self.helper(mid + 1, r)
        root.left, root.right = left_tree, right_tree
        return root