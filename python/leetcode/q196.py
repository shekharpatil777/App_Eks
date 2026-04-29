import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # 1. Sort by id in ascending order
    person.sort_values(by='id', ascending=True, inplace=True)
    
    # 2. Drop rows with duplicate emails, keeping the first occurrence (smallest id)
    person.drop_duplicates(subset='email', keep='first', inplace=True)