import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # Create shifted columns to look at the next and the one after next
    logs['prev'] = logs['Num'].shift(1)
    logs['next'] = logs['Num'].shift(-1)
    
    # Filter rows where current Num matches both the previous and the next
    # This identifies a sequence of at least 3
    is_consecutive = (logs['Num'] == logs['prev']) & (logs['Num'] == logs['next'])
    
    # Extract unique values and rename column to match requirement
    result = logs.loc[is_consecutive, ['Num']].drop_duplicates()
    return result.rename(columns={'Num': 'ConsecutiveNums'})