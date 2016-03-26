class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.n, self.ans = len(nums), []
        self.nums, self.visited = nums, [False] * self.n
        self.helper(0, [])
        return self.ans

    def helper(self, count, nums):
        if count == self.n:
            self.ans.append(nums)
        nums_set = set()
        for i in range(self.n):
            if not self.visited[i] and self.nums[i] not in nums_set:
                self.visited[i] = True
                nums_set.add(self.nums[i])
                self.helper(count + 1, nums + [self.nums[i]])
                self.visited[i] = False
