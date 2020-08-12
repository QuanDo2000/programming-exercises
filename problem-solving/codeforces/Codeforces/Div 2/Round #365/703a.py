n = int(input())
m, c = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        m += 1
    elif b > a:
        c += 1
if m == c:
    print('Friendship is magic!^^')
elif m > c:
    print('Mishka')
else:
    print('Chris')
