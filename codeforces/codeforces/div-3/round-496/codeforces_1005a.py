n = int(input())
a = list(map(int, input().split()))
ans = []
count = 1
for num in a:
    if num == 1:
        ans.append(count)
        count = 1
    else:
        count += 1
ans.append(count)
ans.pop(0)
print(len(ans))
print(*ans)
