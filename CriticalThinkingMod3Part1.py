print("\n\nMeal Calculator\n")

print("How much was the meal?", end=" ")

meal_cost = int(input())

tip = round(meal_cost * 0.18, 2)

sales_tax = round(meal_cost * 0.07, 2)

total_cost = meal_cost + tip + sales_tax

print("\nItemized Receipt\n")

print("Price of Meal: ", meal_cost)

print("Suggest Tip: ", tip)

print("Sales Tax: ", sales_tax)

print("Total: ", total_cost)
