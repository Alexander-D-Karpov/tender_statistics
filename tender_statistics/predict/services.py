import pandas

from django.utils.timezone import now

from tender_statistics.purchases.models import Region, OKVED
from tender_statistics.predict.inference import get_region_predictions


def get_region_ovked_predictions(region: Region, ovked: OKVED, mounthes=12):
    code = str(ovked.code)
    region = region.name
    if len(code) == 1:
        code = "0" + code
    data = {
        "okved": [],
        "delivery_region": [],
        "month": [],
        "year": [],
    }
    year = now().year
    month = now().month
    result = []
    for i in range(mounthes):
        if month == 12:
            year += 1
            month = 0
        month += 1
        data["okved"].append(code)
        data["delivery_region"].append(region)
        data["month"].append(month)
        data["year"].append(year)

        r = {"month": month, "year": year}
        result.append(r)

    df = pandas.DataFrame.from_dict(data)
    data = get_region_predictions(df)
    for i in range(len(result)):
        result[i]["sum"] = round(data[i][0])
        result[i]["amount"] = round(data[i][1])
        result[i]["diff"] = round(data[i][2])
    return result
