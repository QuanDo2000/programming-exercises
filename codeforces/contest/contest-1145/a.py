n = int(input())
a = list(map(int, input().split()))


def q(t): return t > sorted(t) and q(t[::2]) or t


def m(t):
    if t == sorted(t):
        return len(t)
    else:
        return max(m(t[:len(t)//2]), m(t[len(t)//2:]))


print(m(a))
