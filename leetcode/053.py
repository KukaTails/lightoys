class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        sum = 0
        for val in nums:
            sum = sum + val if sum >= 0 else val
            max_sum = sum if sum > max_sum else max_sum
        return max_sum