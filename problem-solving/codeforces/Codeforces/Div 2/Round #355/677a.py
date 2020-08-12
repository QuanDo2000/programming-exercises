n, h = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for num in a:
    if num > h:
        ans += 2
    else:
        ans += 1
print(ans)
