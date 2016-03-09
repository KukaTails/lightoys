class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = n * (n + 1) / 2
        count = reduce(lambda x, y: x + y, nums, 0)
        return sum - count
