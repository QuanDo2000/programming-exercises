import math


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a = a[::-1]
    side = a[0]
    for i in range(len(a)):
        if i + 1 == a[i]:
            print(a[i])
            break
        elif i + 1 > a[i]:
            print(i)
            break
