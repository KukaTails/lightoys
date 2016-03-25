class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums) - 1
        while l < h:
            mid = (l + h) / 2
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
        return nums[l]
