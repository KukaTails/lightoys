class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        flag = True
        ans = ""
        if strs == []:
            return ""
        min_len = min([len(string) for string in strs])
        seq_len = len(strs)
        for i in range(min_len):
            ch = strs[0][i]
            for j in range(seq_len):
                if strs[j][i] != ch:
                    flag = False
                if not flag:
                    break
            if flag:
                ans += ch
            else:
                break
        return ans