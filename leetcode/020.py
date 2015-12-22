class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if stack == []:
                stack.append(ch)
            elif ch in chars_map.keys() and chars_map[ch] == stack[len(stack) - 1]:
                stack.pop()
            else:
                stack.append(ch)
        if len(stack) != 0:
            return False
        else:
            return True
