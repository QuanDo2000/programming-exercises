# CodeChef Problem: ADAKNG
# https://www.codechef.com/problems/ADAKNG

# Loop test cases
for i in range(int(input())):
    # Input
    # r for row, c for column, k for moves
    r, c, k = map(int, input().split())

    # The squares that the king can go to in k moves is the area
    # of the square with side 2k+1 (in an infinite board)
    # So in a non-infinite board, the squares that the king can
    # go to is a rectangle

    # The width can be calculated by taking the row (r) the king is on
    # add/remove k moves from that. Take the higher minus the lower
    # and plus 1 to get the width. Since the board is finite, if
    # the king's move is invalid then set it to border value.
    height = abs(min(r+k, 8) - max(r-k, 1)) + 1
    # The height is similar to width, replace row (r) with column (c)
    width = abs(min(c+k, 8) - max(c-k, 1)) + 1
    rec = width * height
    print(rec)
