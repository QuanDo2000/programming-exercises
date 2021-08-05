n = int(input())
s = input()
a, b = 0, 0
prev = s[0]
for i in range(1, n):
    char = s[i]
    if char != prev:
        if prev == 'F':
            b += 1
        elif prev == 'S':
            a += 1
    prev = char
if a > b:
    print('YES')
else:
    print('NO')
