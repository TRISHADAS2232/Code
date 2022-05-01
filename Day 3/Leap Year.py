def is_leap(year):
    # Write your logic here
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 != 0:
            leap = True
    else:
        leap = False
        if year % 400 == 0:
            leap = True

    return leap



year = 2100
print(is_leap(year))