s, x = map(int, input().split())

div = s // x
i = 1
while div != 0:
    s //= x
    div = s // x
    i += 1
print(i)
