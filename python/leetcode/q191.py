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
