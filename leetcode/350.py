class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash_table = {}
        for num in nums1:
            if num in hash_table.keys():
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        ans = []
        for num in nums2:
            if num in hash_table.keys():
                ans.append(num)
                if hash_table[num] - 1 == 0:
                    hash_table.pop(num)
                else:
                    hash_table[num] -= 1
        return ans


# testing
test_cases = [[[], []], [[1], [2]],[[1, 2, 2, 2, 1], [2, 2, 2]]]
for test_case in test_cases:
    print(Solution().intersect(test_case[0], test_case[1]))