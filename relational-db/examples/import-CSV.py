import pandas as pd
from pandasql import sqldf

# Importing a CSV file that is in the same folder as your py file
# We are going to store the raw data in a DataFrame called data
data = pd.read_csv('data.csv')

# We can now print out the data stored in the DataFrame
print(data)