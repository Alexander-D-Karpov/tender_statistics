from django.db import models

from tender_statistics.purchases.models import Region, OKVED, Company


class RegionOKVED(models.Model):
    region = models.ForeignKey(Region, related_name="okveds", on_delete=models.CASCADE)
    okved = models.ForeignKey(OKVED, related_name="regions", on_delete=models.CASCADE)
    sum = models.BigIntegerField(null=True)
    amount = models.BigIntegerField(null=True)


class CompanyOKVED(models.Model):
    okved = models.ForeignKey(OKVED, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.BigIntegerField(null=True)
    amount = models.BigIntegerField(null=True)
    win_price = models.BigIntegerField(null=True)
    win_amount = models.BigIntegerField(null=True)


class CompanyRegion(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.BigIntegerField(null=True)
    amount = models.BigIntegerField(null=True)
    win_price = models.BigIntegerField(null=True)
    win_amount = models.BigIntegerField(null=True)


class CompanyRegionOKVED(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    region_okved = models.ForeignKey(RegionOKVED, on_delete=models.CASCADE)

    price = models.BigIntegerField(null=True)
    amount = models.BigIntegerField(null=True)

    win_price = models.BigIntegerField(null=True)
    win_amount = models.BigIntegerField(null=True)
