# http://www.pythonchallenge.com/pc/return/uzi.html
# Page image shows a calendar
# The year is missing 2 middle number, 1xx6
# Day Jan 26 is circled
# Febuary in the right corner has 29 days => leap year
# The year's Jan 1st is a Thursday
# Page source says 'he ain't the youngest, he is the second'
# and 'todo: buy flowers for tomorrow' => Birthday?
# Title 'whom?'

import datetime
import calendar

result = []
# Find year in range 1006 to 1996
# Look for leap year

for year in range(1006, 1996, 10):
    d = datetime.date(year, 1, 26)
    if d.isoweekday() == 1 and calendar.isleap(year):
        result.append(d)

# Get second nearest year
print(result[-2])
# That date is Mozart's birthday
# Answer: mozart
