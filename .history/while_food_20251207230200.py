food_list = []
food = input("Enter the food you like (q to quit):")

food_list.append(food)

while not food == "q":
    option = input(f"Do you like any food (y- yes, n - no):")
    while option.lower() == "y":
        food = input("Enter the other food you like (q to quit):")
        food_list.append(food)
        while food == "q":
            break
        
print(f"Your favorite foods are: {food_list}")
print(f"BYE !!!")