# Generated by Django 4.1.7 on 2023-04-01 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("statistic", "0002_alter_regionokved_amount_alter_regionokved_sum"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companyregionokved",
            name="amount",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="companyregionokved",
            name="price",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="regionokved",
            name="amount",
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="regionokved",
            name="sum",
            field=models.BigIntegerField(null=True),
        ),
    ]
