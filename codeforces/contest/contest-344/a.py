n = int(input())
ans = 0
prev = '00'
for _ in range(n):
    s = input()
    if s != prev:
        ans += 1
        prev = s
print(ans)
