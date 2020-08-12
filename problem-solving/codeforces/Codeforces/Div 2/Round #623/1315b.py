from bisect import bisect_left


t = int(input())
for _ in range(t):
    a, b, p = map(int, input().split())
    s = input()
    n = len(s)
    if p < min(a, b):
        print(n)
    else:
        cost = [0] * n
        prev = s[-2]
        if s[-2] == 'A':
            cost[-2] = a
        else:
            cost[-2] = b
        for i in range(n-3, -1, -1):
            curr = s[i]
            cost[i] = cost[i+1]
            if curr != prev and curr == 'A':
                cost[i] += a
            elif curr != prev and curr == 'B':
                cost[i] += b
            prev = curr
        for i in range(n):
            if cost[i] <= p:
                break
        # print(cost)
        print(i+1)
