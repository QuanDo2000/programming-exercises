t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n - 1)
    for i in range(n-1):
        b[i] = a[i+1] - a[i]
        if abs(b[i]) >= 2:
            print('YES')
            print('{} {}'.format(i+1, i+2))
            break
    else:
        print('NO')
