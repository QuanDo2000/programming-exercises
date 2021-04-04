from collections import deque

m, n = map(int, input().split())

grid = []
for _ in range(m):
    grid.append(input())


def bfs(visited, queue, grid, node):
    visited[node[0]][node[1]] = 1
    queue.append(node)

    while queue:
        s = queue.popleft()
        move = s[2]
        if s[0] == m - 1 and s[1] == n - 1:
            return move

        val = int(grid[s[0]][s[1]])
        for x, y in [(val, 0), (-val, 0), (0, val), (0, -val)]:
            a, b = s[0] + x, s[1] + y
            if a >= 0 and a < m and b >= 0 and b < n:
                next_node = (a, b, move + 1)
                if visited[a][b] == 0:
                    visited[a][b] = 1
                    queue.append(next_node)
    return -1


visited = [[0 for _ in range(n)] for _ in range(m)]
queue = deque()

res = bfs(visited, queue, grid, (0, 0, 0))
if res == -1:
    print('IMPOSSIBLE')
else:
    print(res)
