# Greeting a user
# Write a program that asks for user's name, then
# greets the user. If the user appends a ! to their
# name, the computer will yell the greeting (print it
# using all uppercase).


def greeting(name):
    if name[-1] == "!":  # could also use name.endswith('!'):
        return f"HELLO {name.upper()}! WHY ARE WE YELLING?"
    else:
        return f"Hello {name}."


name = input("What is your name? ")

print(greeting(name))
