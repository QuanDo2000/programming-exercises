n = int(input())
s = input()
d = {'z': 0, 'n': 0}
res = []
for char in s:
    if char == 'z':
        d[char] += 1
    elif char == 'n':
        d[char] += 1
for i in range(d['n']):
    res.append('1')
for i in range(d['z']):
    res.append('0')
print(' '.join(res))
