from dataclasses import dataclass
from typing import List, Dict

import pandas as pd

from feature_engineering import get_numerical_cols


@dataclass(frozen=True)
class ColumnInfo:
    dtype: str


@dataclass(frozen=True)
class DataInfo:
    columns: Dict[str, ColumnInfo]
    size: int


def load(path: str, sep: str) -> pd.DataFrame:
    return pd.read_csv(path, sep)


def verify(data: pd.DataFrame, expected_info: DataInfo):
    assert data.columns.size == len(expected_info.columns)
    assert len(data) == expected_info.size
    pass


def EDA(data: pd.DataFrame):
    pass


if __name__ == '__main__':
    train_data = pd.read_csv(r"C:\Users\htsai\Downloads\used_car_train_20200313\used_car_train_20200313.csv", sep=' ')
    print(len(train_data))
    # get_numerical_cols(data)
