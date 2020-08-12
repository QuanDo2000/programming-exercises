# CodeChef Problem: ROBOGAME
# https://www.codechef.com/problems/ROBOGAME

# Loop test cases
for _ in range(int(input())):
    # Get config
    s = list(input())
    r = []
    safe = True
    # Get position of robot
    for i in range(len(s)):
        if s[i] != '.':
            r.append(i)
    # Check if distance between robot is smaller than sum of their range
    for i in range(len(r)-1):
        if ((r[i+1] - r[i]) <= (int(s[r[i+1]]) + int(s[r[i]]))):
            safe = False
    if safe:
        print("safe")
    else:
        print("unsafe")
