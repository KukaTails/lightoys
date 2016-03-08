class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        tmp_list = []
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                tmp_list.append(nums2[j])
                j += 1
            else:
                tmp_list.append(nums1[i])
                i += 1
        while i < m:
            tmp_list.append(nums1[i])
            i += 1
        while j < n:
            tmp_list.append(nums2[j])
            j += 1
        for k, elem in enumerate(tmp_list):
            nums1[k] = elem