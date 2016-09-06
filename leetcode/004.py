class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return self.findKth(nums1, nums2, total // 2 + 1)
        else:
            return (self.findKth(nums1, nums2, total // 2) \
                    + self.findKth(nums1, nums2, total // 2 + 1)) / 2.0

    def findKth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k - 1]
        if len(nums2) == 0:
            return nums1[k - 1]
        if k == 1:
            return min([nums1[0], nums2[0]])
        a = nums1[k / 2 - 1] if len(nums1) >= k / 2 else None
        b = nums2[k / 2 - 1] if len(nums2) >= k / 2 else None

        if b is None or (a is not None and a < b):
            return self.findKth(nums1[k / 2:], nums2, k - k / 2)
        return self.findKth(nums1, nums2[k / 2:], k - k / 2)