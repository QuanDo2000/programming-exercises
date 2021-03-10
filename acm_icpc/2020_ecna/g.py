n, m = map(int, input().split())

d = {}
for i in range(n):
    d['T{}'.format(i + 1)] = i
ls = ['T{}'.format(i) for i in range(1, n + 1)]


for i in range(m):
    w, l = input().split()
    if d[w] > d[l]:
        lo, hi = d[l], d[w]
        for j in range(lo, hi):
            # print(j, ls[j])
            d[ls[j]] += 1
            d[ls[j + 1]] -= 1
            ls[j], ls[j + 1] = ls[j + 1], ls[j]

ans = sorted(d.items(), key=lambda item: item[1])
for i in range(len(ans)):
    print(ans[i][0], end=' ')
