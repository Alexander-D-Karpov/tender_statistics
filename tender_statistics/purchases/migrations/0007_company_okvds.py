# Generated by Django 4.1.7 on 2023-04-01 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchases", "0006_alter_company_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="okvds",
            field=models.ManyToManyField(related_name="companies", to="purchases.kpgz"),
        ),
    ]