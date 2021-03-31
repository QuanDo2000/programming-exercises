n = int(input())

ops = []
for _ in range(n):
    op, num = input().split()
    ops.append((op, int(num)))

res = 0
state = True
for i in range(1, 101):
    num = i
    for op in ops:
        if op[0] == 'ADD':
            num += op[1]
        elif op[0] == 'SUBTRACT':
            num -= op[1]
        elif op[0] == 'MULTIPLY':
            num *= op[1]
        elif op[0] == 'DIVIDE':
            num /= op[1]
        if num - int(num) != 0 or num < 0:
            res += 1
            break
print(res)
