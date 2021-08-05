for _ in range(int(input())):
    a, b, c = map(int, input().split())
    count = 0
    while b > 0:
        if c > 1:
            b -= 1
            c -= 2
            count += 3
        elif b > 1 and a > 0:
            a -= 1
            b -= 2
            count += 3
        else:
            break
    print(count)
