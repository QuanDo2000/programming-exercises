moves = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]

board = ["",
         " ............",
         " ............",
         " ..*......*..",
         " ............",
         " ............",
         " .....##.....",
         " .....##.....",
         " ............",
         " .##......##.",
         " .#*......*#.",
         " ............",
         " ............"]

l = int(input())
pos = []
for _ in range(l):
    pos.append(tuple(map(int, input().split())))

for r, c in pos:
    visited = [[False for _ in range(13)] for _ in range(13)]
    queue = []
    queue.append((r, c, ''))
    visited[r - 1][c - 1] = True
    a, b = r, c
    while queue:
        # print(queue)
        a, b, path = queue.pop(0)
        visited[a][b] = True
        if board[a][b] == '*':
            print(len(path))
            print(path)
            break
        for i in range(4):
            x = a + moves[i][0]
            y = b + moves[i][1]
            temp = moves[i][2]
            if (not (x < 1 or y < 1 or x > 12 or y > 12)) and board[x][y] != '#' and not visited[x][y]:
                queue.append((x, y, path + temp))
