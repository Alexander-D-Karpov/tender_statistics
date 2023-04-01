from rest_framework import serializers

from tender_statistics.purchases.models import Region, OKVED, Company, KPGZ


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name"]


class OKVEDSerializer(serializers.ModelSerializer):
    class Meta:
        model = OKVED
        fields = ["code", "name"]


class KPGZSerializer(serializers.ModelSerializer):
    class Meta:
        model = KPGZ
        fields = ["code", "name"]


class CompanySerializer(serializers.ModelSerializer):
    okvds = KPGZSerializer(many=True)

    class Meta:
        model = Company
        fields = ["name", "okvds", "kpp", "active", "managers"]
