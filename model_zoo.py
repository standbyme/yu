from dataclasses import dataclass

import lightgbm as lgb
import xgboost as xgb

from sklearn.model_selection import GridSearchCV

from dataclass import TrainDataPair


@dataclass(frozen=True)
class TrainResult:
    MAE: float


def build_model_xgb(train_data_pair: TrainDataPair):
    model = xgb.XGBRegressor(n_estimators=150, learning_rate=0.1, gamma=0, subsample=0.8, colsample_bytree=0.9,
                             max_depth=7)
    model.fit(train_data_pair.x, train_data_pair.y)
    return model


def build_model_lgb(train_data_pair: TrainDataPair):
    estimator = lgb.LGBMRegressor(num_leaves=127, n_estimators=150)
    param_grid = {
        'learning_rate': [0.01, 0.05, 0.1, 0.2],
    }
    gbm = GridSearchCV(estimator, param_grid)
    gbm.fit(train_data_pair.x, train_data_pair.y)
    return gbm
