import pandas as pd
from pandas import Index


def get_numerical_cols(data: pd.DataFrame) -> Index:
    numerical_cols: Index = data.select_dtypes(exclude='object').columns
    return numerical_cols
