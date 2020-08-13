import pandas as pd
from sklearn.model_selection import train_test_split

from feature_engineering import TrainFeatureEngineeringResult
from dataclass import DataInfo, SplitResult, TrainDataPair, ValDataPair


def load(path: str, sep: str) -> pd.DataFrame:
    return pd.read_csv(path, sep)


def EDA(data: pd.DataFrame):
    pass


def split(feature_engineering_result: TrainFeatureEngineeringResult, test_size: float):
    x_train, x_val, y_train, y_val = train_test_split(feature_engineering_result.X, feature_engineering_result.Y,
                                                      test_size=test_size)
    train: TrainDataPair = TrainDataPair(x_train, y_train)
    val: ValDataPair = ValDataPair(x_val, y_val)

    return SplitResult(train, val)
