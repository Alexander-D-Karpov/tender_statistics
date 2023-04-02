from rest_framework import generics

from tender_statistics.purchases.models import Region, OKVED, Company
from .serializers import (
    RegionSerializer,
    OKVEDSerializer,
    TopCompanySerializer,
)


class ListRegionView(generics.ListAPIView):
    queryset = Region.objects.all().order_by("id")
    serializer_class = RegionSerializer


class ListOKVEDView(generics.ListAPIView):
    queryset = OKVED.objects.all()
    serializer_class = OKVEDSerializer


class TopCompaniesView(generics.ListAPIView):
    serializer_class = TopCompanySerializer
    queryset = Company.objects.order_by("-win_price")[:20]
