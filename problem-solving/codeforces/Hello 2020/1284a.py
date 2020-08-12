n, m = map(int, input().split())
s = input().split()
t = input().split()
q = int(input())

for i in range(q):
    y = int(input())
    y -= 1
    ans = s[y % n] + t[y % m]
    print(ans)
