class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        left, right, length = 0, len(nums)-1, len(nums)
        while left < right:
            mid = left + (right-left) // 2
            if (mid-1 < 0 or nums[mid-1] < nums[mid]) and (mid+1 >= length or nums[mid] > nums[mid+1]):
                return mid
            elif mid-1 >= 0 and nums[mid-1] > nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return left


# testing
test_cases = [[], [1], [1,2], [-1, 1, 0], [1,2,3,1], [3,4,3,2,1]]
result = [-1, 0, 1, 1, 2, 1]
for i, case in enumerate(test_cases):
    assert result[i] == Solution().findPeakElement(case)