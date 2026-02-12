class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
            rows, cols = set(), set()
            for r, row in enumerate(matrix):
                for c, n in enumerate(row):
                    if not n:
                        rows.add(r)
                        cols.add(c)
            print(rows, cols)
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if i in rows or j in cols: matrix[i][j] = 0
S = Solution()
ma = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
S.setZeroes(ma)
print(ma)