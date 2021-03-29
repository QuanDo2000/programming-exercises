from random import randint

n = 100000
k = 100

with open('./c.inp', 'w') as f:
    print(n, k, file=f)
    for i in range(n - 1):
        print(i + 1, i + 2, 1, file=f)
    for _ in range(k):
        print(randint(1, n), end=' ', file=f)
