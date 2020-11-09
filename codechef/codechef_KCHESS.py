"""
CodeChef Problem: KCHESS
https://www.codechef.com/problems/KCHESS
"""

# Check if position is being checked


def check(knight_pos, pos):
    x = pos[0]
    y = pos[1]
    result = (x + 1, y + 2) in knight_pos or (x + 1, y - 2) in knight_pos \
        or (x - 1, y + 2) in knight_pos or (x - 1, y - 2) in knight_pos \
        or (x + 2, y + 1) in knight_pos or (x + 2, y - 1) in knight_pos \
        or (x - 2, y + 1) in knight_pos or (x - 2, y - 1) in knight_pos
    return result


# Loop test cases
for _ in range(int(input())):
    n = []
    # Get position of all knights
    for i in range(int(input())):
        n.append(tuple(map(int, input().split())))
    # Get position of king
    k = tuple(map(int, input().split()))
    a = k[0]
    b = k[1]
    # All possible move for king
    kingP = [k, (a + 1, b), (a + 1, b + 1), (a + 1, b - 1), (a, b + 1),
             (a, b - 1), (a - 1, b + 1), (a - 1, b), (a - 1, b - 1)]
    # Check all position, if any is not checked then return 'NO'
    for pos in kingP:
        if not check(n, pos):
            print("NO")
            break
    else:
        print("YES")
