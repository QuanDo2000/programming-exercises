n = int(input())
state = False
ans = ''
for _ in range(n):
    row = input()
    if row[:2] == 'OO' and not state:
        ans += '++'
        state = True
    else:
        ans += row[:2]
    ans += '|'
    if row[-2:] == 'OO'and not state:
        ans += '++'
        state = True
    else:
        ans += row[-2:]
    ans += '\n'
if '+' in ans:
    print('YES')
    print(ans)
else:
    print('NO')
