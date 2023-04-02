import pandas
from catboost import CatBoostRegressor
from catboost._catboost import CatBoostError

from django.utils.timezone import now

from tender_statistics.purchases.models import Region, OKVED
from tender_statistics.predict.inference import get_region_predictions


def get_region_ovked_predictions(
    region: Region | list[Region], ovked: OKVED, mounthes=12
):
    code = str(ovked.code)
    if len(code) == 1:
        code = "0" + code
    if type(region) is list:
        regions = [x.name for x in region]
    else:
        regions = [region.name]
    result = []
    req = {
        "okved": [],
        "delivery_region": [],
        "month": [],
        "year": [],
    }
    for reg in regions:
        year = now().year
        month = now().month
        for i in range(mounthes):
            if month == 12:
                year += 1
                month = 0
            month += 1
            req["okved"].append(code)
            req["delivery_region"].append(reg)
            req["month"].append(month)
            req["year"].append(year)

            r = {"month": month, "year": year}
            if type(region) is list:
                r["region"] = reg
            result.append(r)

    df = pandas.DataFrame.from_dict(req)
    data = get_region_predictions(df)
    for i in range(len(result)):
        result[i]["sum"] = abs(round(data[i][0]))
        result[i]["amount"] = abs(round(data[i][1]))
        result[i]["diff"] = abs(round(data[i][2]))

    return result


print("loading purchases to memory: ...")
purchases = pandas.read_csv("data/purch.csv")
print("loading purchases to memory: done")


def get_predictions_by_company(inn):
    q = purchases[purchases["supplier_inn"] == inn]
    q = q[q["is_win"]]
    q["date"] = [x[:7] for x in q["publish_date"]]
    q2 = q[["date", "final_price"]].groupby("date").count()
    q2.sort_values("date")
    q = q[["date", "final_price"]].groupby("date").sum()
    q.sort_values("date")
    if len(q) == 0 or len(q2) == 0:
        return []
    cur_date = max(q.index)
    res = {"date": [], "price": [], "count": []}
    c_year = int(cur_date[:4])
    c_month = int(cur_date[-2:])
    for _ in range(3):
        c_month += 1
        if c_month == 13:
            c_month = 1
            c_year += 1
        if c_month < 10:
            res["date"].append(f"{c_year}-0{c_month}")
        else:
            res["date"].append(f"{c_year}-{c_month}")
    if len(q) < 3:
        for _ in range(3):
            res["price"].append(q["final_price"].mean())
            res["count"].append(round(q2["final_price"].mean()))
        return pandas.DataFrame(res)
    md = CatBoostRegressor(iterations=200, max_depth=5, verbose=False)
    md2 = CatBoostRegressor(iterations=200, max_depth=5, verbose=False)
    for i in range(1, 3):
        q[f"price_{i}"] = [None for _ in range(i)] + q["final_price"].iloc[:-i].tolist()
        q2[f"price_{i}"] = [None for _ in range(i)] + q2["final_price"].iloc[
            :-i
        ].tolist()
    q["target"] = q["final_price"].iloc[1:].tolist() + [None]
    q2["target"] = q2["final_price"].iloc[1:].tolist() + [None]
    rd = q.iloc[-1].tolist()[:-1]
    q = q.iloc[:-1]
    rd2 = q2.iloc[-1].tolist()[:-1]
    q2 = q2.iloc[:-1]
    try:
        md.fit(q[[x for x in q if x != "target"]], q["target"])
        md2.fit(q[[x for x in q2 if x != "target"]], q2["target"])
        for _ in range(3):
            w = md.predict(rd)
            rd = [w] + rd[1:]
            res["price"].append(w)
            w2 = md2.predict(rd2)
            rd2 = [w2] + rd2[1:]
            res["count"].append(round(w2))
    except CatBoostError:
        for _ in range(3):
            res["price"].append(q["final_price"].mean())
            res["count"].append(round(q2["final_price"].mean()))
    return pandas.DataFrame(res)
