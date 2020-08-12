n = int(input())
a = list(map(int, input().split()))
ans = 0
s = max(a)
for num in a:
    ans += abs(s-num)
print(ans)
