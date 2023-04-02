from tender_statistics.predict.services import (
    get_predictions_by_company,
)
from tender_statistics.purchases.models import Company


def get_company_predictions(company: Company):
    data = get_predictions_by_company(company.inn)
    res = []
    if type(data) is not list:
        for i, row in data.iterrows():
            res.append(
                {
                    "month": row.date.split("-")[1],
                    "year": row.date.split("-")[0],
                    "price": str(row.price),
                    "amount": str(row.count),
                }
            )
    return res
