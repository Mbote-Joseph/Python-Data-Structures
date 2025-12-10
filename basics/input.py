# Input - It is a function that allows the user to input data.  It returns the entered data as a string.

# Area of a Trapezium
long_base = float(input("Enter the length of the long length: "))
short_base = float(input("Enter the length of the short length: "))
trapezium_height = float(input("Enter the height of the trapezium: "))

# Area of a Trapezium
area = 1/2 * (long_base + short_base) * trapezium_height
print(f"The area of the trapezium is {area} units squared")
