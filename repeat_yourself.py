# Repeat Yourself
# Write a function that takes two arguments, a
# string and a positive integer, then prints
# the string as many times as the integer
# indicates.

def repeat(word: str, number: int) -> str:
    number = abs(int(number))
    for _ in range(number):
        print(word)

repeat('Hello', 3)
repeat('Bird is the Word', 10)
repeat('Trixie', -3)
repeat('Last test', -2.7)
