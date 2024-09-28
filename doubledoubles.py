# Double Doubles
# A double number is an even-length number whose left-side
# digits are exactly the same as its right-side digits.
# For example, 44, 3333, 103103, and 7676 are all double numbers,
# whereas 444, 334433, and 107 are not.

# Write a function that returns the number provided as an
# argument multiplied by two, unless the argument is a double
# number. If the argument is a double number, return the double
# number as-is.


# My initial approach
def twice(num: int) -> int:
    num_string = str(num)
    len_num_string = len(num_string)
    
    if ((len(num_string) % 2 == 0) and
        (num_string[0:(((len_num_string) // 2))] ==
         num_string[((len_num_string // 2)):])):
        return num
    else:
        return num * 2

# Solution from LS separating logic and process into 2 functions:
# def is_double_number(number):
#     string_number = str(number)
#     center = len(string_number) // 2
#     left_number = string_number[:center]
#     right_number = string_number[center:]

#     return left_number == right_number

# def twice(number):
#     if is_double_number(number):
#         return number
#     else:
#         return number * 2


# Examples
print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
