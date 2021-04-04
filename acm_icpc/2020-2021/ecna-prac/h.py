def check(ss):
    n = len(ss) // 4
    return ss[:2 * n] == ss[2 * n:] and ss[:n] == ss[2 * n - 1:n - 1:-1]


s = input()
n = len(s)
nmax = n - n % 4

ans = 0
for i in range(2, n - 1):
    for j in range(min(i, n - i) // 2):
        nss = 4 * (j + 1)
        if ans > nss:
            continue
        print(i, 4 * (j + 1))
        ss = s[i - 2 * (j + 1):i + 2 * (j + 1)]
        print(ss)
        if ans < nss and check(ss):
            ans = nss

print(ans)
