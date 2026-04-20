import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # 1. Group by email
    # 2. Filter groups where the size is greater than 1
    # 3. Select only the 'email' column
    
    # Method A: Using duplicated() - Very efficient
    duplicates = person[person.duplicated(['email'])]
    
    # Return unique values from the duplicates found to avoid triples/quadruples
    return duplicates[['email']].drop_duplicates()

    # Method B: Using groupby and filter (Closer to SQL logic)
    # df = person.groupby('email').filter(lambda x: len(x) > 1)
    # return df[['email']].drop_duplicates()