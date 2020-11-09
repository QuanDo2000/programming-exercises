t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    temp = []
    cont = -1
    for at, bt in zip(a, b):
        diff = bt - at
        if diff < 0:
            print('NO')
            break
        elif diff > 0:
            if cont != -1:
                if cont != diff:
                    print('NO')
                    break
            else:
                if temp:
                    print('NO')
                    break
                else:
                    cont = diff
                    temp.append(diff)
        else:
            cont = -1
    else:
        print('YES')
