import pandas as pd
from pandasql import sqldf

#import csv as db
# the r is the raw file data flag
data = pd.read_csv(r'data.csv')

#helper function
pysqldf = lambda q: sqldf(q, globals())

#Prints out the database table
df = pd.DataFrame(data)
print(df, end="\n\n")

#SQL query, selcting id and name
query = pysqldf("SELECT product_id, product_name FROM data")
print(query, end="\n\n")

#querying distinct (unique values)
query = pysqldf("SELECT DISTINCT colour FROM data")
print(query, end="\n\n")

#count unique colours
query = pysqldf("SELECT colour, COUNT(colour) FROM data GROUP BY colour")
print(query, end="\n\n")

#display all results if price > 15
query = pysqldf("SELECT product_name, price FROM data WHERE price > 15")
print(query, end="\n\n")

#orders results by a certain column
query = pysqldf("SELECT product_id, product_name, price FROM data ORDER BY product_name ASC")
print(query, end="\n\n")

data = pd.read_csv(r'data.csv')

#inserts record to db
data = data.drop(index = 5)
#data.drop(index = 5, inplace = True)

query = pysqldf("SELECT * FROM data")
print(query, end="\n\n")

#exports dataframe to csv file
data.to_csv('export.csv')