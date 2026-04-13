import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # 1. Get unique salaries and sort them descending
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # 2. Check if there are at least two unique salaries
    if len(unique_salaries) < 2:
        res = None
    else:
        # 3. Take the second highest (index 1)
        res = unique_salaries.iloc[1]
    
    # Return as a DataFrame with the specific column name required
    return pd.DataFrame({'SecondHighestSalary': [res]})