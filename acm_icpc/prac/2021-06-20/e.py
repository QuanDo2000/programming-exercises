import sys

input = sys.stdin.readline


def gen_state(n):
    ret = []

    def rec(k, state=0):
        if k == n:
            ret.append(state)
            return
        for digit in [0, 1]:
            if digit == 1 and k > 0 and state & 1 == 1:
                continue
            rec(k + 1, (state << 1) + digit)
    rec(0)
    return ret


def get_score(grid, i, state):
    line = grid[i]
    res = 0
    for idx in range(len(line)):
        if (state >> idx) & 1 == 1:
            res += grid[i][idx]
    return res


def check_state(state0, state1):
    return (state0 & state1) == 0 and (state0 & state1 << 1) == 0 and (state0 & state1 >> 1) == 0


t = int(input())

states = [[] for _ in range(16)]
pair = [{} for _ in range(16)]
for i in range(1, 16 + 1):
    states[i - 1] = gen_state(i)
    for state in states[i - 1]:
        pair[i - 1][state] = []
        for up_state in states[i - 1]:
            if check_state(up_state, state):
                pair[i - 1][state].append(up_state)

for _ in range(t):
    n = int(input())
    grid = []
    for _ in range(n):
        line = list(map(int, input().split()))
        grid.append(line)

    f = [[0 for _ in range(2 ** 16 + 1)] for _ in range(n)]
    for i in range(n):
        for state in states[n - 1]:
            if i == 0:
                f[i][state] = get_score(grid, i, state)
            else:
                f[i][state] = 0
                base = get_score(grid, i, state)
                for up_state in pair[n - 1][state]:
                    f[i][state] = max(f[i][state], base + f[i - 1][up_state])

    ans = max(f[n - 1])
    print(ans)
