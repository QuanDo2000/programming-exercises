def blur(grid, w, h):
    new_grid = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            h_lo = i - 1
            if i + 1 < h:
                h_hi = i + 1
            else:
                h_hi = 0

            w_lo = j - 1
            if j + 1 < w:
                w_hi = j + 1
            else:
                w_hi = 0
            for x in [h_lo, i, h_hi]:
                for y in [w_lo, j, w_hi]:
                    new_grid[i][j] += grid[x][y]
    return new_grid


w, h, b = map(int, input().split())

grid = []
for _ in range(h):
    grid.append(list(map(int, input().split())))

for i in range(b):
    grid = blur(grid, w, h)
# print(grid)

l = [item for sublist in grid for item in sublist]

grid = set(l)
print(len(grid))
