import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 1. Find customers whose 'id' is NOT in the 'customerId' column of orders
    df = customers[~customers['id'].isin(orders['customerId'])]
