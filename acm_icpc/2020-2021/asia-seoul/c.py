DEBUG = False


def rec(node, prev):
    global visited, ans, adj_list, cs, apts, k

    visited[node] = 1
    count = 0
    if node + 1 in apts:
        cs[node] = 1
        ans[node] = 1
    for edges in adj_list[node]:
        nxt = edges[0]
        if visited[nxt] != 1:
            temp = rec(nxt, node)
            cs[node] += temp
            if temp > 0:
                count += 1
    if k - cs[node] > 0:
        count += 1
    if count > 1:
        ans[node] = 1

    return cs[node]


def not_rec():
    global visited, ans, adj_list, cs, apts, k, children
    stack = [0]
    while stack:
        node = stack.pop()
        sec = False

        if visited[node] == 0:
            visited[node] = 1
            stack.append(node)
        else:
            sec = True
        count = 0
        if node + 1 in apts:
            cs[node] = 1
            ans[node] = 1
        for edges in adj_list[node]:
            nxt = edges[0]
            if visited[nxt] == 0:
                stack.append(nxt)
                children[node].append(nxt)
        if sec:
            for child in children[node]:
                cs[node] += cs[child]
                if cs[child] > 0:
                    count += 1
            if k - cs[node] > 0:
                count += 1
            if count > 1:
                ans[node] = 1


n, k = map(int, input().split())

adj_list = [[] for _ in range(n)]
for _ in range(n - 1):
    i, j, w = map(int, input().split())
    adj_list[i - 1].append((j - 1, w))
    adj_list[j - 1].append((i - 1, w))

apts = set(map(int, input().split()))

if DEBUG:
    print(n, k)
    print(adj_list)
    print(apts)

ans = [0] * n
visited = [0] * n
cs = [0] * n
children = [[] for _ in range(n)]

not_rec()

if DEBUG:
    print(max(apts) - min(apts) + 1)
    # print(ans)
    # print(cs)
print(ans.count(1))
