class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_table = {}
        for i, x in enumerate(nums):
            if hash_table.has_key(x):
                if i - hash_table[x] <= k:
                    return True
            hash_table[x] = i
        return False
