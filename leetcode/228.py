class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        start = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if (i + 1 == len_nums) or (i + 1 < len_nums and nums[i] + 1 != nums[i + 1]):
                if start != i:
                    ans.append(str(nums[start]) + "->" + str(nums[i]))
                else:
                    ans.append(str(nums[start]))
                start = i + 1
        return ans