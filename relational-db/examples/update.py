import pandas as pd
from pandasql import sqldf

stock = pd.read_csv(r"../data/data.csv")
sql = lambda q: sqldf(q, globals())

orderProduct = input()
orderQuantity = int(input())

result = stock["product_name"] == orderProduct
df = stock[result]
quantity = sql("SELECT quantity FROM df").values

if quantity >= orderQuantity:
    # Search for a matching product name and edit the quantity field
    stock.loc[result, "quantity"] -= orderQuantity

    print("order added")
else:
    print("error")
