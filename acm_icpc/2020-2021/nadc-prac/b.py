EPS = 1e-9


d = int(input())
r = int(input())
t = int(input())


for rt in range(4, r + 1):
    rhs = rt * rt + rt - 9 + (d * d - 2 * rt * d - d) / 2
    if abs(rhs - (r + t)) < EPS:
        x = r - (((rt + 4) * (rt - 3)) / 2)
        if abs(x - int(x)) < EPS:
            print(int(x))
            break
