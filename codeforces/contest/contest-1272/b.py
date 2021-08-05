q = int(input())
for _ in range(q):
    s = list(input())
    l, r, u, d = 0, 0, 0, 0
    for char in s:
        if char == 'L':
            l += 1
        if char == 'R':
            r += 1
        if char == 'U':
            u += 1
        if char == 'D':
            d += 1
    ans = [l + r + u + d, '']
    diff_lr = abs(l - r)
    diff_ud = abs(u - d)
    ans[0] -= diff_lr + diff_ud
    if r < l:
        l = r
    else:
        r = l
    if u < d:
        d = u
    else:
        u = d
    ans[1] = 'L' * l + 'D' * d + 'R' * r + 'U' * u
    if (u == 0) or (l == 0):
        ans[0] = 2
        if u == 0:
            ans[1] = 'LR'
        else:
            ans[1] = 'UD'
    if u == 0 and l == 0:
        ans[0] = 0
        ans[1] = ''
    print(*ans, sep='\n')
