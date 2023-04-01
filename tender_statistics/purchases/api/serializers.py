from rest_framework import serializers

from tender_statistics.purchases.models import Region, OKVED


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name"]


class OKVEDSerializer(serializers.ModelSerializer):
    class Meta:
        model = OKVED
        fields = ["code", "name"]
