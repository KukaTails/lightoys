# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n-1
        while low < high:
            mid = low + (high-low)//2
            if not isBadVersion(mid+1):
                low = mid+1
            else:
                if mid == 0 or not isBadVersion(mid):
                    return mid+1
                else:
                    high = mid-1
        return low+1
