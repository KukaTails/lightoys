class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index, length, count = 0, len(nums), len(nums)
        while index + 2 < count:
            if nums[index] == nums[index + 2]:
                self.move(nums, index + 2)
                count -= 1
            else:
                index += 1
        return count

    @staticmethod
    def move(array, pos):
        tmp = array[pos]
        for i in range(pos + 1, len(array)):
            array[i - 1] = array[i]
        array[len(array) - 1] = tmp


# testing
test_cases = [[], [1,1,1,2,2,3], [1,1,1]]
results = [0, 5, 2]
for i, test_case in enumerate(test_cases):
    assert results[i] == Solution().removeDuplicates(test_case)