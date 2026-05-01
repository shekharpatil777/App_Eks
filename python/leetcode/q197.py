import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # 1. Sort by id in ascending order to keep the smallest id
    person.sort_values(by='id', ascending=True, inplace=True)
    
    # 2. Drop duplicates based on email, keeping the first occurrence
    # 'inplace=True' modifies the original dataframe as required by the problem
    person.drop_duplicates(subset='email', keep='first', inplace=True)