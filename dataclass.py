from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Callable, Any

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


class ModelType(Enum):
    XGBRegressor = auto()
    LGBMRegressor = auto()


@dataclass(frozen=True)
class BuildModelResult:
    model: Any
    MAE: Any
    val: pd.DataFrame


@dataclass(frozen=True)
class FusionResult:
    predict_func: Callable[[pd.DataFrame], pd.DataFrame]

    def predict(self, x: pd.DataFrame) -> pd.DataFrame:
        return self.predict_func(x)
