class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        len_nums = len(nums)
        self.dp = [0] * len_nums
        for i in range(len_nums):
            if i == 0:
                self.dp[i] = nums[i]
            else:
                self.dp[i] = self.dp[i - 1] + nums[i]
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i - 1 >= 0:
            return self.dp[j] - self.dp[i - 1]
        else:
            return self.dp[j]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)