# Sum or Product of Consecutive Integers
# Write a program that asks the user to enter an integer
# greater than 0, then asks whether the user wants to
# determine the sum or the product of all numbers
# between 1 and the entered integer, inclusive.

# Examples:
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s
# The sum of the integers between 1 and 5 is 15.

# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p
# The product of the integers between 1 and 6 is 720.

integer = abs(int(input("Please enter an integer that is greater than zero: ")))
algo_choice = input(
    'Enter "s" to compute the sum, or "p" to compute the product of all numbers between 1 and your entered integer: '
)

summed = 0
for num in range(1, (integer + 1)):
    summed += num

product = 1
for num in range(1, (integer + 1)):
    product *= num

if algo_choice == "s":
    print(f"The sum of the integers between 1 and {integer} is {summed}.")
elif algo_choice == "p":
    print(f"The product of the integers between 1 and {integer} is {product}.")
else:
    print("Unknown operation.")

# Further Exploration
# Suppose the input was a list of space separated integers instead
# of just a single integer? How would your compute_sum and
# compute_product functions change?
