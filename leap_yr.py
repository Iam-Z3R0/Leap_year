# Author: John Asare
# Date: Sat Jul 14 19:40


""" Coding algorithm to check if a year is a leap year. This code is written to best of my ability. I am coded these by
referencing it from a book but, with a strong understanding and reasoning.
check the source: https://www.timeanddate.com/date/leapyear.html
"""


def is_leap(year):

    leap = False

    if 1900 >= year >= 10**5:
        print("The year has to be between 1900 and 100000")

    elif year % 4 == 0 or year % 400 == 0 and year != 0:
        leap = True
    else:
        leap = False
    return leap


year = int(input("Please, enter a year: "))
print(is_leap(year))

