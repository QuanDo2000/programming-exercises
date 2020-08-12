# CodeChef Problem: CLIPLX
# https://www.codechef.com/problems/CLIPLX

# Loop test cases
for _ in range(int(input())):
    # Input
    # x for number of points to win
    # y for remaining match
    x, y = map(int, input().split())
    # If x <= y then only need to tie x match to qualify
    # If x > y then need win (x - y) match to qualify
    print(max(0, x - y))
