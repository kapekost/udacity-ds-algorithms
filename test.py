def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    if (year1, month1, day1) == (year2, month2, day2):
        return 0
    assert(dayIsBefore(year1, month1, day1, year2, month2, day2) == True)
    nyear, nmonth, nday = year1, month1, day1
    days = 0
    while (dayIsBefore(nyear, nmonth, nday, year2, month2, day2)):
        days += 1
        nyear, nmonth, nday = nextDay(nyear, nmonth, nday)
    return days


def nextDay(year, month, day):
    if (day < daysInMonth(year, month)):
        return year, month, day + 1
    else:
        if (month < 12):
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


def dayIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysInMonth(year, month):
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28

    if(month < 8):
        if(month % 2 == 0):
            return 30
        else:
            return 31
    else:
        if(month % 2 == 0):
            return 31
        else:
            return 30


def isLeapYear(year):
    """
    1 If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
    2 If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
    3 If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
    4 The year is a leap year (it has 366 days).
    5 The year is not a leap year (it has 365 days)."""
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


def testNextDay():
    assert(nextDay(1999, 11, 2) == (1999, 11, 3))
    assert(nextDay(1999, 11, 29) == (1999, 11, 30))
    assert(nextDay(1999, 11, 30) == (1999, 12, 1))
    assert(nextDay(1999, 12, 30) == (1999, 12, 31))
    assert(nextDay(2020, 7, 31) == (2020, 8, 1))
    assert(nextDay(2020, 7, 30) == (2020, 7, 31))
    assert(nextDay(2020, 6, 30) == (2020, 7, 1))

    print("function testNextDay is working correctly!")


def testDayIsBefore():
    assert(dayIsBefore(1999, 11, 2, 1999, 11, 3) == True)
    assert(dayIsBefore(1999, 11, 2, 1999, 11, 2) == False)
    assert(dayIsBefore(1999, 10, 2, 1999, 11, 3) == True)
    assert(dayIsBefore(1998, 11, 3, 1999, 11, 3) == True)
    assert(dayIsBefore(2000, 11, 3, 1998, 11, 3) == False)
    assert(dayIsBefore(1999, 10, 3, 1999, 11, 3) == True)
    print("function testDayIsBefore is working correctly!")


def testIsLeapYear():
    """1992	Leap Year
    2000	Leap Year
    1900	NOT a Leap Year"""
    assert(isLeapYear(1992) == True)
    assert(isLeapYear(2000) == True)
    assert(isLeapYear(1900) == False)


def testDaysBetweenDates():
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                            2017, 12, 30) == 0)
#     test adjacent days
    assert(daysBetweenDates(2017, 12, 30,
                            2017, 12, 31) == 1)
#     test new year
    assert(daysBetweenDates(2017, 12, 30,
                            2018, 1,  1) == 2)
# #     test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                            2013, 6, 29) == 365)
    # test leap Year
    assert(daysBetweenDates(2000, 1, 1,
                            2001, 1, 1) == 366)
    print("function testDaysBetweenDates is working correctly!")
    print("Congratulations! Your daysBetweenDates")


testDayIsBefore()
testDaysBetweenDates()
testNextDay()
testIsLeapYear()


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()
