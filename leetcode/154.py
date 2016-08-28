class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(0, len(nums) - 1, nums)

    def helper(self, start, end, nums):
        if start < end:
            mid = (start + end) / 2
            if nums[start] == nums[end]:
                min_val = min(nums[start:end+1])
                return min_val
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
            return self.helper(start, end, nums)
        return nums[start]