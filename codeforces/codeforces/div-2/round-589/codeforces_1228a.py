l, r = map(int, input().split())
for i in range(l, r+1):
    num = []
    for index in range(len(str(i))):
        if str(i)[index] not in num:
            num.append(str(i)[index])
        else:
            break
    else:
        print(i)
        break
else:
    print(-1)
