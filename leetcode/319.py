class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        records = [True for i in range(n)]
        for i in range(2, n + 1):
            self.toggle(i, n, records)
        return reduce(lambda x, y: x + y if y else x, records, 0)

    def toggle(self, k, n, records):
        for i in range(k, n + 1, k):
            records[i - 1] = False if records[i - 1] else True

print(Solution().bulbSwitch(10))