from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Callable, Any, Protocol, List

import pandas as pd


@dataclass(frozen=True)
class ColumnInfo:
    name: str
    dtype: str
    exclude: bool = False


class DataInfo:
    def __init__(self,
                 feature_columns: List[ColumnInfo],
                 size: int):
        self.feature_columns = feature_columns
        self.size = size
        self.column_dict: Dict[str, ColumnInfo] = {x.name: x for x in self.feature_columns}


class TrainDataInfo(DataInfo):
    def __init__(self, feature_columns: List[ColumnInfo], size: int, label_column: ColumnInfo):
        super().__init__([*feature_columns, label_column], size)
        self.label_column = label_column


class PredictDataInfo(DataInfo):
    pass


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


class ModelProto(Protocol):
    def predict(self, x: pd.DataFrame) -> pd.DataFrame:
        pass


@dataclass(frozen=True)
class BuildModelResult:
    model: ModelProto
    MAE: Any
    val: pd.DataFrame


@dataclass(frozen=True)
class FusionResult:
    predict_func: Callable[[pd.DataFrame], pd.DataFrame]

    def predict(self, x: pd.DataFrame) -> pd.DataFrame:
        return self.predict_func(x)
