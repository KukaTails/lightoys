class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_table = {}
        for num in nums:
            if num in hash_table.keys():
                hash_table[num] += 1
            else:
                hash_table[num] = 1
        ls = []
        for key, value in hash_table.items():
            ls.append((key, value))