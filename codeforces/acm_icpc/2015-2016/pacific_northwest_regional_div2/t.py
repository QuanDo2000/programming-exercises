t = []
for _ in range(2):
    t.append(sorted(list(map(int, input().split()))))

for tri in t:
    if (tri[0] ** 2 + tri[1] ** 2) != (tri[2] ** 2):
        print('NO')
        break
else:
    if t[0][0] != t[1][0] or t[0][1] != t[1][1] or t[0][2] != t[1][2]:
        print('NO')
    else:
        print('YES')
