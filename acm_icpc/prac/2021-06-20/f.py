def to_min(t):
    h, m = map(int, t.split(':'))
    return h + (m / 60)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    time = 0
    for __ in range(n):
        start, end = input().split()
        dt = to_min(end) - to_min(start)
        time += dt
    if time >= m:
        print('YES')
    else:
        print('NO')
