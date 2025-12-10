food_list = []

food = input("Enter the food you like (q to quit): ")

while food != "q":
    food_list.append(food)
    food = input("Enter the food you like (q to quit): ")

print(f"Your favorite foods are: {food_list}")
print("BYE !!!")
