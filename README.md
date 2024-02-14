Sales Data Analysis

Overview:
This project analyzes sales data from a company to derive insights on customer purchases. The data includes information on customers, sales transactions, orders, and items purchased.

Dataset:
The dataset consists of four tables:

customer_table: Contains customer information, including customer ID and age.
sales_table: Contains sales transaction information, including sale ID and customer ID.
order_id_table: Contains order information, including order ID, sales ID, item ID, and quantity.
items_table: Contains item information, including item ID and item name.

Objective:
The goal is to analyze the total quantities of each item bought per customer aged 18-35, excluding items with no purchase (total quantity=0).

Methodology:
SQL Approach:
Created a temporary table (temp_result) to store the result of the analysis.
Used SQL queries to calculate the total quantities of each item bought per customer aged 18-35 and inserted the result into temp_result.
Filtered out items with a total quantity of 0 from temp_result.
Exported the result to a CSV file (output.csv).
Pandas Approach:
Connected to the SQLite database using the sqlite3 library.
Read relevant tables into Pandas DataFrames.
Merged the DataFrames to get the required data.
Filtered the data for customers aged 18-35 and removed rows with Quantity=NULL.
Grouped the data by customer_id and item_id, and calculated the total quantity.
Filtered out items with a total quantity=0.
Wrote the result to a CSV file (output.csv).

test.db is the database 
Sql_Analysis.sql: Contains the SQL queries used for analysis.
Pandas_analysis.py: Contains the Python code using Pandas for analysis.
output.csv: Output file containing the analysis results.

Conclusion
Both approaches provide the same result, showing the total quantities of each item bought per customer aged 18-35. The choice between SQL and Pandas depends on the specific requirements and preferences of the analysis task.

You can modify this README file to include more details or to match the specific structure and content of your project documentation.




