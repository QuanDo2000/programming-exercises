n = int(input())
index = 0
c = {}
l = []
r = []

for i in range(n):
    name, score = input().split()
    score = int(score)
    if r:
        temp = r[-1].copy()
        r.append(temp)
    else:
        r.append([])
    if name not in c:
        c[name] = [index, score]
        index += 1
        l.append([(i, score)])
        r[i].append(score)
    else:
        l[c[name][0]].append((i, score))
        c[name][1] += score
        r[i][c[name][0]] += score

last = r[-1]
maxp = max(last)
win = []
for i in range(len(r[-1])):
    if r[-1][i] == maxp:
        win.append(i)
index = -1
for i in range(len(r)):
    for j in range(len(r[i])):
        if r[i][j] >= maxp and j in win:
            index = j
            break
    if index != -1:
        break
ans = ''
for name, data in c.items():
    if data[0] == index:
        ans = name
        break
print(ans)
