from rest_framework import serializers

from tender_statistics.purchases.models import Region, OKVED, Company, KPGZ
from tender_statistics.statistic.models import CompanyRegionOKVED


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
        fields = [
            "name",
            "okvds",
            "kpp",
            "active",
            "managers",
            "tender_amount",
            "win_amount",
            "total_price",
            "win_price",
        ]


class TopCompanySerializer(serializers.ModelSerializer):
    okvds = KPGZSerializer(many=True)
    top_okved = serializers.SerializerMethodField()

    def get_top_okved(self, obj):
        res = []
        for c in CompanyRegionOKVED.objects.filter(company=obj).order_by("-win_amount")[
            :5
        ]:
            res.append(
                {
                    "region": c.region_okved.region.name,
                    "region_id": c.region_okved.region.id,
                    "okved": c.region_okved.okved.name,
                    "okved_code": c.region_okved.okved.code,
                    "price": c.price,
                    "amount": c.amount,
                    "win_price": c.win_price,
                    "win_amount": c.win_amount,
                }
            )
        return res

    class Meta:
        model = Company
        fields = [
            "inn",
            "name",
            "okvds",
            "top_okved",
            "kpp",
            "active",
            "managers",
            "tender_amount",
            "win_amount",
            "total_price",
            "win_price",
        ]
