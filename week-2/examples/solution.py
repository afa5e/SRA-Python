import pandas as pd
from pandasql import sqldf

stock = pd.read_csv(r"../data/data.csv")

sql = lambda q: sqldf(q, globals())

result = stock[(stock['price'] == 5.99)]
result = sql("SELECT product_name, price FROM result").values.tolist()

for item in result:
    print(item[0], "price:", item[1])

result = stock["product_name"] == "apple"
stock.loc[result, "quantity"] -= 1

print(stock)