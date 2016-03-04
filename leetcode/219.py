class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_table = {}
        for i, x in enumerate(nums):
            if x not in hash_table.keys():
                hash_table[x] = [i]
            else:
                seq = hash_table[x]
                top_elem = seq.pop()
                seq.append(top_elem)
                if i - top_elem <= k:
                    return True
                else:
                    seq.append(i)
        return False
