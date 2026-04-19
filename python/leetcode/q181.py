import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # 1. Perform a left join on the table itself
    # We match the 'managerId' of the employee with the 'id' of the manager
    df = employee.merge(
        employee, 
        left_on='managerId', 
        right_on='id', 
        suffixes=('_emp', '_mgr')
    )
    
    # 2. Filter rows where employee salary > manager salary
    result = df[df['salary_emp'] > df['salary_mgr']]
    
    # 3. Rename and select the 'name' column as per requirements
    return result[['name_emp']].rename(columns={'name_emp': 'Employee'})