from typing import Any, Optional, Dict, List

import lightgbm as lgb
import xgboost as xgb
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV

from dataclass import SplitResult, BuildModelResult, FusionResult


class ModelFactory:
    def get(self) -> Any:
        pass


class LGBMRegressorFactory(ModelFactory):
    def get(self):
        return lgb.LGBMRegressor(num_leaves=127, n_estimators=150)


class XGBRegressorFactory(ModelFactory):
    def get(self):
        return xgb.XGBRegressor(n_estimators=150, learning_rate=0.1, gamma=0, subsample=0.8, colsample_bytree=0.9,
                                max_depth=7)


def build_model(model_factory: ModelFactory, split_result: SplitResult,
                param_grid: Optional[Dict[str, List]] = None) -> BuildModelResult:
    model = model_factory.get()

    if param_grid:
        model = GridSearchCV(model, param_grid)

    model.fit(split_result.train.x, split_result.train.y)

    val = model.predict(split_result.val.x)
    MAE = mean_absolute_error(split_result.val.y, val)

    return BuildModelResult(model, MAE, val)


def fusion(build_model_results: List[BuildModelResult], split_result: SplitResult) -> BuildModelResult:
    model_result_0: BuildModelResult = build_model_results[0]
    model_result_1: BuildModelResult = build_model_results[1]
    MAE_sum = model_result_0.MAE + model_result_1.MAE

    # noinspection PyTypeChecker
    a = model_result_0.val * (1 - model_result_0.MAE / MAE_sum)
    # noinspection PyTypeChecker
    b = model_result_1.val * (1 - model_result_1.MAE / MAE_sum)

    val = a + b
    MAE = mean_absolute_error(split_result.val.y, val)

    def func(x):
        func_a_val = model_result_0.model.predict(x)
        func_b_val = model_result_1.model.predict(x)
        func_a = func_a_val * (1 - model_result_0.MAE / MAE_sum)
        func_b = func_b_val * (1 - model_result_1.MAE / MAE_sum)
        return func_a + func_b

    return BuildModelResult(FusionResult(func), MAE, val)
