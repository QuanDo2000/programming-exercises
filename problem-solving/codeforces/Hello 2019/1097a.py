d = input()
h = input().split()
for i in h:
    if i[0] == d[0]:
        print('YES')
        break
    if i[1] == d[1]:
        print('YES')
        break
else:
    print('NO')
