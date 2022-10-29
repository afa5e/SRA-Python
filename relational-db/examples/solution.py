import pandas as pd
from pandasql import sqldf

stock = pd.read_csv(r"../data/data.csv")
cart = pd.read_csv(r"../data/cart.csv")

sql = lambda q: sqldf(q, globals())

print('''Welcome to the Python Store.

To search for an item, use the command "s" followed by the name of the item.
To add an item to your cart, use the "a" command followed by the name and the quantity.
To remove an item, use "r" followed by the name and quantity.
To view you cart, use "v"
To calculate the total price, use "c"
To exit, use CTRL+D''')

print("Command: ", end = "")
try:
    command = input()
    print("")
except:
    quit()

while input != "":
    if command[0] == "s":
        result = stock[(stock['product_name'] == command [2:])]
        result = sql("SELECT product_name, quantity FROM result")

        for item in result.values.tolist():
            print(item[0] + ":", item[1], "in stock\n")
    elif command[0] == "v":
        result = sql("SELECT * FROM cart")
        if len(result) == 0:
            print("Your cart is empty\n")
        else:
            print(cart, "\n")
    elif command[0] == "a":
        command = command.split()
        product_name = command[1]
        order_quantity = int(command[2])

        result = stock["product_name"] == product_name
        df = stock[result]
        quantity = sql("SELECT quantity FROM df").values

        if order_quantity > 0:
            if quantity >= order_quantity:
                result = cart[(cart['product_name'] == product_name)]
                result = sql("SELECT product_name, quantity, price FROM result")
                stock_result = sql("SELECT price FROM stock")

                stock.loc[result, "quantity"] -= order_quantity

                if (len(result) == 0):
                    item = pd.DataFrame({
                        "product_name": [str(product_name)],
                        "price": [float(stock_result.values.tolist()[0][0])],
                        "quantity": [int(order_quantity)]
                    })

                    cart = pd.concat([cart, item])
                else:
                    result = cart["product_name"] == product_name
                    cart.loc[result, "quantity"] += order_quantity

                print("Added to cart.\n")
            else:
                print("You cannot order", order_quantity, "of", product_name, "as there are only", int(quantity), "in stock.\n")
        else:
            print("Invalid quantity\n")
    else:
        print("Invalid command.\n")

    print("Command: ", end = "")
    try:
        command = input()
        print()
    except:
        break
