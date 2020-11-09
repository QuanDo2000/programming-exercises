digits = '0123456789'


def main():
    n = int(input())
    p = [input() for _ in range(n)]
    s = set()
    step = 0
    for i in range(n):
        num = p[i]
        if num not in s:
            s.add(num)
            continue
        else:
            state = False
            for j in range(4):
                for digit in digits:
                    temp = list(num)
                    temp[j] = digit
                    temp = ''.join(temp)
                    if temp not in s and temp not in p:
                        step += 1
                        s.add(temp)
                        p[i] = temp
                        state = True
                        break
                if state:
                    break
    print(step, *p, sep='\n')


t = int(input())
for _ in range(t):
    main()
