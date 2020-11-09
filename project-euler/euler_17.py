"""
ID: 17
Name: Number letter counts
Description:
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
Link: https://projecteuler.net/problem=17
"""


def num2let(num):
    num_map = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
               10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
               20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 80: 'eighty'}

    if num in num_map:
        return num_map[num]
    ret = []
    tens_str = str(num)[-2:]
    tens = int(tens_str)
    digit_2 = tens_str[-2]
    digit_1 = tens_str[-1]
    if tens in num_map:
        ret.append(num_map[tens])
    else:
        digit_20 = digit_2 + '0'
        ret.append(num_map[int(digit_1)])
        if int(digit_20) in num_map:
            ret.append(num_map[int(digit_20)])
        else:
            ret.append(num_map[int(digit_2)] + 'ty')
    if num >= 100:
        if tens_str != '00':
            ret.append('and')
        digit_3 = str(num)[-3]
        if digit_3 != '0':
            ret.append('hundred')
        ret.append(num_map[int(digit_3)])
    if num == 1000:
        digit_4 = str(num)[-4]
        ret.append('thousand')
        ret.append(num_map[int(digit_4)])
    return ''.join(reversed(ret))


def count_letter(num):
    num_map = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
               10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
               20: 6, 30: 6, 40: 5, 50: 5, 80: 6}

    if num in num_map:
        return num_map[num]
    ret = 0
    tens_str = str(num)[-2:]
    tens = int(tens_str)
    digit_2 = tens_str[-2]
    digit_1 = tens_str[-1]
    if tens in num_map:
        ret += num_map[tens]
    else:
        digit_20 = digit_2 + '0'
        if int(digit_20) in num_map:
            ret += num_map[int(digit_20)]
        else:
            ret += num_map[int(digit_2)]
            ret += 2
        ret += num_map[int(digit_1)]
    if num >= 100:
        digit_3 = str(num)[-3]
        if digit_3 != '0':
            ret += 7
        ret += num_map[int(digit_3)]
        if tens_str != '00':
            ret += 3
    if num == 1000:
        digit_4 = str(num)[-4]
        ret += num_map[int(digit_4)]
        ret += 8
    return ret


def count_letter_range(lim):
    ret = 0
    for num in range(1, lim + 1):
        diff = count_letter(num)
        ret += diff
        print(num, ret, diff, num2let(num))
    return ret


lim = int(input('Enter upper limit: '))
res = count_letter_range(lim)
print('The sum of all letters is {}'.format(res))
