import pandas as pd
import numpy as np

np.random.seed(0)
costumer_numbers=100
product_numbers = 50
sales_numbers=200
customers= pd.DataFrame({
    'Customer ID': range(1, costumer_numbers + 1),
    'Customer Name': np.random.choice(['John', 'Sarah', 'Bob', 'Emily', 'Michael', 'David', 'Sophia', 'Olivia', 'William', 'James'], size=costumer_numbers),
    'Purchase Amount': np.random.uniform(10, 1000, size=costumer_numbers),
    'Purchase Date': pd.date_range(start='2022-01-01', periods=costumer_numbers, freq='D'),
    'Purchase Frequency': np.random.choice(['Weekly', 'Monthly', 'Quarterly', 'Annually'], size=costumer_numbers),
    'Purchase Category': np.random.choice(['Electronics', 'Clothing', 'Books'],costumer_numbers)

})
products = pd.DataFrame({
    'Product ID': range(1, product_numbers + 1),
    'Product Name': np.random.choice(['Laptop', 'Phone', 'TV', 'Book', 'Shirt', 'Shoes'], product_numbers),
    'Price': np.round(np.random.uniform(20, 5000, product_numbers), 2),  
    'Category': np.random.choice(['Electronics', 'Clothing', 'Books'], product_numbers)
})
sales = pd.DataFrame({
    'Sales ID': range(1, sales_numbers + 1),
    'Customer ID': np.random.choice(customers['Customer ID'], sales_numbers),
    'Product ID': np.random.choice(products['Product ID'], sales_numbers),
    'Sales Date': pd.to_datetime(np.random.choice(pd.date_range('2023-01-01', '2023-12-31'), sales_numbers)),
    'Sales Number': np.random.randint(1, 5, sales_numbers),  
})


sales = sales.merge(products[['Product ID', 'Price']], on='Product ID')
sales['Total Cost'] = sales['Sales Number'] * sales['Price']

print("\nSales Table")
print(sales.head())
print("\nProducts table")
print(products.head())
print("\nCustomer Table")
print(customers.head())