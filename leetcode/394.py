class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from functools import reduce
        stack = []
        for ch in s:
            if ch == ']':
                str = ""
                while stack[-1] != '[':
                    str = stack.pop() + str
                stack.pop()
                times = ""
                while stack and stack[-1].isdigit():
                    times = stack.pop() + times
                times = int(times)
                str = times * str
                stack.append(str)
            else:
                stack.append(ch)
        return reduce(lambda x, y: x + y, stack, "")


# testing
test_cases = ["10[a]", "3[a]2[bc]", "3[a2[c]]"]
for test_case in test_cases:
    print(Solution().decodeString(test_case))