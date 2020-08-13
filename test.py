from typing import Dict, Any, Union, List

import pandas as pd

from dataclass import SplitResult, DataInfo, ColumnInfo, PredictDataInfo, TrainDataInfo
from feature_engineering import TrainFeatureEngineeringResult, verify, train_feature_engineering, \
    predict_feature_engineering
from main import load, split
from model_zoo import build_model, LGBMRegressorFactory, XGBRegressorFactory, fusion

if __name__ == '__main__':
    train_data = load(r"C:\Users\htsai\Downloads\used_car_train_20200313\used_car_train_20200313.csv", sep=' ')
    predict_data = load(r"C:\Users\htsai\Downloads\used_car_testB_20200421\used_car_testB_20200421.csv", sep=' ')
    label_column: ColumnInfo = ColumnInfo('price', 'int')

    feature_columns: List[ColumnInfo] = [
        ColumnInfo('SaleID', 'int', True),
        ColumnInfo('name', 'int', True),
        ColumnInfo('regDate', 'int', True),
        ColumnInfo('model', 'float'),
        ColumnInfo('brand', 'int'),
        ColumnInfo('bodyType', 'float'),
        ColumnInfo('fuelType', 'float'),
        ColumnInfo('gearbox', 'float'),
        ColumnInfo('power', 'int'),
        ColumnInfo('kilometer', 'float'),
        ColumnInfo('notRepairedDamage', 'int'),
        ColumnInfo('regionCode', 'int'),
        ColumnInfo('seller', 'int'),
        ColumnInfo('offerType', 'int'),
        ColumnInfo('creatDate', 'int'),
        ColumnInfo('v_0', 'float'),
        ColumnInfo('v_1', 'float'),
        ColumnInfo('v_2', 'float'),
        ColumnInfo('v_3', 'float'),
        ColumnInfo('v_4', 'float'),
        ColumnInfo('v_5', 'float'),
        ColumnInfo('v_6', 'float'),
        ColumnInfo('v_7', 'float'),
        ColumnInfo('v_8', 'float'),
        ColumnInfo('v_9', 'float'),
        ColumnInfo('v_10', 'float'),
        ColumnInfo('v_11', 'float'),
        ColumnInfo('v_12', 'float'),
        ColumnInfo('v_13', 'float'),
        ColumnInfo('v_14', 'float')
    ]

    predict_expected_info = PredictDataInfo(feature_columns, 50000)
    verify(predict_data, predict_expected_info)

    train_expected_info = TrainDataInfo(feature_columns, 150000, label_column)
    verify(train_data, train_expected_info)

    train_feature_engineering_result: TrainFeatureEngineeringResult = train_feature_engineering(
        train_data, train_expected_info)
    split_result: SplitResult = split(train_feature_engineering_result, 0.3)

    build_model_result_a = build_model(LGBMRegressorFactory(), split_result)
    print('MAE of val with lgb:', build_model_result_a.MAE)

    build_model_result_b = build_model(XGBRegressorFactory(), split_result)
    print('MAE of val with xgb:', build_model_result_b.MAE)

    fusion_model_result = fusion([build_model_result_a, build_model_result_b], split_result)
    print('MAE of val with fusion:', fusion_model_result.MAE)

    predict_feature_data = fusion_model_result.model.predict(
        predict_feature_engineering(predict_data, train_feature_engineering_result))

    sub = pd.DataFrame()
    sub['SaleID'] = predict_data.SaleID
    sub['price'] = predict_feature_data
    sub.to_csv('./sub_Weighted.csv', index=False)
