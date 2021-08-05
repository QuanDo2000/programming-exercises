t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    bit = [0] * n
    for i in range(n):
        if int(s[i]) % 2 == 0:
            bit[i] = 1
    if bit.count(1) == n:
        print(-1)
    elif bit.count(0) == n and n % 2 == 0:
        ans = ''.join([str(x) for x in s])
        ans = int(ans)
        print(ans)
    else:
        i = n - bit[::-1].index(0)
        s = s[:i]
        bit = bit[:i]
        odd = bit.count(0)
        eve = bit.count(1)
        if odd % 2 == 0:
            ans = ''.join([str(x) for x in s])
        else:
            s.remove(s[bit.index(0)])
            ans = ''.join([str(x) for x in s])
        if ans == '':
            ans = -1
        elif odd == 1:
            ans = -1
        print(int(ans))
