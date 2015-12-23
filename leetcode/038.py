class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        pre_seq = "1"
        for i in range(n - 1):
            cur_seq = ""
            size = len(pre_seq)
            count = index = 0
            while index < size:
                count = 0
                val = pre_seq[index]
                while index < size and pre_seq[index] == val:
                    count += 1; index += 1
                cur_seq += str(count) + str(val)
            pre_seq = cur_seq
        return pre_seq