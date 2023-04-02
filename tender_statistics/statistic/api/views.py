from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from tender_statistics.purchases.models import Region, OKVED, Company
from .serializers import (
    PredictOVKEDSerializer,
    PredictOVKEDResponseSerializer,
    PredictCompanySerializer,
    PredictCompanyResponseSerializer,
    PredictOVKEDCharSerializer,
    PredictMultipleOVKEDSerializer,
    PredictOVKEDMultipleResponseSerializer,
    CompanyRequestSerializer,
    FullCompanySerializer,
)
from tender_statistics.predict.services import get_region_ovked_predictions
from tender_statistics.statistic.models import (
    RegionOKVED,
    CompanyRegionOKVED,
    CompanyOKVED,
    CompanyRegion,
)
from tender_statistics.purchases.api.serializers import CompanySerializer


class PredictOKVEDView(generics.GenericAPIView):
    serializer_class = PredictOVKEDSerializer

    @extend_schema(
        request=PredictOVKEDSerializer,
        responses={200: PredictOVKEDResponseSerializer},
    )
    def post(self, request, *args, **kwargs):
        serializer = PredictOVKEDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        region = get_object_or_404(Region, id=data["region"])
        okved = get_object_or_404(OKVED, code=data["okved"])
        res = get_region_ovked_predictions(region, okved)
        data = {
            "predictions": res,
            "ovked": okved.name,
            "region": region.name,
        }
        if RegionOKVED.objects.filter(region=region, okved=okved).exists():
            reg_okv = RegionOKVED.objects.get(region=region, okved=okved)
            data["total_sum"] = reg_okv.sum
            data["total_amount"] = reg_okv.amount
        else:
            data["total_sum"] = 0
            data["total_amount"] = 0

        if data["total_sum"] == 0:
            re = []
            for el in data["predictions"]:
                re.append(
                    {
                        "year": el["year"],
                        "month": el["month"],
                        "sum": 0,
                        "amount": 0,
                        "diff": 0,
                    }
                )
            data["predictions"] = re
        return Response(data=data)


class PredictMultipleOKVEDView(generics.GenericAPIView):
    serializer_class = PredictMultipleOVKEDSerializer

    @extend_schema(
        request=PredictMultipleOVKEDSerializer,
        responses={200: PredictOVKEDMultipleResponseSerializer},
    )
    def post(self, request, *args, **kwargs):
        serializer = PredictMultipleOVKEDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        regions = [get_object_or_404(Region, id=x) for x in data["regions"]]
        okved = get_object_or_404(OKVED, code=data["okved"])
        res = get_region_ovked_predictions(regions, okved)
        data = {
            "predictions": res,
            "total": [],
            "ovked": okved.name,
        }
        i = 0
        for reg in regions:
            r = {
                "region": reg.name,
                "total_sum": 0,
                "total_amount": 0,
            }
            if RegionOKVED.objects.filter(region=reg, okved=okved).exists():
                reg_okv = RegionOKVED.objects.get(region=reg, okved=okved)
                r["total_sum"] = reg_okv.sum
                r["total_amount"] = reg_okv.amount
            data["total"].append(r)
            for j in range(i, i + 12):
                data["predictions"][j] = {
                    "year": data["predictions"][j]["year"],
                    "month": data["predictions"][j]["month"],
                    "region": data["predictions"][j]["region"],
                    "sum": 0,
                    "amount": 0,
                    "diff": 0,
                }
            i += 12
        return Response(data=data)


class PredictOKVEDCharView(generics.GenericAPIView):
    serializer_class = PredictOVKEDCharSerializer

    @extend_schema(
        request=PredictOVKEDCharSerializer,
        responses={200: PredictOVKEDResponseSerializer},
    )
    def post(self, request, *args, **kwargs):
        serializer = PredictOVKEDCharSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        region = get_object_or_404(Region, name=data["region"])
        okved = get_object_or_404(OKVED, name=data["okved"])
        res = get_region_ovked_predictions(region, okved)
        data = {
            "predictions": res,
            "ovked": okved.name,
            "region": region.name,
        }
        if RegionOKVED.objects.filter(region=region, okved=okved).exists():
            reg_okv = RegionOKVED.objects.get(region=region, okved=okved)
            data["total_sum"] = reg_okv.sum
            data["total_amount"] = reg_okv.amount
        else:
            data["total_sum"] = 0
            data["total_amount"] = 0

        if data["total_sum"] == 0:
            data["predictions"] = []
        return Response(data=data)


class PredictCompanyView(generics.GenericAPIView):
    serializer_class = PredictCompanySerializer

    @extend_schema(
        request=PredictCompanySerializer,
        responses={200: PredictCompanyResponseSerializer},
    )
    def post(self, request, *args, **kwargs):
        serializer = PredictCompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        region = get_object_or_404(Region, id=data["region"])
        okved = get_object_or_404(OKVED, code=data["okved"])
        reg_okv = get_object_or_404(RegionOKVED, region=region, okved=okved)
        company = get_object_or_404(Company, inn=data["inn"])
        company_reg_okv = get_object_or_404(
            CompanyRegionOKVED, company=company, region_okved=reg_okv
        )
        return Response(
            data={
                "company": CompanySerializer().to_representation(company),
                "company_market_amount": company_reg_okv.price,
                "company_market_tenders": company_reg_okv.amount,
                "company_market_tender_wins": company_reg_okv.win_price,
                "company_market_tender_money": company_reg_okv.win_amount,
                "region_money": reg_okv.sum,
                "region_tenders": reg_okv.amount,
            }
        )


class FullCompanyView(generics.GenericAPIView):
    serializer_class = CompanyRequestSerializer

    @extend_schema(
        request=CompanyRequestSerializer,
        responses={200: FullCompanySerializer},
    )
    def post(self, request, *args, **kwargs):
        serializer = CompanyRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inn = serializer.data["inn"]
        company = get_object_or_404(Company, inn=inn)
        okveds = []
        for okved in CompanyOKVED.objects.filter(company=company).order_by(
            "-win_price"
        ):
            okveds.append(
                {
                    "okved": okved.okved.name,
                    "company_total_price": okved.price,
                    "company_total_amount": okved.amount,
                    "company_win_price": okved.win_price,
                    "company_win_amount": okved.win_amount,
                    "total_price": okved.okved.total_price,
                    "total_amount": okved.okved.total_amount,
                }
            )
        regions = []
        for reg in CompanyRegion.objects.filter(company=company).order_by("-win_price"):
            regions.append(
                {
                    "region": reg.region.name,
                    "company_total_price": reg.price,
                    "company_total_amount": reg.amount,
                    "company_win_price": reg.win_price,
                    "company_win_amount": reg.win_amount,
                    "total_price": reg.region.total_price,
                    "total_amount": reg.region.total_amount,
                }
            )
        print(company.rev_competetors)
        return Response(
            data={
                "company": CompanySerializer().to_representation(company),
                "competetors": company.competetors.all().values_list("inn", flat=True),
                "okveds": okveds,
                "regions": regions,
            }
        )
