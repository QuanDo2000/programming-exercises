class Solution:
    def diagonalSort(self, mat: list) -> list:
        diag_map = {}
        n_rows = len(mat)
        n_cols = len(mat[0])
        for row_idx in range(n_rows):
            for col_idx in range(n_cols):
                diff = row_idx - col_idx
                curr_val = mat[row_idx][col_idx]
                if diff not in diag_map:
                    diag_map[diff] = [curr_val]
                else:
                    diag_map[diff].append(curr_val)
        for key in diag_map.keys():
            diag_map[key].sort(reverse=True)

        for row_idx in range(n_rows):
            for col_idx in range(n_cols):
                diff = row_idx - col_idx
                mat[row_idx][col_idx] = diag_map[diff].pop()
        return mat
