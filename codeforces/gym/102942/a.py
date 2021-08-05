res = {
    0: 'E',
    1: 'S',
    2: 'W',
    3: 'N'
}

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    start = 0

    for c in s:
        if c == '0':
            start += 1
        else:
            start -= 1
        start %= 4
    print(res[start])
