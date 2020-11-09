t = int(input())
ans = []
for _ in range(t):
    r, g, b = map(int, input().split())
    c = sorted([r, g, b])
    if c[0] + c[1] > c[2]:
        temp = (c[0] + c[1] - c[2]) // 2
        ans.append(c[2] + temp)
    else:
        ans.append(c[0] + c[1])
print('\n'.join([str(x) for x in ans]))
