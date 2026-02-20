# pizza order system
# Make a list called pizza_orders with ordered pizzas.
pizza_orders = ["pepperoni", "cheese", "veggie"]
# Make an empty list called finished_pizzas.
finished_pizzas = []
# Loop through the list of pizza orders and print a message for each order.
while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print("Your pizza pie is finished!")
# Move the finished pizza to the list finished_pizzas.
    finished_pizzas.append(current_pizza)
# After all of the pizza have been made, print a message for each finished pizza.
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")

