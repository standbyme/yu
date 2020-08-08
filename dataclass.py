from dataclasses import dataclass
from typing import Dict

import pandas as pd


@dataclass(frozen=True)
class ColumnInfo:
    dtype: str


@dataclass(frozen=True)
class DataInfo:
    columns: Dict[str, ColumnInfo]
    size: int
    label_col: str

    def __post_init__(self):
        assert self.label_col in self.columns


@dataclass(frozen=True)
class DataPair:
    x: pd.DataFrame
    y: pd.DataFrame


class TrainDataPair(DataPair):
    pass


class ValDataPair(DataPair):
    pass


@dataclass(frozen=True)
class SplitResult:
    train: TrainDataPair
    val: ValDataPair
