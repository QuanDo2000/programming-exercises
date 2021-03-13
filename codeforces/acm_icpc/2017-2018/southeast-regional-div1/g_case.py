import random

n = 20000

with open('./g.inp', 'w') as f:
    print(n, file=f)
    print()
    val = 1
    for i in range(3, n // 2):
        # random.randint(1, n)
        if i != n // 2:
            val += 1
        print(i, i + 1, val, file=f)
