# Generated by Django 4.1.7 on 2023-04-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchases", "0007_company_okvds"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="company",
            name="kpp",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="company",
            name="managers",
            field=models.IntegerField(default=0),
        ),
    ]
