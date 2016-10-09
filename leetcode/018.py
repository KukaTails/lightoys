class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lists = self.k_sum(4, sorted(nums), target)
        ans, hash_table = [], set()
        for list in lists:
            if str(list) in hash_table:
                continue
            else:
                ans.append(list)
                hash_table.add(str(list))
        return ans


    def k_sum(self, k, nums, target):
        ans = []
        if k == 2:
            start, end = 0, len(nums)-1
            while start < end:
                if nums[start] + nums[end] == target:
                    ans.append([nums[start], nums[end]])
                    start += 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1
        else:
            for i, val in enumerate(nums):
                lists = self.k_sum(k-1, nums[i+1:], target-val)
                for list in lists:
                    ans.append([val] + list)
        return ans

# testing
test_cases = [([-3,-2,-1,0,0,1,2,3], 0), ([0, 0, 0, 0, 1, 1, 1], 1)]
for case in test_cases:
    print(Solution().fourSum(case[0], case[1]))