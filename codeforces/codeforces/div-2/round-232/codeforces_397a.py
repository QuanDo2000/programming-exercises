used = [0] * 100
n = int(input())
l, r = map(int, input().split())
for _ in range(n-1):
    a, b = map(int, input().split())
    for i in range(a, b):
        used[i] = 1
print(used[l:r].count(0))
