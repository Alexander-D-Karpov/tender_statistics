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
)
from tender_statistics.predict.services import get_region_ovked_predictions
from ..models import RegionOKVED
from ...purchases.api.serializers import CompanySerializer


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
        for reg in regions:
            r = {
                "region": reg.name,
                "total_sum": 0,
                "total_amount": 0,
            }
            if RegionOKVED.objects.filter(region=reg, okved=okved).exists():
                reg_okv = RegionOKVED.objects.get(region=reg, okved=okved)
                r["total"] = reg_okv.sum
                r["total_amount"] = reg_okv.amount
            data["total"].append(r)
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
        company = get_object_or_404(Company, inn=data["inn"])
        return Response(
            data={
                "company": CompanySerializer().to_representation(company),
                "company_market_amount": 0.0,
                "company_market_tenders": 0,
                "company_market_tender_wins": 0,
                "company_market_tender_money": 0,
                "region_money": 0,
                "region_tenders": 0,
            }
        )
