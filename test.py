from sklearn.metrics import mean_absolute_error

import feature_engineering
from dataclass import SplitResult
from feature_engineering import FeatureEngineeringResult
from main import load, split
from model_zoo import build_model, LGBMRegressorFactory, XGBRegressorFactory, fusion

if __name__ == '__main__':
    train_data = load(r"C:\Users\htsai\Downloads\used_car_train_20200313\used_car_train_20200313.csv", sep=' ')
    test_data = load(r"C:\Users\htsai\Downloads\used_car_testB_20200421\used_car_testB_20200421.csv", sep=' ')
    label_col = 'price'

    feature_engineering_result: FeatureEngineeringResult = feature_engineering.main(train_data, label_col)
    split_result: SplitResult = split(feature_engineering_result, 0.3)

    build_model_result_a = build_model(LGBMRegressorFactory(), split_result)
    print('MAE of val with lgb:', build_model_result_a.MAE)

    build_model_result_b = build_model(XGBRegressorFactory(), split_result)
    print('MAE of val with xgb:', build_model_result_b.MAE)

    fusion_model_result = fusion([build_model_result_a, build_model_result_b], split_result)
    print('MAE of val with fusion:', fusion_model_result.MAE)
