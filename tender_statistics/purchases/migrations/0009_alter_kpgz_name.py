# Generated by Django 4.1.7 on 2023-04-01 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchases", "0008_company_active_company_kpp_company_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kpgz",
            name="name",
            field=models.CharField(max_length=433),
        ),
    ]
