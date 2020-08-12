n = int(input())
s = input()
count = 0
ans = []
for char in s:
    if char == 'B':
        count += 1
    else:
        if count != 0:
            ans.append(count)
        count = 0
if count != 0:
    ans.append(count)
print(len(ans))
if len(ans) != 0:
    print(*ans)
