import math

print("SOH CAH TOA")
# I need to enter 2 sides of the triangle
side1, side2 = input("Enter the sides of the triangle that are missing (opposite(o), adjacent(a), hypotenuse(h)) :").split()

if side1 == "o" and side2 == "h" or side1 == "h" and side2 == "o":
    opposite = float(input("Enter the length of the opposite side: "))
    hypotenuse = float(input("Enter the length of the hypotenuse: "))
    angle = math.asin(opposite / hypotenuse)
    print(f"The angle is {math.degrees(angle)}")

elif side1 == "a" and side2 == "h" or side1 == "h" and side2 == "a":
    adjacent = float(input("Enter the length of the adjacent side: "))
    hypotenuse = float(input("Enter the length of the hypotenuse: "))
    angle = math.acos(adjacent / hypotenuse)
    print(f"The angle is {math.degrees(angle)}")

elif side1 == "o" and side2 == "a" or side1 == "a" and side2 == "o":
    opposite = float(input("Enter the length of the opposite side: "))
    adjacent = float(input("Enter the length of the adjacent side: "))
    angle = math.atan(opposite / adjacent)
    print(f"The angle is {math.degrees(angle)}")

else:
    print("Invalid input")

