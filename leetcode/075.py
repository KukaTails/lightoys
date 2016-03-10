class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        reds = whites = blues = 0
        for color in nums:
            if color == 0:
                reds += 1
            if color == 1:
                whites += 1
            if color == 2:
                blues += 1
        for i in range(len(nums)):
            if i < reds:
                nums[i] = 0
            elif i < whites + reds:
                nums[i] = 1
            else:
                nums[i] = 2
