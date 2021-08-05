n, k = map(int, input().split())
s = input()
k = set(input().split())
count = 0
ans = 0
for char in s:
    if char in k:
        count += 1
    else:
        ans += (count * (count + 1)) / 2
        count = 0
ans += (count * (count + 1)) / 2
print(int(ans))
