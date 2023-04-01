from rest_framework import serializers


class PredictOVKEDSerializer(serializers.Serializer):
    region = serializers.IntegerField()
    okved = serializers.IntegerField()


class PredictOVKEDResponseCellSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    amount = serializers.FloatField()


class PredictOVKEDResponseSerializer(serializers.Serializer):
    predictions = serializers.ListSerializer(child=PredictOVKEDResponseCellSerializer())


class PredictCompanySerializer(serializers.Serializer):
    inn = serializers.IntegerField()
    region = serializers.IntegerField()
    okved = serializers.IntegerField()


class PredictCompanyResponseSerializer(serializers.Serializer):
    company_market_amount = serializers.FloatField()
    company_market_tenders = serializers.IntegerField()
    company_market_tender_wins = serializers.IntegerField()
    company_market_tender_money = serializers.IntegerField()
    region_money = serializers.IntegerField()
    region_tenders = serializers.IntegerField()
