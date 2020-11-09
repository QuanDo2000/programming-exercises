def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    # ans = [0] * n

    ans = 0
    s = [0] * m
    for i in range(n):
        s[i % m] += a[i]
        ans += s[i % m]
        print(ans, end=' ')

    # pen = 0
    # for i in range(n):
    #     if i % m == 0:
    #         pen += 1
    #     # print(a[i], pen)
    #     ans[-1] += a[i] * pen
    # # print(ans[-1])
    # for i in range(2, n+1):
    #     ans[-i] = ans[-(i-1)] - sum(a[i-2::m])

    # for i in range(1, n+1):
    #     ans.append(0)
    #     pen = 1
    #     index = 1
    #     for j in a[-i:]:
    #         ans[i-1] += j * pen
    #         if index % m == 0:
    #             index = 1
    #             pen += 1
    #         else:
    #             index += 1
    # print(a)
    # print(' '.join([str(x) for x in ans]))


main()
