n, p, k = map(int, input().split())
res = ''
l = ' '.join(list(map(str, range(max(p-k, 1), p))))
r = ' '.join(list(map(str, range(p+1, min(p+k+1, n+1)))))
if p-k > 1:
    res += '<< '
if l:
    res += l + ' '
res += '({})'.format(p)
if r:
    res += ' ' + r
if p+k < n:
    res += ' >>'
print(res)
