from collections import defaultdict


DEBUG = False


# def dfs_map(x):
#     global count, tree, orig, adj_list, n, visited
#     count += 1
#     tree[x] = count
#     orig[count] = x
#     visited[x] = 1

#     connected = adj_list[x]

#     if DEBUG:
#         print(count, x, connected)

#     for (i, val) in connected:
#         if visited[i] == 0 and val != 0:
#             dfs_map(i)

#     high[x] = count


def not_dfs():
    global tree, orig, adj_list, n, visited

    stack = [0]
    count = -1

    while stack:
        x = stack.pop()
        if visited[x] == 0:
            count += 1
            tree[x] = count
            orig[count] = x
            visited[x] = 1
            stack.append(x)
        else:
            high[x] = count

        connected = adj_list[x]
        for (i, val) in connected:
            if visited[i] == 0 and val != 0:
                stack.append(i)


def dups(arr):
    tal = defaultdict(list)
    for i, item in arr:
        tal[item].append(i)
    return [locs for key, locs in tal.items() if len(locs) > 1 and key != 0]


def sol():
    global tree, orig, adj_list, n, visited, high, d
    for root in range(n):
        root_orig = orig[root]
        duplicates = dups(adj_list[root_orig])
        if len(duplicates) > 0:
            connected = [item for l in duplicates for item in l]
        else:
            connected = []

        if DEBUG:
            print(root, root_orig)
            print(connected)
            print(d)

        for node in connected:
            idx = tree[node]
            if idx < root:
                lo = 0
                hi = root - 1
                lo1 = high[root_orig] + 1
                hi1 = n
                if DEBUG:
                    print(lo, hi, lo1, hi1)
            else:
                lo = idx
                hi = high[node]
                if DEBUG:
                    print(lo, hi)
            d[lo] += 1
            d[hi + 1] -= 1
            if idx < root and lo1 <= n - 1:
                d[lo1] += 1
                d[hi1] -= 1
            if DEBUG:
                print(idx, hi)


n = int(input())

tree = [0] * n
orig = [0] * n
visited = [0] * n
high = [0] * n
d = [0] * (n + 1)

adj_list = [[(i, 0)] for i in range(n)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    adj_list[a - 1].append((b - 1, c))
    adj_list[b - 1].append((a - 1, c))

if DEBUG:
    print(n)
    print(*adj_list, sep='\n')

# count = -1
# dfs_map(0)
not_dfs()

sol()
s = [0] * n
s[0] = d[0]
for i in range(1, n):
    s[i] = s[i - 1] + d[i]

if DEBUG:
    print(tree, orig, high, sep='\n')
    print(d)
    print(s)

ans = [orig[i] + 1 for i, val in enumerate(s) if val == 0]
ans.sort()

print(len(ans))
print(*ans, sep='\n')
