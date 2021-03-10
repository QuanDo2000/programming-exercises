"""
ID: 25
Name: 1000-digit Fibonacci number
Description:
    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
Link: https://projecteuler.net/problem=25
"""


import time


if __name__ == "__main__":
    n_digits = int(input('Enter amount of digits: '))

    start = time.time_ns()

    prev_f = 1
    curr_f = 1
    curr_idx = 2
    while len(str(curr_f)) < n_digits:
        next_f = curr_f + prev_f
        prev_f = curr_f
        curr_f = next_f
        curr_idx += 1
    print('The index of the first term in Fibonacci sequence with {} digits is {}'.format(
        n_digits, curr_idx))

    time_diff = (time.time_ns() - start) / 1000000
    if time_diff < 1e3:
        print('Time taken: {:.4} ms'.format(time_diff))
    else:
        print('Time taken: {:.4} s'.format(time_diff / 1000))
