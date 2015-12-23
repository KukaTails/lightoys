class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        strs_1 = version1.split('.')
        strs_2 = version2.split('.')
        len_1 = len(strs_1)
        len_2 = len(strs_2)
        max_len = max(len_1, len_2)
        strs_1 += ["0" for i in range(len_1, max_len)]
        strs_2 += ["0" for i in range(len_2, max_len)]
        for i in range(max_len):
            if int(strs_1[i]) > int(strs_2[i]):
                return 1
            elif int(strs_1[i]) < int(strs_2[i]):
                return -1
        return 0