n = int(input())
p = list(map(int, input().split()))
res = [0] * n
for i in range(n):
    res[p[i] - 1] = str(i + 1)
print(' '.join(res))
