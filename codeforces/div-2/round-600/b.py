def main():
    n = int(input())
    a = list(map(int, input().split()))
    num = 0
    stack = 0
    index = []
    day = set()
    for i in range(n):
        e = a[i]
        if i != 0:
            if not stack:
                day = set()
                if index:
                    index.append(i-num)
                else:
                    index.append(i)
                num = i
        stack += e
        if stack < 0:
            print(-1)
            return
        if e < 0:
            if abs(e) not in day:
                print(-1)
                return
        if e in day:
            print(-1)
            return
        else:
            day.add(e)
    if stack:
        print(-1)
        return
    if index:
        index.append(n-num)
    else:
        index.append(n)
    print(len(index))
    print(' '.join([str(x) for x in index]))


main()
