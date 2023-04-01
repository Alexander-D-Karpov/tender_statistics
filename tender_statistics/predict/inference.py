from catboost import CatBoostRegressor

reg_sum = CatBoostRegressor()
reg_sum.load_model("tender_statistics/predict/ml/tenderhack_sum.cb")

reg_amount = CatBoostRegressor()
reg_amount.load_model("tender_statistics/predict/ml/tenderhack_count.cb")

reg_diff = CatBoostRegressor()
reg_diff.load_model("tender_statistics/predict/ml/tenderhack_diff.cb")


def get_region_predictions(data):
    data1 = reg_sum.predict(data)
    data2 = reg_amount.predict(data)
    data3 = reg_diff.predict(data)
    res = []
    for i in range(len(data1)):
        res.append((data1[i], data2[i], data3[i]))
    return res
