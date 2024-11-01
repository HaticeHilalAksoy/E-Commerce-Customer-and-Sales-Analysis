import pandas as pd
import numpy as np

np.random.seed(0)
costumer_numbers=100

customers= pd.DataFrame({
    'Customer ID': range(1, costumer_numbers + 1),
    'Customer Name': np.random.choice(['John', 'Sarah', 'Bob', 'Emily', 'Michael', 'David', 'Sophia', 'Olivia', 'William', 'James'], size=costumer_numbers),
    'Purchase Amount': np.random.uniform(10, 1000, size=costumer_numbers),
    'Purchase Date': pd.date_range(start='2022-01-01', periods=costumer_numbers, freq='D'),
    'Purchase Frequency': np.random.choice(['Weekly', 'Monthly', 'Quarterly', 'Annually'], size=costumer_numbers),
    'Purchase Category': np.random.choice(['Electronics', 'Clothing', 'Books'],costumer_numbers)

})
print("Customer Table")
print(customers.head())