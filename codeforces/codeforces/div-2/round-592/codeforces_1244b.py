for _ in range(int(input())):
    n = int(input())
    s = input()
    if s[0] == '1' or s[-1] == '1':
        print(n*2)
    else:
        a = s.find('1')
        b = s[::-1].find('1')
        if b < a:
            a = b
        if a == -1:
            print(n)
        else:
            print((n-a)*2)
