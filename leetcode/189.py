class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        self.reverse(nums, 0, length - k - 1)
        self.reverse(nums, length - k,length - 1)
        self.reverse(nums, 0, length - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1; right -= 1
        return nums
