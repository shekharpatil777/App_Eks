import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 1. Find customers whose 'id' is NOT in the 'customerId' column of orders
    df = customers[~customers['id'].isin(orders['customerId'])]
    
    # 2. Select only the 'name' column and rename it to 'Customers' as required
    df = df[['name']].rename(columns={'name': 'Customers'})
    
    return df