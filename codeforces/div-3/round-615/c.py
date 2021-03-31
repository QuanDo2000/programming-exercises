import math


t = int(input())
for _ in range(t):
    n = int(input())
    d = []
    temp = n
    while n % 2 == 0:
        d.append(2)
        n //= 2
    for i in range(3, (int(math.sqrt(n)) + 1), 2):
        while n % i == 0:
            d.append(i)
            n //= i
    if n > 2:
        d.append(n)
    if len(d) < 3:
        print('NO')
    elif len(d) == 3 and (d[0] == d[1] or d[1] == d[2]):
        print('NO')
    else:
        # print(d)
        a = d[0]
        if d[1] == d[0]:
            b = d[1] * d[2]
            c = int(temp / (a * b))
        else:
            b = d[1]
            c = int(temp / (a * b))
        if a == b or a == c or b == c:
            print('NO')
        else:
            print('YES')
            print(a, b, c)
