class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        from math import floor
        low, high = -1.0, x + 1.0
        EPS = 0.00000001
        while abs(low - high) > EPS:
            mid = (low + high) / 2
            if mid * mid < x:
                low = mid + 0.0000000000001
            elif mid * mid > x:
                high = mid - 0.0000000000001
            else:
                return int(floor(mid))
        print(x, low, high, (low + high) / 2.0)
        return int(floor((low + high) / 2.0 + EPS / 2.0))


# testing
test_cases = [0, 1, 2, 4, 9, 16, 36, 2147395599, 2147395600]
for test_case in test_cases:
    print(Solution().mySqrt(test_case))

from math import pow
print(pow(2147395600, 0.5))