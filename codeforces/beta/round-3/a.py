chars = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

s = input()
t = input()
s = (int(chars[s[0]]), int(s[1]))
t = (int(chars[t[0]]), int(t[1]))
x = t[0] - s[0]
y = t[1] - s[1]
ans = []
ansx = ['L'] * abs(min(0, x)) + ['R'] * abs(max(0, x))
ansy = ['D'] * abs(min(0, y)) + ['U'] * abs(max(0, y))
print(max(len(ansx), len(ansy)))
while ansx and ansy:
    print(ansx[0], ansy[0], sep='')
    ansx.pop(0)
    ansy.pop(0)
if ansx:
    print(*ansx, sep='\n')
elif ansy:
    print(*ansy, sep='\n')
