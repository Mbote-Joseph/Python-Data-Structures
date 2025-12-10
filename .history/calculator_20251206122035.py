value1 = float(input("Enter the first Value:"))
operator = float(input("Enter the Operation (+ -> Addition, - -> subtraction, * -> multiplication, / -> division):"))
value2 = float(input("Enter the Second Value:"))

if operator == "+":
    result = value1 + value2
    print(f"The result of addition of the 2 values is {result}")
elif operator == "-":
    result = value1 - value2
    print(f"The result of subtraction of the 2 values is {result}")
elif operator == "*":
    result = value1 * value2
    print(f"The result of multiplication of the 2 values is {result}")
elif operator == "/":
    result = value1 / value2
    print(f"The result of division of the 2 values is {result}")
else:
    print(f"The operator you used is undefined")