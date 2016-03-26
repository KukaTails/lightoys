class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = sorted(nums)
        self.len_nums, self.ans = len(nums), []
        self.helper(0, [])
        return self.ans

    def helper(self, start, nums):
        self.ans.append(nums)
        for i in range(start, self.len_nums):
            if (i == start) or (i > start and self.nums[i-1] != self.nums[i]):
                self.helper(i + 1, nums + [self.nums[i]])
