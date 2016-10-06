class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = sum = 0
        while sum + ((k+1) * 9 * (10 ** k)) <= n:
            k += 1
            sum += k * 9 * (10 ** (k-1))
        kth = (n-sum) // (k+1)
        rest = (n-sum) % (k+1)
        print(kth, rest)
        num = 10 ** k + kth
        digit_cnt = (k+1) - rest
        print(n, num)
        while digit_cnt and num:
            num //= 10
            digit_cnt -= 1
        return num % 10



# testing
test_cases = [0, 1, 9, 10]
for case in test_cases:
    print(Solution().findNthDigit(case))