# List of pizza orders
pizza_orders = ["pepperoni", "cheese", "bbq chicken", "veggie"]

# Empty list for finished pizzas
finished_pizzas = []

# Make pizzas using a while loop
while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print("Your pizza pie is finished!")
    finished_pizzas.append(current_pizza)

# Print finished pizzas
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")