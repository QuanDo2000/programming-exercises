t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for num in a:
        if num % 2 != 0:
            count += 1
    if count != n and count >= 1:
        print('YES')
    elif count == n and n % 2 != 0:
        print('YES')
    else:
        print('NO')
