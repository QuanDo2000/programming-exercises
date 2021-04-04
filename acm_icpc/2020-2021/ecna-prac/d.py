import sys


def evaluate(exp):
    stack = []
    for c in exp[::-1]:
        # print(c)
        if c not in ['+', '-', '*', '/']:
            stack.append(c)
        else:
            o1 = stack.pop()
            o2 = stack.pop()

            try:
                o1 = int(o1)
                o2 = int(o2)
                b = True
            except:
                b = False

            if c == '+':
                if b:
                    stack.append(str(o1 + o2))
                else:
                    stack.append('+ {} {}'.format(o1, o2))
            elif c == '-':
                if b:
                    stack.append(str(o1 - o2))
                else:
                    stack.append('- {} {}'.format(o1, o2))
            elif c == '*':
                if b:
                    stack.append(str(o1 * o2))
                else:
                    stack.append('* {} {}'.format(o1, o2))
    return stack


for i, line in enumerate(sys.stdin):
    # print(line)
    line = line.split()
    print('Case {}: {}'.format(i + 1, *evaluate(line)))
