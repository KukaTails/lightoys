class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        numbers = len(prices)
        mins = [0 for i in range(numbers)]
        maxs = [0 for i in range(numbers)]
        profit_pre = [0 for i in range(numbers)]
        profit_post = [0 for i in range(numbers)]
        for i in range(numbers):
            if i == 0 or prices[i] < mins[i - 1]:
                mins[i] = prices[i]
            else:
                mins[i] = mins[i - 1]
            if i == 0:
                profit_pre[i] = 0
            elif prices[i] - mins[i - 1] > profit_pre[i - 1]:
                profit_pre[i] = prices[i] - mins[i - 1]
            else:
                profit_pre[i] = profit_pre[i - 1]

        for i in range(numbers - 1, -1, -1):
            if i == numbers - 1 or prices[i] > maxs[i + 1]:
                maxs[i] = prices[i]
            else:
                maxs[i] = maxs[i + 1]

            if i == numbers - 1:
                profit_post[i] = 0
            elif maxs[i + 1] - prices[i] > profit_post[i + 1]:
                profit_post[i] = maxs[i + 1] - prices[i]
            else:
                profit_post[i] = profit_post[i + 1]
        max_profit = 0

        for i in range(numbers):
            if i == 0:
                profit = profit_post[i]
            else:
                profit = profit_pre[i - 1] + profit_post[i]
            max_profit = profit if profit > max_profit else max_profit
        return max_profit
