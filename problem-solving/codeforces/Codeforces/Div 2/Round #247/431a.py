a = list(map(int, input().split()))
s = list(map(int, list(input())))
ans = 0
for num in s:
    ans += a[num-1]
print(ans)
