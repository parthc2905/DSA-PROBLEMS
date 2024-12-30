import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # return employees.iloc[:3]
    # return employees[:3]
    return employees.head(3)
