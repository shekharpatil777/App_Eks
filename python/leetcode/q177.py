import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # 1. Drop duplicate salaries to find unique values
    unique_salaries = employee['salary'].drop_duplicates()
    
    # 2. Sort salaries in descending order
    # (ascending=False puts the highest at the top)
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    
    # 3. Check if there are at least 2 unique salaries
    if len(sorted_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    # 4. Select the second highest (iloc[1])
    # We wrap it in a DataFrame to match LeetCode's expected output format
    res = sorted_salaries.iloc[1]
    
    return pd.DataFrame({'SecondHighestSalary': [res]})