class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        return self.binarySearch(nums, low, high, target)

    def binarySearch(self, nums, low, high, target):
        if high - low <= 0:
            return low + 1 if target > nums[low] else low
        else:
            mid = (low + high) / 2
            if nums[mid] > target:
                return self.binarySearch(nums, low, mid - 1, target)
            elif nums[mid] < target:
                return self.binarySearch(nums, mid + 1, high, target)
            else:
                return mid