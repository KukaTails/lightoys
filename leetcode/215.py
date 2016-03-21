class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = self.partition(l, r, nums)
            if mid + 1 < k:
                l = mid + 1
            elif mid + 1 > k:
                r = mid - 1
            else:
                return nums[mid]
        return nums[l]

    def partition(self, l, r, num):
        pivot = num[r]
        i = l - 1
        for j in range(l, r):
            if num[j] > pivot:
                i += 1
                num[i], num[j] = num[j], num[i]
        num[i+1], num[r] = num[r], num[i+1]
        return i + 1
