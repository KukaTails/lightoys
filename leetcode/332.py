class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        import sys
        len_coins = len(coins)
        dp = [sys.maxint] * (amount + 1)

        for i in range(amount + 1):
            min_coins = dp[i]
            for j in range(len_coins):
                if i - coins[j] >= 0:
                    steps = dp[i-coins[j]]
                    if steps != sys.maxint and min_coins > steps + 1:
                        min_coins = steps + 1
            dp[i] = min_coins if i != 0 else 0
        return dp[amount] if dp[amount] != sys.maxint else -1
