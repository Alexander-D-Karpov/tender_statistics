from catboost import CatBoostRegressor

reg = CatBoostRegressor()
reg.load_model("tender_statistics/predict/ml/tenderhack_sum.cb")


def get_region_predictions(data):
    data = reg.predict(data)
    return data
