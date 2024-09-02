# How big is the room?
# Build a program that asks the user to enter
# the length and width of a room, in meters,
# then prints the room's area in both square
# meters and square feet.

# Note: 1 square meter == 10.7639 square feet

length_meters = float(input("Enter length of room in meters: "))
width_meters = float(input("Enter width of room in meters: "))

print(
    f"The room's area in square meters is {length_meters * width_meters:.2f}, which is equal to {(length_meters * width_meters) * 10.7639:.2f} square feet."
)
