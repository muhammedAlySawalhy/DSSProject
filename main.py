import pandas as pd
import numpy as np

np.random.seed(42)

# Sample data components
num_rows = 1500
dates = pd.date_range(start='2023-01-01', periods=365).to_list()
product_categories = ['Clothing', 'Electronics', 'Home & Kitchen', 'Books', 'Toys', 'Beauty']
regions = ['US', 'AF', 'Asia', 'Europe', 'Middle East']
payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash on Delivery']

# Generate data
df = pd.DataFrame()
for i in range(1, num_rows+1):
    order_id = i
    order_date = np.random.choice(dates)
    customer_id = np.random.randint(1, num_rows+1)
    product_category = np.random.choice(product_categories)
    region = np.random.choice(regions)
    quantity = np.random.randint(1, 5)
    unit_price = np.round(np.random.uniform(10.0, 500.0), 2)
    discount = np.round(np.random.uniform(0.0, 0.3), 2)
    payment_method = np.random.choice(payment_methods)
    returned = np.random.choice([0, 1], p=[0.9, 0.1])
    total_price = np.round((quantity * unit_price) * (1 - discount), 2)

    # Append data to the DataFrame
    df = pd.concat([df, pd.DataFrame({
        'OrderID': [order_id],
        'OrderDate': [order_date],
        'CustomerID': [customer_id],
        'Discount': [discount],
        'ProductCategory': [product_category],
        'Region': [region],
        'Quantity': [quantity],
        'UnitPrice': [unit_price],
        'PaymentMethod': [payment_method],
        'Returned': [returned],
        'TotalPrice': [total_price]
    })])


    df['TotalPrice'] = (df['Quantity'] * df['UnitPrice']) * (1 - df['Discount'])

# View the first few rows
print(df.head())

# Convert OrderDate to YYYY-MM-DD format for display
df['OrderDate'] = df['OrderDate'].dt.strftime('%Y-%m-%d')

# Save as 3 formats
df.to_csv('orders.csv', index=False)
df.to_excel('orders.xlsx', index=False)
df.to_csv('orders_flat.txt', sep='|', index=False)