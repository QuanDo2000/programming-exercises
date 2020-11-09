class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list) -> int:
        tb_view = [max(x) for x in zip(*grid)]
        lr_view = [max(x) for x in grid]
        ans = 0
        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                tb = tb_view[col_index]
                lr = lr_view[row_index]
                ans += min(tb, lr) - grid[row_index][col_index]
        return ans


sol = Solution()
ans = sol.maxIncreaseKeepingSkyline([[3, 0, 8, 4],
                                     [2, 4, 5, 7],
                                     [9, 2, 6, 3],
                                     [0, 3, 1, 0]])
print(ans)
