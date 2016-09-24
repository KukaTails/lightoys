class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import sys
        if len(nums) < 3: return 0
        nums = sorted(nums)
        length = len(nums)
        min_diff = sys.maxsize
        for i in range(length-2):
            left, right = i+1, length-1
            while left < right:
                diff = nums[i] + nums[left] + nums[right] - target
                if abs(diff) < abs(min_diff):
                    min_diff = diff
                if diff == 0:
                    break
                elif diff < 0:
                    left += 1
                else:
                    right -= 1
        return target + min_diff