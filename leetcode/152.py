class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        max_dp = [0] * len_nums
        min_dp = [0] * len_nums
        for i in range(len_nums):
            if i == 0:
                max_dp[i] = nums[i]
                min_dp[i] = nums[i]
            else:
                min_dp[i] = min(min_dp[i-1] * nums[i], max_dp[i-1] * nums[i], nums[i])
                max_dp[i] = max(min_dp[i-1] * nums[i], max_dp[i-1] * nums[i], nums[i])
        return max(max_dp)