class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.len_nums, self.nums = len(nums), nums
        self.visited, self.per = [0] * self.len_nums, [0] * self.len_nums
        self.ans, self.count = [], 0
        self.helper(0)
        return self.ans

    def helper(self, deep):
        if deep == self.len_nums:
            import copy
            self.ans.append(copy.deepcopy(self.per))
        else:
            for i in range(self.len_nums):
                if self.visited[i]:
                    continue
                self.per[self.count] = self.nums[i]
                self.count += 1
                self.visited[i] = True
                self.helper(deep + 1)
                self.count -= 1
                self.visited[i] = False
