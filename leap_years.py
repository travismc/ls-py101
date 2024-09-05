# Write a function that takes any year greater than 0
# as input and returns True if the year is a leap
# year, or False if it is not.


def is_leap_year(year):
    if year <= 0:
        return "Year must be greater than zero."
    if year < 1752 and year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0


# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)


# Further Exploration
# Different regions adopted the Gregorian calendar at
# different times. Investigate when it was adopted in
# various countries and how that transition was
# managed. Consider how this would impact the leap
# year calculation and potentially adjust the solution
# based on the country of reference.
