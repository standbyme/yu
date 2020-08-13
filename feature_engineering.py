from dataclasses import dataclass
from typing import List

import pandas as pd

from dataclass import DataInfo, TrainDataInfo


@dataclass
class TrainFeatureEngineeringResult:
    X: pd.DataFrame
    Y: pd.DataFrame
    feature_columns: List[str]


def get_numerical_cols(data: pd.DataFrame) -> pd.Index:
    numerical_columns: pd.Index = data.select_dtypes(exclude='object').columns

    return numerical_columns


def verify(data: pd.DataFrame, expected_info: DataInfo):
    assert data.columns.size == len(expected_info.column_dict)
    assert len(data) == expected_info.size


def train_feature_engineering(data: pd.DataFrame, expected_info: TrainDataInfo) -> TrainFeatureEngineeringResult:
    feature_cols = [col for col in get_numerical_cols(data) if
                    col != expected_info.label_column.name and not expected_info.column_dict[col].exclude]
    print(feature_cols)

    X = data[feature_cols]
    X = X.fillna(-1)

    Y = data[expected_info.label_column.name]

    return TrainFeatureEngineeringResult(X, Y, feature_cols)


def predict_feature_engineering(data: pd.DataFrame,
                                train_feature_engineering_result: TrainFeatureEngineeringResult) -> pd.DataFrame:
    X = data[train_feature_engineering_result.feature_columns]
    X = X.fillna(-1)
    # todo: sync with train feature engineering
    return X
