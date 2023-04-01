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
)
from tender_statistics.predict.services import get_region_ovked_predictions
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
        return Response(
            data={"predictions": res, "ovked": okved.name, "region": region.name}
        )


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
