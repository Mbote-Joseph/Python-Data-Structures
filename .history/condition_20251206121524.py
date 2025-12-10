# If does an operation if a specific given condition is True

name = input("Enter your name: ")

if name == "":
    print("The name should not be blank")
elif name != "":
    print(f"Hello {name}")
    