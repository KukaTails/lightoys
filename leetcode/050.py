class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        x_is_positive = True if x > 0 else False
        n_is_positive = True if n >= 0 else False
        if abs(x) < 0.0000001: return 1.0
        ans = self.pow(abs(x), abs(n))
        ans = ans if x_is_positive or abs(n) % 2 == 0 else -ans
        ans = ans if n_is_positive else 1.0 / ans
        return ans

    def pow(self, x, n):
        if n == 0:
            return 1.0
        res = self.pow(x, n // 2)
        if n % 2 == 1:
            return x * res * res
        else:
            return res * res

# testing
test_cases = [[-4.48, 6], [8.8, -3], [0, 0], [-1, 1], [-100, 10], [100, 1], [100, 2], [8.8, 9], [8.8, 10]]
for test_case in test_cases:
    print(Solution().myPow(test_case[0], test_case[1]))