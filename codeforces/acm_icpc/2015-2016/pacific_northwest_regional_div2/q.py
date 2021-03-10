n = int(input())

s = []
for _ in range(n):
    s.append(int(input()))

s.sort()

res = None
for i in range(n // 2):
    t = s[i] + s[-i - 1]
    if res == None or t < res:
        res = t
print(res)
