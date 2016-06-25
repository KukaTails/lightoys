class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lhs_set = set(nums1)
        intersection = set()
        for x in nums2:
            if x in lhs_set:
                intersection.add(x)
        return list(intersection)

# test cases
test_cases = [[[], []],
              [[1, 2, 3, 4], [1, 2, 3, 4]],
              [1, 1, 1, 1], [1, 1, 1, 1],
              [1, 1, 2, 3, 2, 4], [2, 3, 4]]
