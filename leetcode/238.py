class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        len_nums = len(nums)
        output = output_pre = output_post = []
        for i in range(len_nums):
            output_pre[i] = product
            product *= nums[i]
        product = 1
        for i in range(len_nums):
            output_post[len_nums - i] = product
            product *= nums[len_nums - i]
        for i in range(len_nums):
            output[i] = output_pre[i] * output_post[i]
        return output
