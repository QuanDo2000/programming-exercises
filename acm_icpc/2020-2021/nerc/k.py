n = int(input())
mi = 10e5 + 1
ans = -1
for i in range(n):
    p, s = input().split()
    p = int(p)
    if s.count("2") >= 2 and s.count("1") >= 1 and s.count("0") >= 1 and (ans == -1 or mi > p):
        ans = i + 1
        mi = p
if ans == -1:
    print(0)
else:
    print(ans)
