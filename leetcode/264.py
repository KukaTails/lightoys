class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums, ugly_index = [1] * n, 1
        index_2 = index_3 = index_5 = 0
        while ugly_index < n:
            min_val = min([nums[index_2]*2, nums[index_3]*3, nums[index_5]*5])
            nums[ugly_index] = min_val
            while nums[index_2] * 2 <= min_val: index_2 += 1
            while nums[index_3] * 3 <= min_val: index_3 += 1
            while nums[index_5] * 5 <= min_val: index_5 += 1
            ugly_index += 1
        return nums[n-1]