food_list = []

food = input("Enter the food you like (q to quit): ")

while food.lower() != "q":
    food_list.append(food)

    option = input("Do you like any other food? (y - yes, n - no): ")

    if option.lower() == "y":
        food = input("Enter the other food you like (q to quit): ")
    else:
        break

print(f"Your favorite foods are: {food_list}")
print("BYE !!!")
