n = int(input())
s = input()

stack = [0]
temp = []
arr = [0] * (n + 1)

for i, char in enumerate(s):
    # print(temp, stack, arr)
    if char != '(' and char != ')':
        temp.append(char)
    if char == '(' or char == ')':
        if len(temp) != 0:
            stack.append(int(''.join(temp)))
        arr[stack[-1]] = stack[-2]
        temp = []
    if char == ')':
        stack.pop()
print(*arr[1:])
