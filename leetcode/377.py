class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        max_value = max(max(nums), target)
        self.dp = [0] * (max_value + 1)
        for i in range(target+1):
            self.solve_iterator(i, nums)
        return self.dp[target]

    def solve_iterator(self, i, nums):
        cnt = 0
        for num in nums:
            rest = i - num
            if rest == 0:
                cnt += 1
            if rest > 0:
                cnt += self.dp[rest]
        self.dp[i] = cnt

    def solve_recursion(self, i, nums):
        cnt = 0
        if i <= 0: return
        if self.dp[i] != 0: return self.dp[i]
        for num in nums:
            rest = i - num
            if rest == 0:
                cnt += 1
            if rest > 0:
                cnt += self.solve(rest, nums)
        self.dp[i] = cnt
        return cnt


# testing
test_nums = [[1, 2, 3], [3, 33, 333]]
test_targets = [4, 10000]
for i in range(len(test_nums)):
    print(Solution().combinationSum4(test_nums[i], test_targets[i]))