n = int(input())
d = {}
d1 = {}
visit = {}
l1 = []

for i in range(1, n+1):
    d[i] = []
    d1[i] = 0
    visit[i] = False
for i in range(n-2):
    a, b, c = map(int, input().split())
    d[a].append(b)
    d[a].append(c)
    d1[a] += 1
    d[b].append(a)
    d[b].append(c)
    d1[b] += 1
    d[c].append(b)
    d[c].append(a)
    d1[c] += 1
d1 = dict(sorted(d1.items(), key=lambda x: x[1]))
for i in d1:
    if len(l1) == n:
        break
    if not visit[i]:
        visit[i] = True
        l1.append(i)
    x = sorted(d[i], key=lambda x: d1[x])
    for j in x:
        # print(j, x)
        if not visit[j]:
            visit[j] = True
            l1.append(j)
            x += d[j]
print(*l1)

# arr = [[i+1, 0] for i in range(n)]
# for i in range(n-2):
#     temp = list(map(int, input().split()))
#     for num in temp:
#         arr[num-1][1] += 1
# arr = sorted(arr, key=lambda x: x[1])
# ans1 = arr[::2]
# ans2 = arr[1::2][::-1]
# ans = ans1 + ans2
# for i, num in ans:
#     print(i, end=' ')
