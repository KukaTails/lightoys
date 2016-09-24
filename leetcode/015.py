class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        length = len(nums)
        ans = set()
        if length < 3: return []
        for i in range(length-2):
            left, right = i+1, length-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                #print(sum, left, right)
                if sum == 0:
                    ans.add(str(nums[i]) + ',' + str(nums[left]) + ',' + str(nums[right]))
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return [self.decode(x) for x in ans]

    def decode(self, nums_coded):
        from functools import reduce
        values = nums_coded.split(',')
        return reduce(lambda x, y: x + [int(y)], values, [])


# testing
test_cases = [[], [-2,0,1,1,2], [1,-1], [-1,-1,5], [2,-1,-1], [-1,-1,-1,2,2], [-1,0,1,2,-1,4]]
for case in test_cases:
    print(Solution().threeSum(case))