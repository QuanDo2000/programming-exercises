"""
ID: 19
Name: Counting Sundays
Description:
    You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.

    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
Link: https://projecteuler.net/problem=19
"""

import datetime


def check_leap(year):
    """Return if input year is leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def count_first_sundays(start_year, end_year):
    """Return the count of Sundays that happens at the first of the month within a range of years."""
    count = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 12 + 1):
            curr_date = datetime.datetime(year, month, 1)
            if curr_date.weekday() == 6:
                count += 1
    return count


start_year = int(input('Input start year: '))
end_year = int(input('Input end year: '))
ans = count_first_sundays(start_year, end_year)
print('There are {} Sundays that occurs at the start of the month'.format(ans))
