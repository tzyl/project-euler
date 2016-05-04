MONTH_LENGTHS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
                 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

date = 7
month = 1
month_length = MONTH_LENGTHS[month]
year = 1900
first_sundays = 0

while year < 2001:
    # Check if this Sunday is the first of the month.
    if date == 1 and year >= 1901:
        first_sundays += 1
        print date, month, year

    # Move forward to the next sunday.
    date += 7
    if date > month_length:
        date -= month_length
        month += 1

        if (month == 2 and ((year % 4 == 0 and year % 100 != 0) or
                            (year % 400 == 0))):
            month_length = 29
            continue
        elif month > 12:
            month -= 12
            year += 1

        month_length = MONTH_LENGTHS[month]

print first_sundays
