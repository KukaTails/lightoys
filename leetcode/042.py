class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        import sys
        length = len(height)
        left, right = [0] * length, [0] * length
        max_left = max_right = -sys.maxsize-1

        left_start, right_start = 0, length-1
        for i in range(length):
            if not(i == 0 or height[i] >= height[i-1]):
                left_start = i
                break
        for i in range(length-1, -1, -1):
            if not(i == length-1 or height[i] >= height[i+1]):
                right_start = i
                break
        for i in range(0, length):
            max_left = height[i] if height[i] > max_left else max_left
            left[i] = max_left
        for i in range(length-1, -1, -1):
            max_right = height[i] if height[i] > max_right else max_right
            right[i] = max_right
        result = 0
        while left_start <= right_start:
            result += min([left[left_start], right[left_start]]) - height[left_start]
            left_start += 1
        return result


# testing
test_cases = [[], [1,2,3], [3,2,1], [4,2,3], [2,1,1,2], [0,1,2,2,1,0]]
for test_case in test_cases:
    print(Solution().trap(test_case))