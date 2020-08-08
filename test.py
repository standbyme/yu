from sklearn.metrics import mean_absolute_error

import feature_engineering
from feature_engineering import FeatureEngineeringResult
from main import load, split
from model_zoo import build_model_lgb

if __name__ == '__main__':
    train_data = load(r"C:\Users\htsai\Downloads\used_car_train_20200313\used_car_train_20200313.csv", sep=' ')
    test_data = load(r"C:\Users\htsai\Downloads\used_car_testB_20200421\used_car_testB_20200421.csv", sep=' ')
    label_col = 'price'

    feature_engineering_result: FeatureEngineeringResult = feature_engineering.main(train_data, label_col)
    split_result = split(feature_engineering_result, 0.3)

    print('Train lgb...')
    model_lgb = build_model_lgb(split_result.x_train, split_result.y_train)
    val_lgb = model_lgb.predict(split_result.x_val)
    MAE_lgb = mean_absolute_error(split_result.y_val, val_lgb)
    print('MAE of val with lgb:', MAE_lgb)
