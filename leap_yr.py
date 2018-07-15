# Author: John Asare
# Date: Sat Jul 14 19:40


""" Coding algorithm to check if a year is a leap year. This code is written to best of my ability. I am coded these by
referencing it from a book but, with a strong understanding and reasoning.
check the source: https://www.timeanddate.com/date/leapyear.html
"""


def is_leap(year):
    leap = False

    # Check if the year enter is between 1900 and 100000. if not then print a message
    if 1900 >= year >= 10**5:
        print("Please, type a proper year. Constraints: 1900 <= year <= 10^5")

    # check if the year is divisible by 4 or 100 or 400
    elif year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
        leap = True
    elif year % 4 != 0 or year % 100 != 0 or year % 400 != 0:
        leap = False

    return leap


year = int(input("Please enter a year: "))
print(is_leap(year))
