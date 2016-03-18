class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pre_row = [1]
        for i in range(1, rowIndex + 1):
            next_row = [1] * (i + 1)
            for j in range(i + 1):
                if j == 0 or j == i:
                    next_row[j] = 1
                else:
                    next_row[j] = pre_row[j] + pre_row[j-1]
            pre_row = next_row
        return pre_row
