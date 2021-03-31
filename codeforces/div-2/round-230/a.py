d = {'n': 0, 'i': 0, 'e': 0, 't': 0}
s = input()
for char in s:
    if char in ['n', 'i', 'e', 't']:
        d[char] += 1
print(max(0, min((d['n']-1)//2, d['i'], d['e']//3, d['t'])))
