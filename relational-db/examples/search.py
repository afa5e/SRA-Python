import pandas as pd
from pandasql import sqldf

stock = pd.read_csv(r"../data/data.csv")
sql = lambda q: sqldf(q, globals())

# Find all records that match the condition and place them into the results DF
result = stock[(stock['price'] == 5.99)]


# SQL select name and price from the search results
result = sql("SELECT product_name, price FROM result").values.tolist()

# Iterate through the list of results and print out each one
for item in result:
    print(item[0], "price:", item[1])