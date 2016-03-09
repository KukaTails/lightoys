class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        nums = len(prices)
        mins = [0 for i in range(nums)]
        for i in range(nums):
            if i == 0 or prices[i] < mins[i - 1]:
                mins[i] = prices[i]
            else:
                mins[i] = mins[i - 1]
        profit = 0
        for i in range(1, nums):
            if prices[i] - mins[i] > profit:
                profit = prices[i] - mins[i]
        return profit
