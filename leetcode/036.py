class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        checked = []
        for row in board:
            checked.append(row)
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            checked.append(column)
        subboards = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                subboards[int(i / 3) * 3 + int(j / 3)].append(board[i][j])
        for subboard in subboards:
            checked.append(subboard)
        for x in checked:
            num_set = set()
            for num in x:
                if num != '.' and num in num_set:
                    return False
                else:
                    num_set.add(num)
        return True