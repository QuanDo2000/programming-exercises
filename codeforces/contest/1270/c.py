t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    x = 0
    for i in range(n):
        x = x ^ a[i]
    diff = abs(x * 2 - s)
    if x * 2 == s:
        print('0\n')
    elif x == 0:
        print('1')
        print('{}'.format(s))
    else:
        print('2')
        print('{} {}'.format(x, s + x))
