class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        dp = [0] * len_nums
        for i in range(len_nums):
            if i == 0:
                dp[i] = nums[i]
            elif i - 2 < 0:
                dp[i] = max(dp[i-1], nums[i])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[len_nums - 1] if len_nums > 0 else 0
