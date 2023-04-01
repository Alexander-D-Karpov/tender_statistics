from rest_framework import serializers

from tender_statistics.purchases.api.serializers import CompanySerializer


class PredictOVKEDSerializer(serializers.Serializer):
    region = serializers.IntegerField()
    okved = serializers.IntegerField()


class PredictMultipleOVKEDSerializer(serializers.Serializer):
    regions = serializers.ListSerializer(child=serializers.IntegerField())
    okved = serializers.IntegerField()


class PredictOVKEDCharSerializer(serializers.Serializer):
    region = serializers.CharField()
    okved = serializers.CharField()


class PredictOVKEDResponseCellSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    sum = serializers.FloatField()
    amount = serializers.FloatField()
    diff = serializers.FloatField()


class PredictOVKEDResponseSerializer(serializers.Serializer):
    ovked = serializers.CharField()
    region = serializers.CharField()
    total_sum = serializers.IntegerField()
    total_amount = serializers.IntegerField()
    predictions = serializers.ListSerializer(child=PredictOVKEDResponseCellSerializer())


class PredictOVKEDMultipleResponseCellSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    region = serializers.CharField()
    sum = serializers.FloatField()
    amount = serializers.FloatField()
    diff = serializers.FloatField()


class OKVEDRegionTotalSerializer(serializers.Serializer):
    region = serializers.CharField()
    total_sum = serializers.IntegerField()
    total_amount = serializers.IntegerField()


class PredictOVKEDMultipleResponseSerializer(serializers.Serializer):
    ovked = serializers.CharField()
    total = serializers.ListSerializer(child=OKVEDRegionTotalSerializer())
    predictions = serializers.ListSerializer(
        child=PredictOVKEDMultipleResponseCellSerializer()
    )


class PredictCompanySerializer(serializers.Serializer):
    inn = serializers.IntegerField()
    region = serializers.IntegerField()
    okved = serializers.IntegerField()


class PredictCompanyResponseSerializer(serializers.Serializer):
    company = CompanySerializer()
    company_market_amount = serializers.FloatField()
    company_market_tenders = serializers.IntegerField()
    company_market_tender_wins = serializers.IntegerField()
    company_market_tender_money = serializers.IntegerField()
    region_money = serializers.IntegerField()
    region_tenders = serializers.IntegerField()
