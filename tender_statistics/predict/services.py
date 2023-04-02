import pandas

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
