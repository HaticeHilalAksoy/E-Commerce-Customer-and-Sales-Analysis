import pandas as pd
import numpy as np

np.random.seed(0)
costumer_numbers=100
product_numbers = 50
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
    'Product Adı': np.random.choice(['Laptop', 'Phone', 'TV', 'Book', 'Shirt', 'Shoes'], product_numbers),
    'Price': np.round(np.random.uniform(20, 5000, product_numbers), 2),  
    'Category': np.random.choice(['Electronics', 'Clothing', 'Books'], product_numbers)
})

print("\nProducts table")
print(products.head())
print("Customer Table")
print(customers.head())