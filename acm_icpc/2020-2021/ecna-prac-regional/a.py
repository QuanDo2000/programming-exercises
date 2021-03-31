def sum_digits(n):
    ans = 0
    while (n != 0):
        ans += int(n % 10)
        n = int(n / 10)
    return ans


while True:
    n = int(input())
    if n == 0:
        break
    t = sum_digits(n)
    for i in range(11, 101):
        if sum_digits(n * i) == t:
            print(i)
            break
