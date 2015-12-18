class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for ident, x in enumerate(nums):
            dict[x] = ident
        nums.sort()
        l = 0
        r = len(nums) - 1
        find = False
        while l <= r and find == False:
            sum = nums[l] + nums[r]
            if (sum == target):
                result = [nums[l], nums[r]]
                find = True
            elif sum > target:
                r -= 1
            else:
                l += 1
        ans = []
        for x in result:
            ans.append(dict[x] + 1)
        return ans

nums = [0, 4, 3, 0]
print(Solution().twoSum(nums, 0))