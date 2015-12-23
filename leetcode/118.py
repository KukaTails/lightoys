class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = []
        for i in range(numRows):
            sub_arr = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    sub_arr.append(1)
                else:
                    sub_arr.append(arr[i-1][j-1] + arr[i-1][j])
            arr.append(sub_arr)
        return arr