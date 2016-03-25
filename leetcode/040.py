class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans, self.len = [], len(candidates)
        self.nums = sorted(candidates)
        self.helper(target, 0, [])
        return self.ans

    def helper(self, rest, start, nums):
        import copy
        if rest == 0:
            self.ans.append(nums); return
        for i in range(start, self.len):
            if (i > start and self.nums[i] == self.nums[i-1]) or (self.nums[i] > rest):
                continue
            self.helper(rest - self.nums[i], i + 1, copy.deepcopy(nums) + [self.nums[i]])
