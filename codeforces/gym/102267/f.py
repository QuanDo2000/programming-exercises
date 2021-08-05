import math


def topoSort(graph, v, visited, stack, n):
    # print(visited, stack)
    visited[v] = 1
    for i in range(n):
        if graph[v][i] == 1:
            if visited[i] == 0:
                topoSort(graph, i, visited, stack, n)
            if visited[i] == 1:
                return -1
    visited[v] = 2
    stack.append(v + 1)


n = int(input())
fighters = []
for _ in range(n):
    x, y, a, r = map(int, input().split())
    fighters.append((x, y, a, r))

graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x = fighters[j][0] - fighters[i][0]
        y = fighters[j][1] - fighters[i][1]
        a = fighters[i][2]
        r = fighters[i][3]
        angle = math.degrees(math.atan2(y, x))
        if angle < 0:
            angle += 360
        print(i, j, angle)
        lo = a - r
        if lo < 0:
            lo += 360
        hi = a + r
        if hi > 359:
            hi -= 360
        if angle >= lo and angle <= hi:
            graph[i][j] = 1


visited = [False] * n
stack = []

for i in range(n):
    if visited[i] == False:
        status = topoSort(graph, i, visited, stack, n)

if status == -1:
    print(-1)
else:
    print(*stack[::-1])
