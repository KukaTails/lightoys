class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import sys
        min_1 = min_2 = sys.maxsize
        for num in nums:
            if min_1 >= num:
                min_1 = num
            elif min_2 >= num:
                min_2 = num
            else:
                return True
        return False