n = int(input())
a = list(map(int, input().split()))
ans = 1
for num in a:
    ans = max(ans, a.count(num))
print(ans)
