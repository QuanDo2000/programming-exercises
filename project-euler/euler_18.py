"""
ID: 18
Name: Maximum path sum I
Description:
    By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

    "3"
    "7" 4
    2 "4" 6
    8 5 "9" 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
Link: https://projecteuler.net/problem=18
"""


import time


def read_file(input_path):
    with open(input_path, 'r') as f:
        raw_data = f.readlines()
    ret_data = [list(map(int, line.split(' '))) for line in raw_data]
    return ret_data


def sum_triangle(triangle):
    row_len = len(triangle)

    for row_idx in range(row_len - 2, -1, -1):
        row = triangle[row_idx]
        col_len = len(row)
        for col_idx in range(col_len):
            triangle[row_idx][col_idx] += max(
                triangle[row_idx + 1][col_idx], triangle[row_idx + 1][col_idx + 1])
    return triangle


def print_triangle(triangle):
    for row in triangle:
        line = list(map(str, row))
        print(' '.join(line))


if __name__ == "__main__":
    start = time.time_ns()

    triangle = read_file('./data/euler_inp_18.txt')
    print('\nOriginal triangle')
    print_triangle(triangle)
    triangle_mod = sum_triangle(triangle)
    print('\nModified triangle')
    print_triangle(triangle_mod)
    print('\nThe sum of the maximum path is {}'.format(triangle_mod[0][0]))

    time_diff = (time.time_ns() - start) / 1000000
    if time_diff < 1e3:
        print('Time taken: {:.4} ms'.format(time_diff))
    else:
        print('Time taken: {:.4} s'.format(time_diff / 1000))
