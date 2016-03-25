class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.visited = [False] * 10
        self.k, self.ans = k, []
        self.helper(1, n, 0, [])
        return self.ans

    def helper(self, start, rest, count, nums):
        import copy
        if rest < 0 or count > self.k: return
        if rest == 0 and count == self.k:
            self.ans.append(nums); return
        for i in range(start, 10):
            if i <= rest:
                self.helper(i + 1, rest - i, count + 1, copy.deepcopy(nums) + [i])
