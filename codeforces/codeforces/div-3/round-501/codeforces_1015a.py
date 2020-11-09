n, m = map(int, input().split())
ans = [x for x in range(1, m+1)]
for _ in range(n):
    l, r = map(int, input().split())
    for i in range(l, r+1):
        if i in ans:
            ans.remove(i)
print(len(ans))
print(*ans)
