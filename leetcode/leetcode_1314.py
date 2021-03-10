class Solution:
    def matrixBlockSum(self, mat: list, K: int) -> list:
        m = len(mat)
        n = len(mat[0])
        ans = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                l_row = max(0, i - K)
                h_row = min(m, i + K + 1)
                l_col = max(0, j - K)
                h_col = min(n, j + K + 1)
                ans[i][j] = sum([sum(mat[row][l_col:h_col])
                                 for row in range(l_row, h_row)])

        return ans


sol = Solution()
ans = sol.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2)
print(ans)
