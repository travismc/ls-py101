# Bannerizer
# Write a function that takes a short line of text and prints it within a box.

# def print_in_box(string: str) -> str:
# 	print(f"+{("-" * len(string)) + 2}+")
# 	print(f"|{(" " * len(string)) + 2}|")
# 	print(f"| {string} |")
# 	print(f"|{(" " * len(string)) + 2}|")
# 	print(f"+{("-" * len(string)) + 2}+")

# Better optimized approach
def print_in_box(message):
    horizontal_rule = f'+-{"-" * len(message)}-+'
    empty_line = f'| {" " * len(message)} |'

    print(horizontal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_rule)

# Examples
print_in_box('To boldly go where no one has gone before.')
print_in_box('')
