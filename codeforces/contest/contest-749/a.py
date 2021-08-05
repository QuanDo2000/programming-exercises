n = int(input())
print(n // 2)
print('2 ' * ((n // 2) - 1), end='')
if n % 2 != 0:
    print('3')
else:
    print('2')
