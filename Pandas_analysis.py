import sqlite3
import pandas as pd
import os

# Connect to SQLite database
test.db = os.getenv('test.db')
conn = sqlite3.connect('test.db')

# Read relevant tables into DataFrames
sales_df = pd.read_sql_query('SELECT * FROM sales_table', conn)
customer_df = pd.read_sql_query('SELECT * FROM customer_table', conn)
order_df = pd.read_sql_query('SELECT * FROM order_id_table', conn)
items_df = pd.read_sql_query('SELECT * FROM items_table', conn)

# Merge tables to get the required data
merged_df = pd.merge(sales_df, customer_df, on='customer_id')
merged_df = pd.merge(merged_df, order_df, left_on='sale_id', right_on='sales_id')
merged_df = pd.merge(merged_df, items_df, on='item_id')

# Filter data for customers aged 18-35 and remove rows with Quantity=NULL
filtered_df = merged_df[(merged_df['age'] >= 18) & (merged_df['age'] <= 35) & (merged_df['Quantity'].notnull())]

# Group by customer, item, and calculate total quantity
grouped_df = filtered_df.groupby(['customer_id', 'age', 'item_name']).agg({'Quantity': 'sum'}).reset_index()

# Rename columns for consistency
grouped_df.rename(columns={'customer_id': 'Customer', 'age': 'Age', 'item_name': 'Item', 'Quantity': 'Quantity'}, inplace=True)

# Write DataFrame to CSV
grouped_df.to_csv('output.csv', sep=';', index=False)
output_df = pd.read_csv('output.csv', sep=';')
print(output_df)
# Close SQLite3 connection
conn.close()
