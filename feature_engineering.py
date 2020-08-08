from dataclasses import dataclass

import pandas as pd
from pandas import Index


@dataclass
class FeatureEngineeringResult:
    X: pd.DataFrame
    Y: pd.DataFrame


def get_numerical_cols(data: pd.DataFrame) -> Index:
    numerical_cols: Index = data.select_dtypes(exclude='object').columns

    return numerical_cols


def main(data: pd.DataFrame, label_col: str) -> FeatureEngineeringResult:
    feature_cols = [col for col in get_numerical_cols(data) if col != label_col]
    print(feature_cols)

    X = data[feature_cols]
    X = X.fillna(-1)

    Y = data[label_col]

    return FeatureEngineeringResult(X, Y)
