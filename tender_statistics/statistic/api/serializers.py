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


class CompanyPrediction(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    amount = serializers.IntegerField()
    sum = serializers.IntegerField()


class PredictCompanyResponseSerializer(serializers.Serializer):
    company = CompanySerializer()
    predictions = serializers.ListSerializer(child=CompanyPrediction())
    company_market_amount = serializers.FloatField()
    company_market_tenders = serializers.IntegerField()
    company_market_tender_wins = serializers.IntegerField()
    company_market_tender_money = serializers.IntegerField()
    region_money = serializers.IntegerField()
    region_tenders = serializers.IntegerField()


class CompanyRequestSerializer(serializers.Serializer):
    inn = serializers.IntegerField()


class CompanyOKVEDSerializer(serializers.Serializer):
    okved = serializers.CharField()
    company_total_price = serializers.IntegerField()
    company_total_amount = serializers.IntegerField()
    company_win_price = serializers.IntegerField()
    company_win_amount = serializers.IntegerField()
    total_price = serializers.IntegerField()
    total_amount = serializers.IntegerField()


class CompanyRegionSerializer(serializers.Serializer):
    region = serializers.CharField()
    company_total_price = serializers.IntegerField()
    company_total_amount = serializers.IntegerField()
    company_win_price = serializers.IntegerField()
    company_win_amount = serializers.IntegerField()
    total_price = serializers.IntegerField()
    total_amount = serializers.IntegerField()


class CompetetorSerializer(serializers.Serializer):
    inn = serializers.IntegerField()
    okved = serializers.CharField()
    predictions = serializers.ListSerializer(child=CompanyPrediction())


class FullCompanySerializer(serializers.Serializer):
    okveds = serializers.ListSerializer(child=CompanyOKVEDSerializer())
    regions = serializers.ListSerializer(child=CompanyRegionSerializer())
    competetors = serializers.ListSerializer(child=CompetetorSerializer())
    predictions = serializers.ListSerializer(child=CompanyPrediction())
    company = CompanySerializer()


class RegionOKVEDSerializer(serializers.Serializer):
    code = serializers.IntegerField()


class RegionOKVEDResponseCellSerializer(serializers.Serializer):
    region = serializers.CharField()
    sum = serializers.IntegerField()


class RegionOKVEDResponseSerializer(serializers.Serializer):
    regions = serializers.ListSerializer(child=RegionOKVEDResponseCellSerializer())


class OKVEDDestribution(serializers.Serializer):
    name = serializers.CharField()
    amount = serializers.IntegerField()


class GlobalSerializer(serializers.Serializer):
    regions_count = serializers.IntegerField()
    okved_count = serializers.IntegerField()
    destribution = serializers.ListSerializer(child=OKVEDDestribution())
    company_amount = serializers.IntegerField()
    total_amount = serializers.IntegerField()
    total_sum = serializers.IntegerField()
