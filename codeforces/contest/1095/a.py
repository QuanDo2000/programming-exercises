n = int(input())
t = input()
num = 1
i = 0
ans = ''
while i < n:
    ans += t[i]
    i += num
    num += 1
print(ans)
