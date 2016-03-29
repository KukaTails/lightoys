class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.visited = [False] * (n + 1)
        self.count, self.ans = 0, None
        self.n, self.k = n, k
        self.helper(0, [])
        self.dp = [1] * (n + 1)
        for i in range(1, n + 1):
            self.dp[i] = self.dp[i-1] * i
        print(self.dp)
        return self.ans

    def helper(self, count, nums):
        if count == self.n:
            self.count += 1
            self.ans = nums if self.count == self.k else None
            return
        for i in range(1, self.n + 1):
            if self.count == self.k: return
            if not self.visited[i]:
                self.visited[i] = True
                self.helper(count + 1, nums + [i])
                self.visited[i] = False

for i in range(1, 7):
    print(Solution().getPermutation(3, i))