class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashtable = {}
        for ch in s:
            if ch in hashtable.keys():
                hashtable[ch] += 1
            else:
                hashtable[ch] = 1
        ans = 0
        for key in hashtable.keys():
            value = hashtable[key]
            ans += 2 * (value // 2)
            hashtable[key] = value % 2
        for key in hashtable.keys():
            if hashtable[key] == 1:
                ans += 1
                break
        return ans
