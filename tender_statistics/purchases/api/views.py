from rest_framework import generics

from tender_statistics.purchases.models import Region, OKVED
from .serializers import (
    RegionSerializer,
    OKVEDSerializer,
)


class ListRegionView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ListOKVEDView(generics.ListAPIView):
    queryset = OKVED.objects.all()
    serializer_class = OKVEDSerializer
