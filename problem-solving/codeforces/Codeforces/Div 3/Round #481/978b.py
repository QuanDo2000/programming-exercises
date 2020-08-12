n = int(input())
s = input()
ans = 0
count = 0
for char in s:
    if char == 'x':
        count += 1
        if count >= 3:
            ans += 1
    else:
        count = 0
print(ans)
