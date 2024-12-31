import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # return students.dropna(subset=['name'], axis=0, how='any')
    return students[students['name'].notna()]
