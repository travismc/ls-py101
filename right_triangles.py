# Right Triangles
# Write a function that takes a positive integer, n, 
# as an argument and prints a right triangle whose 
# sides each have n stars. The hypotenuse of the 
# triangle (the diagonal side in the images below) 
# should have one end at the lower-left of the 
# triangle, and the other end at the upper-right.

def triangle(height: int) -> None:
	for num in range(1, height + 1):
		spaces = height - num
		stars = num
		print(f'{" " * spaces}{"*" * stars}')

# Example
triangle(5)
triangle(9)
