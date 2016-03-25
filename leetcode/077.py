class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.ans, self.k, self.n = [], k, n
        self.helper(1, 0, [])
        return self.ans

    def helper(self, start, count, nums):
        import copy
        if count == self.k:
            self.ans.append(nums); return
        for i in range(start, self.n + 1):
            self.helper(i + 1, count + 1, copy.deepcopy(nums) + [i])
