for _ in range(int(input())):
    s = input()
    t = input()
    char = []
    for i in s:
        if i not in char:
            char.append(i)
    for i in t:
        if i in char:
            print('YES')
            break
    else:
        print('NO')
