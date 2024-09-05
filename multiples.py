# Write a function that computes the sum of all
# numbers between 1 and some other number, inclusive,
# that are multiples of 3 or 5. For instance, if the
# supplied number is 20, the result should be 98 (3 +
# 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an
# integer greater than 1.


def multisum(number):
    sum = 0
    for num in range(1, number + 1):
        if (num % 3 == 0) or (num % 5 == 0):
            sum += num
        else:
            continue
    return sum


# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
