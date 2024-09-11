# Squaring an Argument
# Using the multiply function from the "Multiplying
# Two Numbers" exercise, write a function that
# computes the square of its argument (the square is
# the result of multiplying a number by itself).


def square(num):
    return num**2


# Examples
# print(square(5) == 25)  # True
# print(square(-8) == 64)  # True


# Further Exploration
# Suppose we want to generalize this function to a
# "power to the n" type function: cubed, to the 4th
# power, to the 5th, etc. How would we go about doing
# so while still using the multiply function?


def exponent(num, exp):
    # num = int(input("What is the number?: "))
    # exp = int(input("What is the exponent?: "))
    return f"The answer is {num**exp}"


# Example test
print(exponent(4, 3))
