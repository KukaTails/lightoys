class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count, added, stack = [0] * 26, [False] * 26, []
        for ch in s:
            count[ord(ch)-ord('a')] += 1
        for ch in s:
            count[ord(ch)-ord('a')] -= 1
            if added[ord(ch)-ord('a')]:
                continue
            while stack and ord(stack[-1]) > ord(ch) and count[ord(stack[-1]) - ord('a')] > 0:
                added[ord(stack[-1])-ord('a')] = False
                stack.pop()
            stack.append(ch)
            added[ord(ch)-ord('a')] = True
        return "".join(stack)
