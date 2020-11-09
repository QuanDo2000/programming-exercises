n = int(input())
res = 0
while n:
    if n >= 100:
        res += n // 100
        n %= 100
    elif n >= 20:
        res += n // 20
        n %= 20
    elif n >= 10:
        res += n // 10
        n %= 10
    elif n >= 5:
        res += n // 5
        n %= 5
    else:
        res += n
        n = 0
print(res)
