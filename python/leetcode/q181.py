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
