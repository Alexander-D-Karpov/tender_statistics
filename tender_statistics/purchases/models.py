from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=200)


class KPGZ(models.Model):
    okved = models.ForeignKey(
        "OKVED", related_name="kpgz", null=True, on_delete=models.SET_NULL
    )
    code = models.CharField(unique=True, max_length=30, db_index=True)
    name = models.CharField(max_length=433)


class OKVED(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)


class Lot(models.Model):
    name = models.CharField(unique=True, max_length=400)


class Purchase(models.Model):
    id = models.IntegerField(db_index=True, unique=True, primary_key=True)
    name = models.CharField(max_length=400)
    lots = models.ManyToManyField(Lot, related_name="purchases")
    price = models.IntegerField()
    customer = models.ForeignKey(
        "Company", related_name="orders", null=True, on_delete=models.SET_NULL
    )
    supplier = models.ForeignKey(
        "Company", related_name="supplies", null=True, on_delete=models.SET_NULL
    )


class Company(models.Model):
    inn = models.BigIntegerField(unique=True, db_index=True, primary_key=True)
    name = models.CharField(max_length=500)
    okvds = models.ManyToManyField(KPGZ, related_name="companies")
    kpp = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    managers = models.IntegerField(default=0)
