# from datetime import datetime
MOD = 10**9 + 7


def main():

    x = int(input())
    s = input()
    ln = len(s)
    key = 0
    for l in range(x):
        num = int(s[l]) - 1
        if num == 0:
            continue
        if ln < x and not key:
            # print(s, s[l+1:])
            s += s[l+1:] * num
        # print(l, ln, end='-')
        # print((ln - l - 1), (int(s[l]) - 1), end='-')
        r = (ln - l - 1) * (num)
        ln += r
        if ln >= MOD:
            key = 1
        ln %= MOD
        # print(r, s[l])
    print(ln % MOD)


# start = datetime.now()
t = int(input())
for _ in range(t):
    main()
# print(datetime.now() - start)
