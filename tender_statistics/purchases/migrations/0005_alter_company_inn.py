# Generated by Django 4.1.7 on 2023-04-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchases", "0004_region_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="inn",
            field=models.BigIntegerField(
                db_index=True, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
