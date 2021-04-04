DEBUG = False


n = int(input())

if DEBUG:
    print(n)


for x in range(2, n // 2 + 2):
    for y in range(x - 1, x + 1):
        if x == y and n % x == 0:
            print(x, y)
        else:
            t = n // (x + y)
            for a in range(t - 1, t + 2):
                for b in range(a - 1, a + 1):
                    if x * a + y * b == n:
                        if DEBUG:
                            print(x, y, a, b)
                        print(x, y)
