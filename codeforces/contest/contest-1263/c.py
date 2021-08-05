def main():
    n = int(input())
    num = n // 2
    ans = [0, 1]
    prev = 1
    l = 2
    while num > 0:
        temp = n // num
        # print(num, temp)
        if temp != prev:
            l += 1
            # prev = num
            prev = temp
            ans.append(temp)
            num = n // (temp + 1)
            # print(prev - num)
        else:
            num -= 1
    print(l)
    print(*ans)


t = int(input())
for _ in range(t):
    main()
