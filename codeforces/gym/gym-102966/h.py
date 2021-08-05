

def ncr(n, r, p=(10 ** 9 + 7)):
    num = dens[n]
    den = dens[r] * dens[n - r] % p
    return (num * pow(den,
                      p - 2, p)) % p


t = int(input())

ns = []
hi = -1
for _ in range(t):
    n = int(input())
    ns.append(n)
    if n > hi:
        hi = n

hi = 2 * hi - 1
dens = [1] * (hi + 1)
for i in range(2, hi + 1):
    dens[i] = (dens[i - 1] * i) % (10 ** 9 + 7)
# print(dens)

for n in ns:
    print(ncr(2 * n - 1, n))
