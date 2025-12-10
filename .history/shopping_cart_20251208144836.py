# Shopping Cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)
        total += price

print("=========Thank you for shopping with us==========")
for food in foods:
    print(f"{food} - ${prices[food]}")

print(f"Total bill is : ${total}")