class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import copy
        ans = [[]]
        for num in sorted(nums):
            lists = []
            for ls in copy.deepcopy(ans):
                ls.append(num)
                lists.append(ls)
            ans = ans + lists
        return ans
