class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_index = self.find_left_most(nums, target)
        right_index = self.find_right_most(nums, target)


    def find_left_most(self, nums, target):
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        if start >= 0 and start < len(nums) and nums[start] == target:
            return start
        return -1

    def find_right_most(self, nums, target):
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                start = mid + 1
        if end >= 0 and end < len(nums) and nums[end] == target:
            return end
        return -1