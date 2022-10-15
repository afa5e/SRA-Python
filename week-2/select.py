import pandas as pd
from pandasql import sqldf

# Importing a CSV file that is in the same folder as your py file
# We are going to store the raw data in a DataFrame called data
data = pd.read_csv('data.csv')

# Helper function to process queries
sql = lambda q: sqldf(q, globals())

# Select everything from the DF, this should output the same as print(data)
query = sql("SELECT * FROM data")
print(query)