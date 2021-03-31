n, v = map(int, input().split())
temp = {1: [], 2: []}
s = {1: [0], 2: [0]}
for i in range(n):
    x, y = map(int, input().split())
    temp[x].append([y, i+1])
temp[1].sort(reverse=True)
temp[2].sort(reverse=True)
# print(temp[1])
# print(temp[2])

for i in range(min(v, len(temp[1]))):
    s[1].append(s[1][-1] + temp[1][i][0])
for i in range(min((v//2), len(temp[2]))):
    s[2].append(s[2][-1] + temp[2][i][0])
ans = 0
num = 0
# print(s[1])
# print(s[2])

for i in range(min(v, len(temp[1])) + 1):
    t = s[1][i] + s[2][min(len(temp[2]), ((v-i)//2))]
    # print(t)
    if ans < t:
        num, ans = i, t
print(ans)
for i in range(num):
    print(temp[1][i][1], end=' ')
for i in range(min(len(temp[2]), (v-num)//2)):
    print(temp[2][i][1], end=' ')
