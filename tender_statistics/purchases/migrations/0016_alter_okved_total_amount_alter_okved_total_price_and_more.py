# Generated by Django 4.1.7 on 2023-04-02 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchases", "0015_okved_total_amount_okved_total_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="okved",
            name="total_amount",
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="okved",
            name="total_price",
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="region",
            name="total_amount",
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="region",
            name="total_price",
            field=models.BigIntegerField(default=0),
        ),
    ]