def get_line(x, a):
    return (a, x[1] - a * x[0])


def get_intersect(line1, line2):
    if line1[0] == line2[0]:
        if line1[1] == line2[1]:
            return 0
        else:
            return -1
    x = (line2[1] - line1[1]) / (line1[0] - line2[0])
    y = line1[0] * (x) + line1[1]
    return (x, y)


n = int(input())


for _ in range(n):
    x1, x2, y1, y2 = input().split()
    xc1 = ord(x1) - ord('A') + 1
    yc1 = ord(y1) - ord('A') + 1
    x2 = int(x2)
    y2 = int(y2)
    a = (xc1, x2)
    b = (yc1, y2)
    # print(a, b)
    if (sum(a) % 2) != (sum(b) % 2):
        print('Impossible')
        continue
    elif a == b:
        print('0 {} {}'.format(x1, x2))
        continue
    for i in [1, -1]:
        line1 = get_line(a, i)
        line2 = get_line(b, -i)
        line3 = get_line(b, i)
        # print(line1, line2)
        ans = get_intersect(line1, line2)
        # print(ans)
        if line1 == line3:
            ret = '1 {} {} {} {}'.format(x1, x2, y1, y2)
            break
        if ans[0] > 0 and ans[0] < 9 and ans[1] > 0 and ans[1] < 9:
            x, y = chr(int(ans[0]) - 1 + ord('A')), int(ans[1])
            ret = '2 {} {} {} {} {} {}'.format(x1, x2, x, y, y1, y2)
    print(ret)
