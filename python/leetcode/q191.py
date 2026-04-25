import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # 1. Perform an inner join of the table with itself
    # We join the 'managerId' of the employee with the 'id' of the manager
    df = employee.merge(
        employee, 
        how='inner', 
        left_on='managerId', 
        right_on='id', 
        suffixes=('_emp', '_mgr')
    )
    
    # 2. Filter rows where employee salary > manager salary
    result_df = df[df['salary_emp'] > df['salary_mgr']]
    
    # 3. Rename the column to match the required output format
    return result_df[['name_emp']].rename(columns={'name_emp': 'Employee'})