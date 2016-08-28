class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, is_prime = 2, [True if i >= 2 else False for i in range(n)]
        while i * i < n:
            if not is_prime[i]:
                i += 1
                continue
            j = i * i
            while j < n:
                is_prime[j] = False
                j += i
            i += 1
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
        return count


# testing
test_cases = [100, 0, 1, 2, 3, 10, 100, 1000, 10000]
for case in test_cases:
    print(Solution().countPrimes(case))