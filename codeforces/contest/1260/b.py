t = int(input())
ans = []
for _ in range(t):
    a, b = map(int, input().split())
    if (a * 2) < b or (b * 2) < a or (a + b) % 3 != 0:
        ans.append('NO')
    else:
        if a and b:
            ans.append('YES')
        elif not a and not b:
            ans.append('YES')
        else:
            ans.append('NO')
print('\n'.join(ans))
