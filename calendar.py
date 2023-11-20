from datetime import datetime

days_in = {
    1: 31, 2: 28, # 29 in leap years
    3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
    8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Every year that is exactly divisible by four is a leap year,
# except for years that are exactly divisible by 100
def is_leap(year: int) -> bool:
    if year%100==0: return False
    elif year%4==0: return True
    else: return False

def days_till(month: int, day: int) -> int:
    """
    Arguments:

    month - integer from 1 to 12 (january to december)

    day - integer from 1 to 31 (day of the month)

    Returns number of days till the next DAY of the MONTH,
    for example, 7 th of july.
    """
    c_day = datetime.now().day
    c_month = datetime.now().month
    c_year = datetime.now().year
    result = 0
    while c_month!=month or c_day!=day:
        c_day += 1
        result += 1
        c_month_days = days_in[c_month]
        if c_month==2 and is_leap(c_year):
            c_month_days = 29
        if c_day > c_month_days:
            c_day = 1
            c_month += 1
            if c_month > 12:
                c_month = 1
                c_year += 1
    return result
