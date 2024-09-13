# Exclusive Or
# The or operator returns a truthy value if either or
# both of its operands are truthy, a falsy value if
# both operands are falsy. The and operator returns a
# truthy value if both of its operands are truthy,
# and a falsy value if either operand is falsy. This
# works great until you need only one of two
# conditions to be truthy, the so-called exclusive
# or, also known as xor (pronounced "ECKS-or").

# In this exercise, you will write an xor function
# that takes two arguments, and returns True if
# exactly one of its arguments is truthy, False
# otherwise.


# def xor(obj1, obj2):
#     if (obj1 and not obj2) or (obj2 and not obj1):
#         return True

#     return False


# def xor(value1, value2):
#     if (value1 and not value2) or (value2 and not value1):
#         return True

#     return False


# def xor(value1, value2):
#     return bool((value1 and not value2) or (value2 and not value1))


# def xor(arg1, arg2):
#     return bool(arg1) != bool(arg2)


def xor(arg1, arg2):
    return bool(arg1 ^ arg2)


# Examples
print(xor(5, 0))
print(xor(False, True))
print(xor(1, 1))
print(xor(True, True))
