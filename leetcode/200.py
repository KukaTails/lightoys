class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or len(grid) == 0: return 0
        self.rows, self.columns = len(grid), len(grid[0])
        self.grid = grid
        self.parent = [[-1] * self.columns for i in range(self.rows)]
        self.visited = [[0] * self.columns for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                if grid[i][j] == '1':
                    self.search(None, None, i, j)
        count = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if grid[i][j] == '1' and self.parent[i][j] == -1:
                    count += 1
        return count


    def search(self, pre_i, pre_j, i, j):
        if i < 0 or i >= self.rows or j < 0 or j >= self.columns:
            return
        if self.grid[i][j] == '0' or self.visited[i][j]:
            return
        self.visited[i][j] = 1
        if pre_i != None and pre_j != None:
            self.union(pre_i, pre_j, i, j)
        self.search(i, j, i+1, j)
        self.search(i, j, i-1, j)
        self.search(i, j, i, j+1)
        self.search(i, j, i, j-1)

    def union(self, lhs_i, lhs_j, rhs_i, rhs_j):
        lhs_father = self.find(lhs_i, lhs_j)
        rhs_father = self.find(rhs_i, rhs_j)
        if lhs_father != rhs_father:
            if lhs_father < rhs_father:
                i = lhs_father // self.columns
                j = lhs_father % self.columns
                self.parent[i][j] = rhs_father
                return self.parent[i][j]
            else:
                i = rhs_father // self.columns
                j = rhs_father % self.columns
                self.parent[i][j] = lhs_father
                return self.parent[i][j]

    def find(self, i, j):
        if self.parent[i][j] != -1:
            tmp = self.parent[i][j]
            p_i = tmp // self.columns
            p_j = tmp % self.columns
            p_p = self.find(p_i, p_j)
            self.parent[i][j] = p_p
            return p_p
        return i * self.columns + j


# testing
test_cases = [["111", "010", "111"], ["11110","11010","11000","00000"], ["11000", "11000", "00100", "00011"]]
for test_case in test_cases:
    print(Solution().numIslands(test_case))