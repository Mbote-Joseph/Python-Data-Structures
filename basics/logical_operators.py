#  Logical Operators - Evaluate multiple conditions (or, and, not)
#  or - At least one condition must be True
#  and - Both conditions must be True
#  not - Inverts the condition (not False, not True)

temp = 25
is_sunny = False

if temp >= 28 and is_sunny:
    print(f"It is Hot outside")
    print(f"It is Sunny")
elif temp < 28 and is_sunny:
    print(f"It is cold outside")
    print("It is sunny")
elif temp < 28 and not is_sunny:
    print(f"It is cold outside")
    print("It is NOT sunny")